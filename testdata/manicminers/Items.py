from __future__ import annotations

import pathlib
import shutil
import platform

from BaseClasses import Item, ItemClassification
from typing import TYPE_CHECKING
if TYPE_CHECKING:    
    from .World import ManicMinersWorld


class ManicMinersItem(Item):
    game = "Manic Miners"

ITEM_NAME_TO_ID = {
    #Reserve 0XXX for base game, 1XXX for LRRR, 2XXX for LRRC, 3XXX for BAZ
    #Add filler items counting down from 999
    #Add unlock items counting down from 899
    "Level Access: LRR - A Breath Of Fresh Air": 1,
    "Level Access: LRR - Air Raiders": 2,
    "Level Access: LRR - Back To Basics": 3,
    "Level Access: LRR - Breathless": 4,
    "Level Access: LRR - Don't Panic": 5,
    "Level Access: LRR - Driller Night": 6,
    "Level Access: LRR - Erode Works": 7,
    "Level Access: LRR - Explosive Action": 8,
    "Level Access: LRR - Fire And Water": 9,
    "Level Access: LRR - Frozen Frenzy": 10,
    "Level Access: LRR - Hot Stuff": 11,
    "Level Access: LRR - Ice Spy": 12,
    "Level Access: LRR - It's A Hold Up": 13,
    "Level Access: LRR - Lake Of Fire": 14,
    "Level Access: LRR - Lava Laughter": 15,
    "Level Access: LRR - Oresome": 16,
    "Level Access: LRR - Rock Hard": 17,
    "Level Access: LRR - Rocky Horror": 18,
    "Level Access: LRR - Rubble Trouble": 19,
    "Level Access: LRR - Run The Gauntlet": 20,
    "Level Access: LRR - Search And Rescue": 21,
    "Level Access: LRR - Split Down The Middle": 22,
    "Level Access: LRR - The Path To Power": 23,
    "Level Access: LRR - Water Lot Of Fun": 24,
    "Level Access: LRR - Water Works": 25,
    
    "Level Access: LRRR - A Breath Of Fresh Air": 1001,
    "Level Access: LRRR - Air Raiders": 1002,
    "Level Access: LRRR - Back To Basics": 1003,
    "Level Access: LRRR - Breathless": 1004,
    "Level Access: LRRR - Don't Panic": 1005,
    "Level Access: LRRR - Driller Night": 1006,
    "Level Access: LRRR - Erode Works": 1007,
    "Level Access: LRRR - Explosive Action": 1008,
    "Level Access: LRRR - Fire And Water": 1009,
    "Level Access: LRRR - Frozen Frenzy": 1010,
    "Level Access: LRRR - Hot Stuff": 1011,
    "Level Access: LRRR - Ice Spy": 1012,
    "Level Access: LRRR - It's A Hold Up": 1013,
    "Level Access: LRRR - Lake Of Fire": 1014,
    "Level Access: LRRR - Lava Laughter": 1015,
    "Level Access: LRRR - Oresome": 1016,
    "Level Access: LRRR - Rock Hard": 1017,
    "Level Access: LRRR - Rocky Horror": 1018,
    "Level Access: LRRR - Rubble Trouble": 1019,
    "Level Access: LRRR - Run The Gauntlet": 1020,
    "Level Access: LRRR - Search And Rescue": 1021,
    "Level Access: LRRR - Split Down The Middle": 1022,
    "Level Access: LRRR - The Path To Power": 1023,
    "Level Access: LRRR - Water Lot Of Fun": 1024,
    "Level Access: LRRR - Water Works": 1025,
    
    "Level Access: LRRC - A Breath Of Fresh Air": 2001,
    "Level Access: LRRC - Air Raiders": 2002,
    "Level Access: LRRC - Back To Basics": 2003,
    "Level Access: LRRC - Breathless": 2004,
    "Level Access: LRRC - Don't Panic": 2005,
    "Level Access: LRRC - Driller Night": 2006,
    "Level Access: LRRC - Erode Works": 2007,
    "Level Access: LRRC - Explosive Action": 2008,
    "Level Access: LRRC - Fire And Water": 2009,
    "Level Access: LRRC - Frozen Frenzy": 2010,
    "Level Access: LRRC - Hot Stuff": 2011,
    "Level Access: LRRC - Ice Spy": 2012,
    "Level Access: LRRC - It's A Hold Up": 2013,
    "Level Access: LRRC - Lake Of Fire": 2014,
    "Level Access: LRRC - Lava Laughter": 2015,
    "Level Access: LRRC - Oresome": 2016,
    "Level Access: LRRC - Rock Hard": 2017,
    "Level Access: LRRC - Rocky Horror": 2018,
    "Level Access: LRRC - Rubble Trouble": 2019,
    "Level Access: LRRC - Run The Gauntlet": 2020,
    "Level Access: LRRC - Search And Rescue": 2021,
    "Level Access: LRRC - Split Down The Middle": 2022,
    "Level Access: LRRC - The Path To Power": 2023,
    "Level Access: LRRC - Water Lot Of Fun": 2024,
    "Level Access: LRRC - Water Works": 2025,
    
    "Level Access: BAZ - A Breath Of Fresh Air": 3001,
    "Level Access: BAZ - Air Raiders": 3002,
    "Level Access: BAZ - Back To Basics": 3003,
    "Level Access: BAZ - Breathless": 3004,
    "Level Access: BAZ - Cold Comfort": 3005,
    "Level Access: BAZ - Don't Panic": 3006,
    "Level Access: BAZ - Down In The Dirt": 3007,
    "Level Access: BAZ - Driller Night": 3008,
    "Level Access: BAZ - Erode Works": 3009,
    "Level Access: BAZ - Explosive Action": 3010,
    "Level Access: BAZ - Fire And Water": 3011,
    "Level Access: BAZ - Frozen Frenzy": 3012,
    "Level Access: BAZ - Hot Stuff": 3013,
    "Level Access: BAZ - Ice Spy": 3014,
    "Level Access: BAZ - It's A Hold Up": 3015,
    "Level Access: BAZ - Lake Of Fire": 3016,
    "Level Access: BAZ - Lava Laughter": 3017,
    "Level Access: BAZ - Mine Over Matter": 3018,
    "Level Access: BAZ - Molten Meltdown": 3019,
    "Level Access: BAZ - Oresome": 3020,
    "Level Access: BAZ - Recruitment": 3021,
    "Level Access: BAZ - Rock Hard": 3022,
    "Level Access: BAZ - Rocky Horror": 3023,
    "Level Access: BAZ - Rubble Trouble": 3024,
    "Level Access: BAZ - Run The Gauntlet": 3025,
    "Level Access: BAZ - Seamless": 3026,
    "Level Access: BAZ - Search And Rescue": 3027,
    "Level Access: BAZ - Slimey Simple": 3028,
    "Level Access: BAZ - Split Down The Middle": 3029,
    "Level Access: BAZ - The Hard Rock Life": 3030,
    "Level Access: BAZ - The Path To Power": 3031,
    "Level Access: BAZ - Water Lot Of Fun": 3032,
    "Level Access: BAZ - Water Works": 3033,
    
    "Building Unlock: Tool Store": 899,
    "Building Unlock: Teleport Pad": 898,
    "Building Unlock: Docks": 897,
    "Building Unlock: Canteen": 896,
    "Building Unlock: Power Station": 895,
    "Building Unlock: Support Station": 894,
    "Building Unlock: Upgrade Station": 893,
    "Building Unlock: Geological Center": 892,
    "Building Unlock: Ore Refinery": 891,
    "Building Unlock: Mining Laser": 890,
    "Building Unlock: Super Teleport": 889,
    
    "Item Unlock: Electric Fence": 888,
    "Item Unlock: Dynamite": 887,
    
    "Vehicle Unlock: Hover Scout": 886,
    "Vehicle Unlock: Tunnel Scout": 885,
    "Vehicle Unlock: Small Digger": 884,
    "Vehicle Unlock: Small Transport Truck": 883,
    "Vehicle Unlock: Small Mobile Laser Cutter": 882,
    "Vehicle Unlock: Rapid Rider": 881,
    "Vehicle Unlock: Cargo Carrier": 880,
    "Vehicle Unlock: Loader Dozer": 879,
    "Vehicle Unlock: Granite Grinder": 878,
    "Vehicle Unlock: Large Mobile Laser Cutter": 877,
    "Vehicle Unlock: Chrome Crusher": 876,
    "Vehicle Unlock: Tunnel Transport": 875,
    
    "Transporter Coordinates": 874,
    
    "An Energy Crystal Has Been Found!": 999,
    "Good Work, Cadet!": 998,
    "A Monster Has Appeared!": 997,
    "Well Done!": 996,
    
    "Increased Starting Ore": 950,    
    "Chief's Favourite Truck": 949
    
}

