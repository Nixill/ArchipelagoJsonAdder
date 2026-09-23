import binascii
import struct
import datetime
import math

def fileToHexString(filepath):
    f = open(filepath, 'rb')
    hexString = str(binascii.hexlify(f.read()))
    f.close()
    return hexString

def hexToString(hexstring):
    return bytes.fromhex(hexstring).decode('utf-8')

def hexToInt(hexstring):
    return int.from_bytes(bytes.fromhex(hexstring), byteorder="little")

def hexToFloat(hexString):
    return struct.unpack('f',bytes.fromhex(hexString))[0]

def floatToClearTime(time):
    time = math.floor(time)
    return str(datetime.timedelta(seconds = time))

def parseLevelData(fullHex,initialOffset):
    offset = initialOffset
    
    # Level Name:
    levelNameLength = hexToInt(fullHex[offset:offset+8])*2
    offset += 8
    levelNameHex = fullHex[offset:offset+levelNameLength-2]
    levelName = hexToString(levelNameHex)
    offset += levelNameLength
    
    # LowestClearTime:
    offset += 94
    clearTimeHex = fullHex[offset:offset+8]
    clearTime = hexToFloat(clearTimeHex)
    offset += 8
    
    # HighestCrystalCount:
    offset += 98
    crystalCountHex = fullHex[offset:offset+8]
    crystalCount = hexToInt(crystalCountHex)
    offset += 8
    
    # HighestOreCount:
    offset += 90
    oreCountHex = fullHex[offset:offset+8]
    oreCount = hexToInt(oreCountHex)
    offset += 8
    
    # HighestCreatureKillCount:
    # NB: Stat exists but game does not actually populate it!
    offset += 108
    killCountHighHex = fullHex[offset:offset+8]
    killCountHigh = hexToInt(killCountHighHex)
    offset += 8
    
    # LowestCreatureKillCount:
    # NB: Stat exists but game does not actually populate it!
    offset += 106
    killCountLowHex = fullHex[offset:offset+8]
    killCountLow = hexToInt(killCountLowHex)
    offset += 8
    
    # LowestMinersLost:
    # NB: Stat exists but game does not actually populate it!
    offset += 92
    minersLostHex = fullHex[offset:offset+8]
    minersLost = hexToInt(minersLostHex)
    offset += 8
    
    # MostCavernsDiscovered:
    offset += 102
    cavernCountHex = fullHex[offset:offset+8]
    cavernCount = hexToInt(cavernCountHex)
    offset += 8
    
    # Not currently parsing "ClearedModes" but need the offset:
    offset += 152
    
    return (levelName,clearTime,crystalCount,oreCount,killCountHigh,killCountLow,minersLost,cavernCount,offset)

def parseAllLevels(hexString):
    # Hex value for "ClearedLevelStats"
    levelDataStartString = "436c65617265644c6576656c735374617473"
    levelDataStartIndex = hexString.find(levelDataStartString)
    # Offset from the above to first level data line
    firstOffset = 174
    
    # Count levels based on occurrences of hex for "LowestClearTime"
    overallLevelCount = hexString.count("4c6f77657374436c65617254696d65")
    counter = overallLevelCount
    offset = levelDataStartIndex + firstOffset
    
    levelDataList = []
    
    while (counter > 0):
        levelData = parseLevelData(hexString,offset)
        levelDataList.append(levelData)
        offset = levelData[8]
        counter -= 1
    
    return levelDataList

def parseAllLevelsFromFilepath(filepath):
    hexString = fileToHexString(filepath)
    levelDataList = parseAllLevels(hexString)
    return levelDataList

#####################
# Currently unused by Archipelago but could be handy to hold around for future features...
#####################

def printLevelData(levelData):
    print("Level Name: " + levelData[0])
    print("Lowest Clear Time: " + floatToClearTime(levelData[1]))
    print("Highest Crystal Count: " + str(levelData[2]))
    print("Highest Ore Count: " + str(levelData[3]))
    print("Highest Creature Kill Count: " + str(levelData[4]))
    print("Lowest Creature Kill Count: " + str(levelData[5]))
    print("Lowest Miners Lost: " + str(levelData[6]))
    print("Most Caverns Discovered: " + str(levelData[7]))

def parseAndPrint(hexString,prefix=""):
    # Hex value for "ClearedLevelStats"
    levelDataStartString = "436c65617265644c6576656c735374617473"
    levelDataStartIndex = hexString.find(levelDataStartString)
    # Offset from the above to first level data line
    firstOffset = 174

    # Count levels based on occurrences of hex for "LowestClearTime"
    overallLevelCount = hexString.count("4c6f77657374436c65617254696d65")
    counter = overallLevelCount
    offset = levelDataStartIndex + firstOffset

    totalLevelCount = 0
    totalClearTime = 0.0
    totalCrystalCount = 0
    totalOreCount = 0
    totalKillCountHigh = 0
    totalKillCountLow = 0
    totalMinersLost = 0
    totalCavernCount = 0

    while (counter > 0):
        levelData = parseLevelData(hexString,offset)
        if (levelData[0].find(prefix) == 0):
            printLevelData(levelData)
            print("")
            
            totalLevelCount += 1
            totalClearTime += levelData[1]
            totalCrystalCount += levelData[2]
            totalOreCount += levelData[3]
            totalKillCountHigh += levelData[4]
            totalKillCountLow += levelData[5]
            totalMinersLost += levelData[6]
            totalCavernCount += levelData[7]
            
        offset = levelData[8]
        counter -= 1

    if (totalLevelCount == 0):
        print("No level data found for supplied prefix.")
    elif (totalLevelCount > 1):
        print("Total Levels Cleared: " + str(totalLevelCount))
        print("Total Lowest Clear Time: " + floatToClearTime(totalClearTime))
        print("Total Highest Crystal Count: " + str(totalCrystalCount))
        print("Total Highest Ore Count: " + str(totalOreCount))
        print("Total Highest Creature Kill Count: " + str(totalKillCountHigh))
        print("Total Lowest Creature Kill Count: " + str(totalKillCountLow))
        print("Total Lowest Miners Lost: " + str(totalMinersLost))
        print("Total Most Caverns Discovered: " + str(totalCavernCount))