DEFAULT_ITEM_CLASSIFICATIONS = {
    "Level Access: LRR - A Breath Of Fresh Air": ItemClassification.progression,
    "Level Access: LRR - Air Raiders": ItemClassification.progression,
    "Level Access: LRR - Back To Basics": ItemClassification.progression,
    "Level Access: LRR - Breathless": ItemClassification.progression,
    "Level Access: LRR - Don't Panic": ItemClassification.progression,
    "Level Access: LRR - Driller Night": ItemClassification.progression,
    "Level Access: LRR - Erode Works": ItemClassification.progression,
    "Level Access: LRR - Explosive Action": ItemClassification.progression,
    "Level Access: LRR - Fire And Water": ItemClassification.progression,
    "Level Access: LRR - Frozen Frenzy": ItemClassification.progression,
    "Level Access: LRR - Hot Stuff": ItemClassification.progression,
    "Level Access: LRR - Ice Spy": ItemClassification.progression,
    "Level Access: LRR - It's A Hold Up": ItemClassification.progression,
    "Level Access: LRR - Lake Of Fire": ItemClassification.progression,
    "Level Access: LRR - Lava Laughter": ItemClassification.progression,
    "Level Access: LRR - Oresome": ItemClassification.progression,
    "Level Access: LRR - Rock Hard": ItemClassification.progression,
    "Level Access: LRR - Rocky Horror": ItemClassification.progression,
    "Level Access: LRR - Rubble Trouble": ItemClassification.progression,
    "Level Access: LRR - Run The Gauntlet": ItemClassification.progression,
    "Level Access: LRR - Search And Rescue": ItemClassification.progression,
    "Level Access: LRR - Split Down The Middle": ItemClassification.progression,
    "Level Access: LRR - The Path To Power": ItemClassification.progression,
    "Level Access: LRR - Water Lot Of Fun": ItemClassification.progression,
    "Level Access: LRR - Water Works": ItemClassification.progression,
    
    "Level Access: LRRR - A Breath Of Fresh Air": ItemClassification.progression,
    "Level Access: LRRR - Air Raiders": ItemClassification.progression,
    "Level Access: LRRR - Back To Basics": ItemClassification.progression,
    "Level Access: LRRR - Breathless": ItemClassification.progression,
    "Level Access: LRRR - Don't Panic": ItemClassification.progression,
    "Level Access: LRRR - Driller Night": ItemClassification.progression,
    "Level Access: LRRR - Erode Works": ItemClassification.progression,
    "Level Access: LRRR - Explosive Action": ItemClassification.progression,
    "Level Access: LRRR - Fire And Water": ItemClassification.progression,
    "Level Access: LRRR - Frozen Frenzy": ItemClassification.progression,
    "Level Access: LRRR - Hot Stuff": ItemClassification.progression,
    "Level Access: LRRR - Ice Spy": ItemClassification.progression,
    "Level Access: LRRR - It's A Hold Up": ItemClassification.progression,
    "Level Access: LRRR - Lake Of Fire": ItemClassification.progression,
    "Level Access: LRRR - Lava Laughter": ItemClassification.progression,
    "Level Access: LRRR - Oresome": ItemClassification.progression,
    "Level Access: LRRR - Rock Hard": ItemClassification.progression,
    "Level Access: LRRR - Rocky Horror": ItemClassification.progression,
    "Level Access: LRRR - Rubble Trouble": ItemClassification.progression,
    "Level Access: LRRR - Run The Gauntlet": ItemClassification.progression,
    "Level Access: LRRR - Search And Rescue": ItemClassification.progression,
    "Level Access: LRRR - Split Down The Middle": ItemClassification.progression,
    "Level Access: LRRR - The Path To Power": ItemClassification.progression,
    "Level Access: LRRR - Water Lot Of Fun": ItemClassification.progression,
    "Level Access: LRRR - Water Works": ItemClassification.progression,
    
    "Level Access: LRRC - A Breath Of Fresh Air": ItemClassification.progression,
    "Level Access: LRRC - Air Raiders": ItemClassification.progression,
    "Level Access: LRRC - Back To Basics": ItemClassification.progression,
    "Level Access: LRRC - Breathless": ItemClassification.progression,
    "Level Access: LRRC - Don't Panic": ItemClassification.progression,
    "Level Access: LRRC - Driller Night": ItemClassification.progression,
    "Level Access: LRRC - Erode Works": ItemClassification.progression,
    "Level Access: LRRC - Explosive Action": ItemClassification.progression,
    "Level Access: LRRC - Fire And Water": ItemClassification.progression,
    "Level Access: LRRC - Frozen Frenzy": ItemClassification.progression,
    "Level Access: LRRC - Hot Stuff": ItemClassification.progression,
    "Level Access: LRRC - Ice Spy": ItemClassification.progression,
    "Level Access: LRRC - It's A Hold Up": ItemClassification.progression,
    "Level Access: LRRC - Lake Of Fire": ItemClassification.progression,
    "Level Access: LRRC - Lava Laughter": ItemClassification.progression,
    "Level Access: LRRC - Oresome": ItemClassification.progression,
    "Level Access: LRRC - Rock Hard": ItemClassification.progression,
    "Level Access: LRRC - Rocky Horror": ItemClassification.progression,
    "Level Access: LRRC - Rubble Trouble": ItemClassification.progression,
    "Level Access: LRRC - Run The Gauntlet": ItemClassification.progression,
    "Level Access: LRRC - Search And Rescue": ItemClassification.progression,
    "Level Access: LRRC - Split Down The Middle": ItemClassification.progression,
    "Level Access: LRRC - The Path To Power": ItemClassification.progression,
    "Level Access: LRRC - Water Lot Of Fun": ItemClassification.progression,
    "Level Access: LRRC - Water Works": ItemClassification.progression,
    
    "Level Access: BAZ - A Breath Of Fresh Air": ItemClassification.progression,
    "Level Access: BAZ - Air Raiders": ItemClassification.progression,
    "Level Access: BAZ - Back To Basics": ItemClassification.progression,
    "Level Access: BAZ - Breathless": ItemClassification.progression,
    "Level Access: BAZ - Cold Comfort": ItemClassification.progression,
    "Level Access: BAZ - Don't Panic": ItemClassification.progression,
    "Level Access: BAZ - Down In The Dirt": ItemClassification.progression,
    "Level Access: BAZ - Driller Night": ItemClassification.progression,
    "Level Access: BAZ - Erode Works": ItemClassification.progression,
    "Level Access: BAZ - Explosive Action": ItemClassification.progression,
    "Level Access: BAZ - Fire And Water": ItemClassification.progression,
    "Level Access: BAZ - Frozen Frenzy": ItemClassification.progression,
    "Level Access: BAZ - Hot Stuff": ItemClassification.progression,
    "Level Access: BAZ - Ice Spy": ItemClassification.progression,
    "Level Access: BAZ - It's A Hold Up": ItemClassification.progression,
    "Level Access: BAZ - Lake Of Fire": ItemClassification.progression,
    "Level Access: BAZ - Lava Laughter": ItemClassification.progression,
    "Level Access: BAZ - Mine Over Matter": ItemClassification.progression,
    "Level Access: BAZ - Molten Meltdown": ItemClassification.progression,
    "Level Access: BAZ - Oresome": ItemClassification.progression,
    "Level Access: BAZ - Recruitment": ItemClassification.progression,
    "Level Access: BAZ - Rock Hard": ItemClassification.progression,
    "Level Access: BAZ - Rocky Horror": ItemClassification.progression,
    "Level Access: BAZ - Rubble Trouble": ItemClassification.progression,
    "Level Access: BAZ - Run The Gauntlet": ItemClassification.progression,
    "Level Access: BAZ - Seamless": ItemClassification.progression,
    "Level Access: BAZ - Search And Rescue": ItemClassification.progression,
    "Level Access: BAZ - Slimey Simple": ItemClassification.progression,
    "Level Access: BAZ - Split Down The Middle": ItemClassification.progression,
    "Level Access: BAZ - The Hard Rock Life": ItemClassification.progression,
    "Level Access: BAZ - The Path To Power": ItemClassification.progression,
    "Level Access: BAZ - Water Lot Of Fun": ItemClassification.progression,
    "Level Access: BAZ - Water Works": ItemClassification.progression,
    
    "Building Unlock: Tool Store": ItemClassification.progression,
    "Building Unlock: Teleport Pad": (ItemClassification.progression | ItemClassification.useful), # On SS critical path so same logic as SS
    "Building Unlock: Docks": ItemClassification.progression,
    "Building Unlock: Canteen": ItemClassification.useful,
    "Building Unlock: Power Station": (ItemClassification.progression | ItemClassification.useful), # On SS critical path so same logic as SS
    "Building Unlock: Support Station": (ItemClassification.progression | ItemClassification.useful), # Since SS gates so much, like breathing and every non-dynamite blast option, it's worth marking as a prog-useful item
    "Building Unlock: Upgrade Station": ItemClassification.useful,
    "Building Unlock: Geological Center": ItemClassification.useful,
    "Building Unlock: Ore Refinery": ItemClassification.useful,
    "Building Unlock: Mining Laser": ItemClassification.progression,
    "Building Unlock: Super Teleport": ItemClassification.progression,
    
    "Item Unlock: Electric Fence": ItemClassification.useful,
    "Item Unlock: Dynamite": ItemClassification.progression,
    
    "Vehicle Unlock: Hover Scout": ItemClassification.useful,
    "Vehicle Unlock: Tunnel Scout": ItemClassification.progression,
    "Vehicle Unlock: Small Digger": ItemClassification.progression,
    "Vehicle Unlock: Small Transport Truck": ItemClassification.useful,
    "Vehicle Unlock: Small Mobile Laser Cutter": ItemClassification.progression,
    "Vehicle Unlock: Rapid Rider": ItemClassification.progression,
    "Vehicle Unlock: Cargo Carrier": ItemClassification.progression,
    "Vehicle Unlock: Loader Dozer": ItemClassification.useful,
    "Vehicle Unlock: Granite Grinder": ItemClassification.progression,
    "Vehicle Unlock: Large Mobile Laser Cutter": ItemClassification.progression,
    "Vehicle Unlock: Chrome Crusher": ItemClassification.progression,
    "Vehicle Unlock: Tunnel Transport": ItemClassification.progression,
    
    "Transporter Coordinates": ItemClassification.progression,
    
    "An Energy Crystal Has Been Found!": ItemClassification.filler,
    "Good Work, Cadet!": ItemClassification.filler,
    "A Monster Has Appeared!": ItemClassification.filler,
    "Well Done!": ItemClassification.filler,
    
    "Increased Starting Ore": ItemClassification.filler,    
    "Chief's Favourite Truck": ItemClassification.useful
}

LEVEL_ACCESS_LRR_NOUNLOCK_LIST = [
    "Level Access: LRR - Air Raiders",
    "Level Access: LRR - Don't Panic",
    "Level Access: LRR - Driller Night",
    "Level Access: LRR - It's A Hold Up",
    "Level Access: LRR - Lake Of Fire",
    "Level Access: LRR - Oresome",
    "Level Access: LRR - Rubble Trouble",
    "Level Access: LRR - Run The Gauntlet",
    "Level Access: LRR - Split Down The Middle"
]

LEVEL_ACCESS_LRR_NEEDSUNLOCK_LIST = [
    "Level Access: LRR - A Breath Of Fresh Air",
    "Level Access: LRR - Back To Basics",
    "Level Access: LRR - Breathless",
    "Level Access: LRR - Erode Works",
    "Level Access: LRR - Explosive Action",
    "Level Access: LRR - Fire And Water",
    "Level Access: LRR - Frozen Frenzy",
    "Level Access: LRR - Hot Stuff",
    "Level Access: LRR - Ice Spy",
    "Level Access: LRR - Lava Laughter",
    "Level Access: LRR - Rock Hard",
    "Level Access: LRR - Rocky Horror",
    "Level Access: LRR - Search And Rescue",
    "Level Access: LRR - The Path To Power",
    "Level Access: LRR - Water Lot Of Fun",
    "Level Access: LRR - Water Works"
]

LEVEL_ACCESS_LRR_LIST = LEVEL_ACCESS_LRR_NOUNLOCK_LIST + LEVEL_ACCESS_LRR_NEEDSUNLOCK_LIST

LEVEL_ACCESS_LRRR_NOUNLOCK_LIST = [
    "Level Access: LRRR - Don't Panic",
    "Level Access: LRRR - Driller Night",
    "Level Access: LRRR - Run The Gauntlet"
]

LEVEL_ACCESS_LRRR_NEEDSUNLOCK_LIST = [
    "Level Access: LRRR - A Breath Of Fresh Air",
    "Level Access: LRRR - Air Raiders",
    "Level Access: LRRR - Back To Basics",
    "Level Access: LRRR - Breathless",
    "Level Access: LRRR - Erode Works",
    "Level Access: LRRR - Explosive Action",
    "Level Access: LRRR - Fire And Water",
    "Level Access: LRRR - Frozen Frenzy",
    "Level Access: LRRR - Hot Stuff",
    "Level Access: LRRR - Ice Spy",
    "Level Access: LRRR - It's A Hold Up",
    "Level Access: LRRR - Lake Of Fire",
    "Level Access: LRRR - Lava Laughter",
    "Level Access: LRRR - Oresome",
    "Level Access: LRRR - Rock Hard",
    "Level Access: LRRR - Rocky Horror",
    "Level Access: LRRR - Rubble Trouble",
    "Level Access: LRRR - Search And Rescue",
    "Level Access: LRRR - Split Down The Middle",
    "Level Access: LRRR - The Path To Power",
    "Level Access: LRRR - Water Lot Of Fun",
    "Level Access: LRRR - Water Works"
]

LEVEL_ACCESS_LRRR_LIST = LEVEL_ACCESS_LRRR_NOUNLOCK_LIST + LEVEL_ACCESS_LRRR_NEEDSUNLOCK_LIST

LEVEL_ACCESS_LRRC_NOUNLOCK_LIST = [
    "Level Access: LRRC - Air Raiders",
    "Level Access: LRRC - Don't Panic",
    "Level Access: LRRC - Driller Night",
    "Level Access: LRRC - It's A Hold Up",
    "Level Access: LRRC - Lake Of Fire",
    "Level Access: LRRC - Oresome",
    "Level Access: LRRC - Rubble Trouble",
    "Level Access: LRRC - Run The Gauntlet",
    "Level Access: LRRC - Split Down The Middle"
]

LEVEL_ACCESS_LRRC_NEEDSUNLOCK_LIST = [
    "Level Access: LRRC - A Breath Of Fresh Air",
    "Level Access: LRRC - Back To Basics",
    "Level Access: LRRC - Breathless",
    "Level Access: LRRC - Erode Works",
    "Level Access: LRRC - Explosive Action",
    "Level Access: LRRC - Fire And Water",
    "Level Access: LRRC - Frozen Frenzy",
    "Level Access: LRRC - Hot Stuff",
    "Level Access: LRRC - Ice Spy",
    "Level Access: LRRC - Lava Laughter",
    "Level Access: LRRC - Rock Hard",
    "Level Access: LRRC - Rocky Horror",
    "Level Access: LRRC - Search And Rescue",
    "Level Access: LRRC - The Path To Power",
    "Level Access: LRRC - Water Lot Of Fun",
    "Level Access: LRRC - Water Works"
]

LEVEL_ACCESS_LRRC_LIST = LEVEL_ACCESS_LRRC_NOUNLOCK_LIST + LEVEL_ACCESS_LRRC_NEEDSUNLOCK_LIST

LEVEL_ACCESS_BAZ_NOUNLOCK_LIST = [
    "Level Access: BAZ - Mine Over Matter",
    "Level Access: BAZ - Driller Night",
    "Level Access: BAZ - Split Down The Middle"
]

LEVEL_ACCESS_BAZ_NEEDSUNLOCK_LIST = [
    "Level Access: BAZ - A Breath Of Fresh Air",
    "Level Access: BAZ - Air Raiders",
    "Level Access: BAZ - Back To Basics",
    "Level Access: BAZ - Breathless",
    "Level Access: BAZ - Cold Comfort",
    "Level Access: BAZ - Don't Panic",
    "Level Access: BAZ - Down In The Dirt",
    "Level Access: BAZ - Erode Works",
    "Level Access: BAZ - Explosive Action",
    "Level Access: BAZ - Fire And Water",
    "Level Access: BAZ - Frozen Frenzy",
    "Level Access: BAZ - Hot Stuff",
    "Level Access: BAZ - Ice Spy",
    "Level Access: BAZ - It's A Hold Up",
    "Level Access: BAZ - Lake Of Fire",
    "Level Access: BAZ - Lava Laughter",
    "Level Access: BAZ - Molten Meltdown",
    "Level Access: BAZ - Oresome",
    "Level Access: BAZ - Recruitment",
    "Level Access: BAZ - Rock Hard",
    "Level Access: BAZ - Rocky Horror",
    "Level Access: BAZ - Rubble Trouble",
    "Level Access: BAZ - Run The Gauntlet",
    "Level Access: BAZ - Seamless",
    "Level Access: BAZ - Search And Rescue",
    "Level Access: BAZ - Slimey Simple",
    "Level Access: BAZ - The Hard Rock Life",
    "Level Access: BAZ - The Path To Power",
    "Level Access: BAZ - Water Lot Of Fun",
    "Level Access: BAZ - Water Works"
]

LEVEL_ACCESS_BAZ_LIST = LEVEL_ACCESS_BAZ_NOUNLOCK_LIST + LEVEL_ACCESS_BAZ_NEEDSUNLOCK_LIST

BUILDING_UNLOCK_LIST = [
    "Building Unlock: Tool Store",
    "Building Unlock: Teleport Pad",
    "Building Unlock: Docks",
    "Building Unlock: Canteen",
    "Building Unlock: Power Station",
    "Building Unlock: Support Station",
    "Building Unlock: Upgrade Station",
    "Building Unlock: Geological Center",
    "Building Unlock: Ore Refinery",
    "Building Unlock: Mining Laser",
    "Building Unlock: Super Teleport"
]

ITEM_UNLOCK_LIST = [
    "Item Unlock: Electric Fence",
    "Item Unlock: Dynamite"
]

VEHICLE_UNLOCK_LIST = [
    "Vehicle Unlock: Hover Scout",
    "Vehicle Unlock: Tunnel Scout",
    "Vehicle Unlock: Small Digger",
    "Vehicle Unlock: Small Transport Truck",
    "Vehicle Unlock: Small Mobile Laser Cutter",
    "Vehicle Unlock: Rapid Rider",
    "Vehicle Unlock: Cargo Carrier",
    "Vehicle Unlock: Loader Dozer",
    "Vehicle Unlock: Granite Grinder",
    "Vehicle Unlock: Large Mobile Laser Cutter",
    "Vehicle Unlock: Chrome Crusher",
    "Vehicle Unlock: Tunnel Transport"
]

FILLER_LIST = [
    "An Energy Crystal Has Been Found!",
    "Good Work, Cadet!",
    "A Monster Has Appeared!",
    "Well Done!",
    "Increased Starting Ore"
]

def get_random_filler_item_name(world: ManicMinersWorld) -> str:
    random_filler_item_index = world.random.randint(0,len(FILLER_LIST)-1)
    return FILLER_LIST[random_filler_item_index]
    
def create_item_with_correct_classification(world: ManicMinersWorld, name: str) -> ManicMinersItem:
    classification = DEFAULT_ITEM_CLASSIFICATIONS[name]
    if world.options.campaign_selection_lrrr:
        if name == "Item Unlock: Electric Fence":
            classification = ItemClassification.progression
        if name == "Building Unlock: Geological Center":
            classification = ItemClassification.progression
        if name == "Building Unlock: Ore Refinery":
            classification = ItemClassification.progression
        if name == "Building Unlock: Upgrade Station":
            classification = ItemClassification.progression
        if name == "Building Unlock: Canteen":
            classification = ItemClassification.progression
        if name == "Vehicle Unlock: Hover Scout":
            classification = ItemClassification.progression
        if name == "Vehicle Unlock: Small Transport Truck":
            classification = ItemClassification.progression
    return ManicMinersItem(name, classification, ITEM_NAME_TO_ID[name], world.player)
    
def create_all_items(world: ManicMinersWorld) -> None:
    
    itempool: list[Item] = []
    
    itempool_access = []
    itempool_sphere1_access = []
    itempool_sphere2plus_access = []
 
    initial_access_item_list = []
    
    if world.options.no_duplicate_levels == 0:

        if world.options.campaign_selection_lrr:
            itempool_lrr_sphere1_access = []
            itempool_lrr_sphere2plus_access = []
            for item in LEVEL_ACCESS_LRR_NOUNLOCK_LIST:
                itempool_lrr_sphere1_access.append(world.create_item(item))
            for item in LEVEL_ACCESS_LRR_NEEDSUNLOCK_LIST:
                itempool_lrr_sphere2plus_access.append(world.create_item(item))
            if world.options.buildings_are_items == 0 and world.options.items_are_items == 0 and world.options.vehicles_are_items == 0:
                itempool_lrr_sphere1_access += itempool_lrr_sphere2plus_access
                itempool_lrr_sphere2plus_access.clear()
            
            itempool_sphere1_access += itempool_lrr_sphere1_access
            itempool_sphere2plus_access += itempool_lrr_sphere2plus_access
     
        if world.options.campaign_selection_lrrr:
            itempool_lrrr_sphere1_access = []
            itempool_lrrr_sphere2plus_access = []
            for item in LEVEL_ACCESS_LRRR_NOUNLOCK_LIST:
                itempool_lrrr_sphere1_access.append(world.create_item(item))
            for item in LEVEL_ACCESS_LRRR_NEEDSUNLOCK_LIST:
                itempool_lrrr_sphere2plus_access.append(world.create_item(item))
            if world.options.buildings_are_items == 0 and world.options.items_are_items == 0 and world.options.vehicles_are_items == 0:
                itempool_lrrr_sphere1_access += itempool_lrrr_sphere2plus_access
                itempool_lrrr_sphere2plus_access.clear()
            
            itempool_sphere1_access += itempool_lrrr_sphere1_access
            itempool_sphere2plus_access += itempool_lrrr_sphere2plus_access
     
        if world.options.campaign_selection_lrrc:
            itempool_lrrc_sphere1_access = []
            itempool_lrrc_sphere2plus_access = []
            for item in LEVEL_ACCESS_LRRC_NOUNLOCK_LIST:
                itempool_lrrc_sphere1_access.append(world.create_item(item))
            for item in LEVEL_ACCESS_LRRC_NEEDSUNLOCK_LIST:
                itempool_lrrc_sphere2plus_access.append(world.create_item(item))
            if world.options.buildings_are_items == 0 and world.options.items_are_items == 0 and world.options.vehicles_are_items == 0:
                itempool_lrrc_sphere1_access += itempool_lrrc_sphere2plus_access
                itempool_lrrc_sphere2plus_access.clear()
            
            itempool_sphere1_access += itempool_lrrc_sphere1_access
            itempool_sphere2plus_access += itempool_lrrc_sphere2plus_access
     
        # if world.options.campaign_selection_baz:
            # itempool_baz_sphere1_access = []
            # itempool_baz_sphere2plus_access = []
            # for item in LEVEL_ACCESS_BAZ_NOUNLOCK_LIST:
                # itempool_baz_sphere1_access.append(world.create_item(item))
            # for item in LEVEL_ACCESS_BAZ_NEEDSUNLOCK_LIST:
                # itempool_baz_sphere2plus_access.append(world.create_item(item))
            # if world.options.buildings_are_items == 0 and world.options.items_are_items == 0 and world.options.vehicles_are_items == 0:
                # itempool_baz_sphere1_access += itempool_baz_sphere2plus_access
                # itempool_baz_sphere2plus_access.clear()
            
            # itempool_sphere1_access += itempool_baz_sphere1_access
            # itempool_sphere2plus_access += itempool_baz_sphere2plus_access
        
        initial_access_item_index = world.random.randint(0,len(itempool_sphere1_access)-1)
        initial_access_item_list.append(itempool_sphere1_access[initial_access_item_index])
        itempool_sphere1_access.pop(initial_access_item_index)
        
        itempool_access = itempool_sphere1_access + itempool_sphere2plus_access
        
        for i in range(world.options.available_levels_at_start-1):
            initial_access_item_index = world.random.randint(0,len(itempool_access)-1)
            initial_access_item_list.append(itempool_access[initial_access_item_index])
            itempool_access.pop(initial_access_item_index)
    
    else:

        if world.options.level_selection_lrr_abreathoffreshair:
            itempool_access.append(world.create_item("Level Access: LRR - A Breath Of Fresh Air"))
        if world.options.level_selection_lrr_airraiders:
            itempool_access.append(world.create_item("Level Access: LRR - Air Raiders"))
        if world.options.level_selection_lrr_backtobasics:
            itempool_access.append(world.create_item("Level Access: LRR - Back To Basics"))
        if world.options.level_selection_lrr_breathless:
            itempool_access.append(world.create_item("Level Access: LRR - Breathless"))
        if world.options.level_selection_lrr_dontpanic:
            itempool_access.append(world.create_item("Level Access: LRR - Don't Panic"))
        if world.options.level_selection_lrr_drillernight:
            initial_access_item_list.append(world.create_item("Level Access: LRR - Driller Night"))
        if world.options.level_selection_lrr_erodeworks:
            itempool_access.append(world.create_item("Level Access: LRR - Erode Works"))
        if world.options.level_selection_lrr_explosiveaction:
            itempool_access.append(world.create_item("Level Access: LRR - Explosive Action"))
        if world.options.level_selection_lrr_fireandwater:
            itempool_access.append(world.create_item("Level Access: LRR - Fire And Water"))
        if world.options.level_selection_lrr_frozenfrenzy:
            itempool_access.append(world.create_item("Level Access: LRR - Frozen Frenzy"))
        if world.options.level_selection_lrr_hotstuff:
            itempool_access.append(world.create_item("Level Access: LRR - Hot Stuff"))
        if world.options.level_selection_lrr_icespy:
            itempool_access.append(world.create_item("Level Access: LRR - Ice Spy"))
        if world.options.level_selection_lrr_itsaholdup:
            itempool_access.append(world.create_item("Level Access: LRR - It's A Hold Up"))
        if world.options.level_selection_lrr_lakeoffire:
            itempool_access.append(world.create_item("Level Access: LRR - Lake Of Fire"))
        if world.options.level_selection_lrr_lavalaughter:
            itempool_access.append(world.create_item("Level Access: LRR - Lava Laughter"))
        if world.options.level_selection_lrr_oresome:
            itempool_access.append(world.create_item("Level Access: LRR - Oresome"))
        if world.options.level_selection_lrr_rockhard:
            itempool_access.append(world.create_item("Level Access: LRR - Rock Hard"))
        if world.options.level_selection_lrr_rockyhorror and world.options.boss_level_lrr_rockyhorror == 0:
            itempool_access.append(world.create_item("Level Access: LRR - Rocky Horror"))
        if world.options.level_selection_lrr_rubbletrouble:
            itempool_access.append(world.create_item("Level Access: LRR - Rubble Trouble"))
        if world.options.level_selection_lrr_runthegauntlet:
            itempool_access.append(world.create_item("Level Access: LRR - Run The Gauntlet"))
        if world.options.level_selection_lrr_searchandrescue:
            itempool_access.append(world.create_item("Level Access: LRR - Search And Rescue"))
        if world.options.level_selection_lrr_splitdownthemiddle:
            itempool_access.append(world.create_item("Level Access: LRR - Split Down The Middle"))
        if world.options.level_selection_lrr_thepathtopower:
            itempool_access.append(world.create_item("Level Access: LRR - The Path To Power"))
        if world.options.level_selection_lrr_waterlotoffun:
            itempool_access.append(world.create_item("Level Access: LRR - Water Lot Of Fun"))
        if world.options.level_selection_lrr_waterworks:
            itempool_access.append(world.create_item("Level Access: LRR - Water Works"))

        if world.options.level_selection_lrrr_abreathoffreshair:
            itempool_access.append(world.create_item("Level Access: LRRR - A Breath Of Fresh Air"))
        if world.options.level_selection_lrrr_airraiders:
            itempool_access.append(world.create_item("Level Access: LRRR - Air Raiders"))
        if world.options.level_selection_lrrr_backtobasics:
            itempool_access.append(world.create_item("Level Access: LRRR - Back To Basics"))
        if world.options.level_selection_lrrr_breathless:
            itempool_access.append(world.create_item("Level Access: LRRR - Breathless"))
        if world.options.level_selection_lrrr_dontpanic:
            itempool_access.append(world.create_item("Level Access: LRRR - Don't Panic"))
        if world.options.level_selection_lrrr_drillernight:
            initial_access_item_list.append(world.create_item("Level Access: LRRR - Driller Night"))
        if world.options.level_selection_lrrr_erodeworks:
            itempool_access.append(world.create_item("Level Access: LRRR - Erode Works"))
        if world.options.level_selection_lrrr_explosiveaction:
            itempool_access.append(world.create_item("Level Access: LRRR - Explosive Action"))
        if world.options.level_selection_lrrr_fireandwater:
            itempool_access.append(world.create_item("Level Access: LRRR - Fire And Water"))
        if world.options.level_selection_lrrr_frozenfrenzy:
            itempool_access.append(world.create_item("Level Access: LRRR - Frozen Frenzy"))
        if world.options.level_selection_lrrr_hotstuff:
            itempool_access.append(world.create_item("Level Access: LRRR - Hot Stuff"))
        if world.options.level_selection_lrrr_icespy:
            itempool_access.append(world.create_item("Level Access: LRRR - Ice Spy"))
        if world.options.level_selection_lrrr_itsaholdup:
            itempool_access.append(world.create_item("Level Access: LRRR - It's A Hold Up"))
        if world.options.level_selection_lrrr_lakeoffire:
            itempool_access.append(world.create_item("Level Access: LRRR - Lake Of Fire"))
        if world.options.level_selection_lrrr_lavalaughter:
            itempool_access.append(world.create_item("Level Access: LRRR - Lava Laughter"))
        if world.options.level_selection_lrrr_oresome:
            itempool_access.append(world.create_item("Level Access: LRRR - Oresome"))
        if world.options.level_selection_lrrr_rockhard:
            itempool_access.append(world.create_item("Level Access: LRRR - Rock Hard"))
        if world.options.level_selection_lrrr_rockyhorror and world.options.boss_level_lrrr_rockyhorror == 0:
            itempool_access.append(world.create_item("Level Access: LRRR - Rocky Horror"))
        if world.options.level_selection_lrrr_rubbletrouble:
            itempool_access.append(world.create_item("Level Access: LRRR - Rubble Trouble"))
        if world.options.level_selection_lrrr_runthegauntlet:
            itempool_access.append(world.create_item("Level Access: LRRR - Run The Gauntlet"))
        if world.options.level_selection_lrrr_searchandrescue:
            itempool_access.append(world.create_item("Level Access: LRRR - Search And Rescue"))
        if world.options.level_selection_lrrr_splitdownthemiddle:
            itempool_access.append(world.create_item("Level Access: LRRR - Split Down The Middle"))
        if world.options.level_selection_lrrr_thepathtopower:
            itempool_access.append(world.create_item("Level Access: LRRR - The Path To Power"))
        if world.options.level_selection_lrrr_waterlotoffun:
            itempool_access.append(world.create_item("Level Access: LRRR - Water Lot Of Fun"))
        if world.options.level_selection_lrrr_waterworks:
            itempool_access.append(world.create_item("Level Access: LRRR - Water Works"))

        if world.options.level_selection_lrrc_abreathoffreshair:
            itempool_access.append(world.create_item("Level Access: LRRC - A Breath Of Fresh Air"))
        if world.options.level_selection_lrrc_airraiders:
            itempool_access.append(world.create_item("Level Access: LRRC - Air Raiders"))
        if world.options.level_selection_lrrc_backtobasics:
            itempool_access.append(world.create_item("Level Access: LRRC - Back To Basics"))
        if world.options.level_selection_lrrc_breathless:
            itempool_access.append(world.create_item("Level Access: LRRC - Breathless"))
        if world.options.level_selection_lrrc_dontpanic:
            itempool_access.append(world.create_item("Level Access: LRRC - Don't Panic"))
        if world.options.level_selection_lrrc_drillernight:
            initial_access_item_list.append(world.create_item("Level Access: LRRC - Driller Night"))
        if world.options.level_selection_lrrc_erodeworks:
            itempool_access.append(world.create_item("Level Access: LRRC - Erode Works"))
        if world.options.level_selection_lrrc_explosiveaction:
            itempool_access.append(world.create_item("Level Access: LRRC - Explosive Action"))
        if world.options.level_selection_lrrc_fireandwater:
            itempool_access.append(world.create_item("Level Access: LRRC - Fire And Water"))
        if world.options.level_selection_lrrc_frozenfrenzy:
            itempool_access.append(world.create_item("Level Access: LRRC - Frozen Frenzy"))
        if world.options.level_selection_lrrc_hotstuff:
            itempool_access.append(world.create_item("Level Access: LRRC - Hot Stuff"))
        if world.options.level_selection_lrrc_icespy:
            itempool_access.append(world.create_item("Level Access: LRRC - Ice Spy"))
        if world.options.level_selection_lrrc_itsaholdup:
            itempool_access.append(world.create_item("Level Access: LRRC - It's A Hold Up"))
        if world.options.level_selection_lrrc_lakeoffire:
            itempool_access.append(world.create_item("Level Access: LRRC - Lake Of Fire"))
        if world.options.level_selection_lrrc_lavalaughter:
            itempool_access.append(world.create_item("Level Access: LRRC - Lava Laughter"))
        if world.options.level_selection_lrrc_oresome:
            itempool_access.append(world.create_item("Level Access: LRRC - Oresome"))
        if world.options.level_selection_lrrc_rockhard:
            itempool_access.append(world.create_item("Level Access: LRRC - Rock Hard"))
        if world.options.level_selection_lrrc_rockyhorror and world.options.boss_level_lrrc_rockyhorror == 0:
            itempool_access.append(world.create_item("Level Access: LRRC - Rocky Horror"))
        if world.options.level_selection_lrrc_rubbletrouble:
            itempool_access.append(world.create_item("Level Access: LRRC - Rubble Trouble"))
        if world.options.level_selection_lrrc_runthegauntlet:
            itempool_access.append(world.create_item("Level Access: LRRC - Run The Gauntlet"))
        if world.options.level_selection_lrrc_searchandrescue:
            itempool_access.append(world.create_item("Level Access: LRRC - Search And Rescue"))
        if world.options.level_selection_lrrc_splitdownthemiddle:
            itempool_access.append(world.create_item("Level Access: LRRC - Split Down The Middle"))
        if world.options.level_selection_lrrc_thepathtopower:
            itempool_access.append(world.create_item("Level Access: LRRC - The Path To Power"))
        if world.options.level_selection_lrrc_waterlotoffun:
            itempool_access.append(world.create_item("Level Access: LRRC - Water Lot Of Fun"))
        if world.options.level_selection_lrrc_waterworks:
            itempool_access.append(world.create_item("Level Access: LRRC - Water Works"))
        
        for i in range(world.options.available_levels_at_start-1):
            initial_access_item_index = world.random.randint(0,len(itempool_access)-1)
            initial_access_item_list.append(itempool_access[initial_access_item_index])
            itempool_access.pop(initial_access_item_index)        
    
    itempool += itempool_access   
    
    itempool_buildings = []
    for item in BUILDING_UNLOCK_LIST:
        itempool_buildings.append(world.create_item(item))
    
    itempool_items = []
    for item in ITEM_UNLOCK_LIST:
        itempool_items.append(world.create_item(item))

    itempool_vehicles = []
    for item in VEHICLE_UNLOCK_LIST:
        itempool_vehicles.append(world.create_item(item))
    
    for item in initial_access_item_list:
        world.push_precollected(item)
    
    if world.options.buildings_are_items:
        itempool += itempool_buildings
    else:
        for item in itempool_buildings:
            world.push_precollected(item)

    if world.options.items_are_items:
        itempool += itempool_items
    else:
        for item in itempool_items:
            world.push_precollected(item)

    if world.options.vehicles_are_items:
        itempool += itempool_vehicles
    else:
        for item in itempool_vehicles:
            world.push_precollected(item)
            
    if world.options.bonus_truck:
        itempool.append(world.create_item("Chief's Favourite Truck"))
    
    if world.options.victory_condition == 3 and world.options.locked_coordinates == 0:
        level_count = 0
        if world.options.campaign_selection_lrr:
            level_count += 25
        if world.options.campaign_selection_lrrr:
            level_count += 25
        if world.options.campaign_selection_lrrc:
            level_count += 25
        if world.options.no_duplicate_levels:
            level_count = 25
        for i in range(level_count):
            itempool.append(world.create_item("Transporter Coordinates"))

    number_of_items = len(itempool)
    number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))
    needed_number_of_filler_items = number_of_unfilled_locations - number_of_items
    itempool += [world.create_filler() for _ in range(needed_number_of_filler_items)]
    
    if world.options.boss_level_lrr_rockyhorror:
        world.push_precollected(world.create_item("Level Access: LRR - Rocky Horror"))
    if world.options.boss_level_lrrr_rockyhorror:
        world.push_precollected(world.create_item("Level Access: LRRR - Rocky Horror"))
    if world.options.boss_level_lrrc_rockyhorror:
        world.push_precollected(world.create_item("Level Access: LRRC - Rocky Horror"))
    
    world.multiworld.itempool += itempool

def copy_level_into_archipelago(root_dir, arch_level_dir, item_id, all_items, options):
    main_level_dir = root_dir + "\\ManicMiners\\Levels"
    arch_level_dir = arch_level_dir + "\\Levels\\Archipelago"
    match item_id:
        case 1:
            source = "\\LRR\\abreathoffreshair.dat"
            target = "\\LRR - A Breath Of Fresh Air.dat"
        case 2:
            source = "\\LRR\\airraiders.dat"
            target = "\\LRR - Air Raiders.dat"
        case 3:
            source = "\\LRR\\backtobasics.dat"
            target = "\\LRR - Back To Basics.dat"
        case 4:
            source = "\\LRR\\breathless.dat"
            target = "\\LRR - Breathless.dat"
        case 5:
            source = "\\LRR\\dontpanic.dat"
            target = "\\LRR - Don't Panic.dat"
        case 6:
            source = "\\LRR\\drillernight.dat"
            target = "\\LRR - Driller Night.dat"
        case 7:
            source = "\\LRR\\erodeworks.dat"
            target = "\\LRR - Erode Works.dat"
        case 8:
            source = "\\LRR\\explosiveaction.dat"
            target = "\\LRR - Explosive Action.dat"
        case 9:
            source = "\\LRR\\fireandwater.dat"
            target = "\\LRR - Fire And Water.dat"
        case 10:
            source = "\\LRR\\frozenfrenzy.dat"
            target = "\\LRR - Frozen Frenzy.dat"
        case 11:
            source = "\\LRR\\hotstuff.dat"
            target = "\\LRR - Hot Stuff.dat"
        case 12:
            source = "\\LRR\\icespy.dat"
            target = "\\LRR - Ice Spy.dat"
        case 13:
            source = "\\LRR\\itsaholdup.dat"
            target = "\\LRR - It's A Hold Up.dat"
        case 14:
            source = "\\LRR\\lakeoffire.dat"
            target = "\\LRR - Lake Of Fire.dat"
        case 15:
            source = "\\LRR\\lavalaughter.dat"
            target = "\\LRR - Lava Laughter.dat"
        case 16:
            source = "\\LRR\\oresome.dat"
            target = "\\LRR - Oresome.dat"
        case 17:
            source = "\\LRR\\rockhard.dat"
            target = "\\LRR - Rock Hard.dat"
        case 18:
            if options["boss_level_lrr_rockyhorror"] == 1:
                if all_items.count(874) < options["target_level_count"]:
                    return False
            source = "\\LRR\\rockyhorror.dat"
            target = "\\LRR - Rocky Horror.dat"
        case 19:
            source = "\\LRR\\rubbletrouble.dat"
            target = "\\LRR - Rubble Trouble.dat"
        case 20:
            source = "\\LRR\\runthegauntlet.dat"
            target = "\\LRR - Run The Gauntlet.dat"
        case 21:
            source = "\\LRR\\searchandrescue.dat"
            target = "\\LRR - Search And Rescue.dat"
        case 22:
            source = "\\LRR\\splitdownthemiddle.dat"
            target = "\\LRR - Split Down The Middle.dat"
        case 23:
            source = "\\LRR\\thepathtopower.dat"
            target = "\\LRR - The Path To Power.dat"
        case 24:
            source = "\\LRR\\waterlotoffun.dat"
            target = "\\LRR - Water Lot Of Fun.dat"
        case 25:
            source = "\\LRR\\waterworks.dat"
            target = "\\LRR - Water Works.dat"
        case 1001:
            source = "\\LRRR\\abreathoffreshair.dat"
            target = "\\LRRR - A Breath Of Fresh Air.dat"
        case 1002:
            source = "\\LRRR\\airraiders.dat"
            target = "\\LRRR - Air Raiders.dat"
        case 1003:
            source = "\\LRRR\\backtobasics.dat"
            target = "\\LRRR - Back To Basics.dat"
        case 1004:
            source = "\\LRRR\\breathless.dat"
            target = "\\LRRR - Breathless.dat"
        case 1005:
            source = "\\LRRR\\dontpanic.dat"
            target = "\\LRRR - Don't Panic.dat"
        case 1006:
            source = "\\LRRR\\drillernight.dat"
            target = "\\LRRR - Driller Night.dat"
        case 1007:
            source = "\\LRRR\\erodeworks.dat"
            target = "\\LRRR - Erode Works.dat"
        case 1008:
            source = "\\LRRR\\explosiveaction.dat"
            target = "\\LRRR - Explosive Action.dat"
        case 1009:
            source = "\\LRRR\\fireandwater.dat"
            target = "\\LRRR - Fire And Water.dat"
        case 1010:
            source = "\\LRRR\\frozenfrenzy.dat"
            target = "\\LRRR - Frozen Frenzy.dat"
        case 1011:
            source = "\\LRRR\\hotstuff.dat"
            target = "\\LRRR - Hot Stuff.dat"
        case 1012:
            source = "\\LRRR\\icespy.dat"
            target = "\\LRRR - Ice Spy.dat"
        case 1013:
            source = "\\LRRR\\itsaholdup.dat"
            target = "\\LRRR - It's A Hold Up.dat"
        case 1014:
            source = "\\LRRR\\lakeoffire.dat"
            target = "\\LRRR - Lake Of Fire.dat"
        case 1015:
            source = "\\LRRR\\lavalaughter.dat"
            target = "\\LRRR - Lava Laughter.dat"
        case 1016:
            source = "\\LRRR\\oresome.dat"
            target = "\\LRRR - Oresome.dat"
        case 1017:
            source = "\\LRRR\\rockhard.dat"
            target = "\\LRRR - Rock Hard.dat"
        case 1018:
            if options["boss_level_lrrr_rockyhorror"] == 1:
                if all_items.count(874) < options["target_level_count"]:
                    return False
            source = "\\LRRR\\rockyhorror.dat"
            target = "\\LRRR - Rocky Horror.dat"
        case 1019:
            source = "\\LRRR\\rubbletrouble.dat"
            target = "\\LRRR - Rubble Trouble.dat"
        case 1020:
            source = "\\LRRR\\runthegauntlet.dat"
            target = "\\LRRR - Run The Gauntlet.dat"
        case 1021:
            source = "\\LRRR\\searchandrescue.dat"
            target = "\\LRRR - Search And Rescue.dat"
        case 1022:
            source = "\\LRRR\\splitdownthemiddle.dat"
            target = "\\LRRR - Split Down The Middle.dat"
        case 1023:
            source = "\\LRRR\\thepathtopower.dat"
            target = "\\LRRR - The Path To Power.dat"
        case 1024:
            source = "\\LRRR\\waterlotoffun.dat"
            target = "\\LRRR - Water Lot Of Fun.dat"
        case 1025:
            source = "\\LRRR\\waterworks.dat"
            target = "\\LRRR - Water Works.dat"
        case 2001:
            source = "\\LRRC\\abreathoffreshair.dat"
            target = "\\LRRC - A Breath Of Fresh Air.dat"
        case 2002:
            source = "\\LRRC\\airraiders.dat"
            target = "\\LRRC - Air Raiders.dat"
        case 2003:
            source = "\\LRRC\\backtobasics.dat"
            target = "\\LRRC - Back To Basics.dat"
        case 2004:
            source = "\\LRRC\\breathless.dat"
            target = "\\LRRC - Breathless.dat"
        case 2005:
            source = "\\LRRC\\dontpanic.dat"
            target = "\\LRRC - Don't Panic.dat"
        case 2006:
            source = "\\LRRC\\drillernight.dat"
            target = "\\LRRC - Driller Night.dat"
        case 2007:
            source = "\\LRRC\\erodeworks.dat"
            target = "\\LRRC - Erode Works.dat"
        case 2008:
            source = "\\LRRC\\explosiveaction.dat"
            target = "\\LRRC - Explosive Action.dat"
        case 2009:
            source = "\\LRRC\\fireandwater.dat"
            target = "\\LRRC - Fire And Water.dat"
        case 2010:
            source = "\\LRRC\\frozenfrenzy.dat"
            target = "\\LRRC - Frozen Frenzy.dat"
        case 2011:
            source = "\\LRRC\\hotstuff.dat"
            target = "\\LRRC - Hot Stuff.dat"
        case 2012:
            source = "\\LRRC\\icespy.dat"
            target = "\\LRRC - Ice Spy.dat"
        case 2013:
            source = "\\LRRC\\itsaholdup.dat"
            target = "\\LRRC - It's A Hold Up.dat"
        case 2014:
            source = "\\LRRC\\lakeoffire.dat"
            target = "\\LRRC - Lake Of Fire.dat"
        case 2015:
            source = "\\LRRC\\lavalaughter.dat"
            target = "\\LRRC - Lava Laughter.dat"
        case 2016:
            source = "\\LRRC\\oresome.dat"
            target = "\\LRRC - Oresome.dat"
        case 2017:
            source = "\\LRRC\\rockhard.dat"
            target = "\\LRRC - Rock Hard.dat"
        case 2018:
            if options["boss_level_lrrc_rockyhorror"] == 1:
                if all_items.count(874) < options["target_level_count"]:
                    return False
            source = "\\LRRC\\rockyhorror.dat"
            target = "\\LRRC - Rocky Horror.dat"
        case 2019:
            source = "\\LRRC\\rubbletrouble.dat"
            target = "\\LRRC - Rubble Trouble.dat"
        case 2020:
            source = "\\LRRC\\runthegauntlet.dat"
            target = "\\LRRC - Run The Gauntlet.dat"
        case 2021:
            source = "\\LRRC\\searchandrescue.dat"
            target = "\\LRRC - Search And Rescue.dat"
        case 2022:
            source = "\\LRRC\\splitdownthemiddle.dat"
            target = "\\LRRC - Split Down The Middle.dat"
        case 2023:
            source = "\\LRRC\\thepathtopower.dat"
            target = "\\LRRC - The Path To Power.dat"
        case 2024:
            source = "\\LRRC\\waterlotoffun.dat"
            target = "\\LRRC - Water Lot Of Fun.dat"
        case 2025:
            source = "\\LRRC\\waterworks.dat"
            target = "\\LRRC - Water Works.dat"
        case 3001:
            source = "\\BAZ\\abreathoffreshair.dat"
            target = "\\BAZ - A Breath Of Fresh Air.dat"
        case 3002:
            source = "\\BAZ\\airraiders.dat"
            target = "\\BAZ - Air Raiders.dat"
        case 3003:
            source = "\\BAZ\\backtobasics.dat"
            target = "\\BAZ - Back To Basics.dat"
        case 3004:
            source = "\\BAZ\\breathless.dat"
            target = "\\BAZ - Breathless.dat"
        case 3005:
            source = "\\BAZ\\coldcomfort.dat"
            target = "\\BAZ - Cold Comfort.dat"
        case 3006:
            source = "\\BAZ\\dontpanic.dat"
            target = "\\BAZ - Don't Panic.dat"
        case 3007:
            source = "\\BAZ\\downinthedirt.dat"
            target = "\\BAZ - Down In The Dirt.dat"
        case 3008:
            source = "\\BAZ\\drillernight.dat"
            target = "\\BAZ - Driller Night.dat"
        case 3009:
            source = "\\BAZ\\erodeworks.dat"
            target = "\\BAZ - Erode Works.dat"
        case 3010:
            source = "\\BAZ\\explosiveaction.dat"
            target = "\\BAZ - Explosive Action.dat"
        case 3011:
            source = "\\BAZ\\fireandwater.dat"
            target = "\\BAZ - Fire And Water.dat"
        case 3012:
            source = "\\BAZ\\frozenfrenzy.dat"
            target = "\\BAZ - Frozen Frenzy.dat"
        case 3013:
            source = "\\BAZ\\hotstuff.dat"
            target = "\\BAZ - Hot Stuff.dat"
        case 3014:
            source = "\\BAZ\\icespy.dat"
            target = "\\BAZ - Ice Spy.dat"
        case 3015:
            source = "\\BAZ\\itsaholdup.dat"
            target = "\\BAZ - It's A Hold Up.dat"
        case 3016:
            source = "\\BAZ\\lakeoffire.dat"
            target = "\\BAZ - Lake Of Fire.dat"
        case 3017:
            source = "\\BAZ\\lavalaughter.dat"
            target = "\\BAZ - Lava Laughter.dat"
        case 3018:
            source = "\\BAZ\\mineovermatter.dat"
            target = "\\BAZ - Mine Over Matter.dat"
        case 3019:
            source = "\\BAZ\\moltenmeltdown.dat"
            target = "\\BAZ - Molten Meltdown.dat"
        case 3020:
            source = "\\BAZ\\oresome.dat"
            target = "\\BAZ - Oresome.dat"
        case 3021:
            source = "\\BAZ\\recruitment.dat"
            target = "\\BAZ - Recruitment.dat"
        case 3022:
            source = "\\BAZ\\rockhard.dat"
            target = "\\BAZ - Rock Hard.dat"
        case 3023:
            source = "\\BAZ\\rockyhorror.dat"
            target = "\\BAZ - Rocky Horror.dat"
        case 3024:
            source = "\\BAZ\\rubbletrouble.dat"
            target = "\\BAZ - Rubble Trouble.dat"
        case 3025:
            source = "\\BAZ\\runthegauntlet.dat"
            target = "\\BAZ - Run The Gauntlet.dat"
        case 3026:
            source = "\\BAZ\\seamless.dat"
            target = "\\BAZ - Seamless.dat"
        case 3027:
            source = "\\BAZ\\searchandrescue.dat"
            target = "\\BAZ - Search And Rescue.dat"
        case 3028:
            source = "\\BAZ\\slimeysimple.dat"
            target = "\\BAZ - Slimey Simple.dat"
        case 3029:
            source = "\\BAZ\\splitdownthemiddle.dat"
            target = "\\BAZ - Split Down The Middle.dat"
        case 3030:
            source = "\\BAZ\\thehardrocklife.dat"
            target = "\\BAZ - The Hard Rock Life.dat"
        case 3031:
            source = "\\BAZ\\thepathtopower.dat"
            target = "\\BAZ - The Path To Power.dat"
        case 3032:
            source = "\\BAZ\\waterlotoffun.dat"
            target = "\\BAZ - Water Lot Of Fun.dat"
        case 3033:
            source = "\\BAZ\\waterworks.dat"
            target = "\\BAZ - Water Works.dat"
        case _:
            return False
    if platform.system() != "Windows":
        main_level_dir = main_level_dir.replace("\\","/")
        arch_level_dir = arch_level_dir.replace("\\","/")
        source = source.replace("\\","/")
        target = target.replace("\\","/")
    source_path = pathlib.Path(main_level_dir + source)
    target_path = pathlib.Path(arch_level_dir + target)
    shutil.copy(source_path, target_path)
    update_disabled_unlocks(target_path, all_items)
    return True

def update_disabled_unlocks(filepath, all_items):
    with open(filepath,'r') as file:
        original_file_contents = file.read()
        file.close()

    archipelago_index = original_file_contents.find("# Begin Archipelago")
    if (archipelago_index == -1):
        archipelago_index = original_file_contents.rfind("}")

    original_file_beginning = original_file_contents[:archipelago_index]

    archipelago_section = "# Begin Archipelago Disablers\n# Everything after this point in the file will be overwritten by Archipelago!\n\ninit::;\n"
    
    if 899 not in all_items: 
        archipelago_section = archipelago_section + "disable:ToolStore;\n"
    if 898 not in all_items:
        archipelago_section = archipelago_section + "disable:TeleportPad;\n"
    if 897 not in all_items:
        archipelago_section = archipelago_section + "disable:Docks;\n"
    if 896 not in all_items:
        archipelago_section = archipelago_section + "disable:Canteen;\n"
    if 895 not in all_items:
        archipelago_section = archipelago_section + "disable:PowerStation;\n"
    if 894 not in all_items:
        archipelago_section = archipelago_section + "disable:SupportStation;\n"
    if 893 not in all_items:
        archipelago_section = archipelago_section + "disable:UpgradeStation;\n"
    if 892 not in all_items:
        archipelago_section = archipelago_section + "disable:GeologicalCenter;\n"
    if 891 not in all_items:
        archipelago_section = archipelago_section + "disable:OreRefinery;\n"
    if 890 not in all_items:
        archipelago_section = archipelago_section + "disable:MiningLaser;\n"
    if 889 not in all_items:
        archipelago_section = archipelago_section + "disable:SuperTeleport;\n"

    if 888 not in all_items:
        archipelago_section = archipelago_section + "disable:ElectricFence;\n"
    if 887 not in all_items:
        archipelago_section = archipelago_section + "disable:Dynamite;\n"

    if 886 not in all_items:
        archipelago_section = archipelago_section + "disable:HoverScout;\n"
    if 885 not in all_items:
        archipelago_section = archipelago_section + "disable:TunnelScout;\n"
    if 884 not in all_items:
        archipelago_section = archipelago_section + "disable:SmallDigger;\n"
    if 883 not in all_items:
        archipelago_section = archipelago_section + "disable:SmallTransportTruck;\n"
    if 882 not in all_items:
        archipelago_section = archipelago_section + "disable:SMLC;\n"
    if 881 not in all_items:
        archipelago_section = archipelago_section + "disable:RapidRider;\n"
    if 880 not in all_items:
        archipelago_section = archipelago_section + "disable:CargoCarrier;\n"
    if 879 not in all_items:
        archipelago_section = archipelago_section + "disable:LoaderDozer;\n"
    if 878 not in all_items:
        archipelago_section = archipelago_section + "disable:GraniteGrinder;\n"
    if 877 not in all_items:
        archipelago_section = archipelago_section + "disable:LMLC;\n"
    if 876 not in all_items:
        archipelago_section = archipelago_section + "disable:ChromeCrusher;\n"
    if 875 not in all_items:
        archipelago_section = archipelago_section + "disable:TunnelTransport;\n"
    
    bonus_ore = all_items.count(950)
    archipelago_section = archipelago_section + "ore+=" + str(bonus_ore) + ";\n"

    archipelago_section = archipelago_section + "\n}\n"

    new_file_contents = original_file_beginning + archipelago_section
    
    if 949 in all_items:
        buildings_section_start = new_file_contents.find("buildings{")
        buildings_section_end = new_file_contents.find("}",buildings_section_start)+1
        buildings_section = new_file_contents[buildings_section_start:buildings_section_end]

        toolstore_section_start = buildings_section.find("BuildingToolStore_C")
        toolstore_section_end = buildings_section.find("Building",toolstore_section_start+1)-1
        if toolstore_section_end == 0:
            toolstore_section_end = buildings_section.find("}")
        toolstore_section = buildings_section[toolstore_section_start:toolstore_section_end]

        toolstore_translation = toolstore_section[toolstore_section.find("Translation:"):toolstore_section.find("Rotation:")]

        vehicle_spawn_line = "\nVehicleSmallTransportTruck_C," + toolstore_translation + "Rotation: P=0.000000 Y=0.000000 R=0.000000 Scale X=1.000 Y=1.000 Z=1.000,Essential=true"
       
        vehicles_section_start = new_file_contents.find("vehicles{")+9

        temp = new_file_contents[:vehicles_section_start] + vehicle_spawn_line + new_file_contents[vehicles_section_start:]
        new_file_contents = temp
    
    with open(filepath,'w') as file:
        file.write(new_file_contents)
        file.close()