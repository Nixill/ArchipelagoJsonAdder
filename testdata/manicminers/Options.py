from dataclasses import dataclass

from Options import PerGameCommonOptions, OptionGroup, Toggle, DefaultOnToggle, Choice, Range, Visibility

class VictoryCondition(Choice):
    """
    What the victory condition for the overall game is. 
    Clear X Levels: You must clear X total levels to goal the game.
    Beat X Par Times: You must beat the target time on X total levels.
    Beat X Crystal Targets: You must beat the crystal target on X total levels.
    Coordinate Hunt: You must find X "Transporter Coordinates" items to gain access to Rocky Horror, which you must then clear to win the game. 
    """
    
    display_name = "Victory Condition"
    
    option_clear_x_levels = 0
    option_beat_x_par_times = 1
    option_beat_x_crystal_targets = 2
    option_coordinate_hunt = 3
    
    default = option_clear_x_levels

class LockedCoordinates(DefaultOnToggle):
    """
    Only relevant if Victory Condition is set to "Coordinate Hunt". 
    If true, then clearing each level unlocks one "Transporter Coordinates" item. 
    If false, then the "Transporter Coordinates" can be anywhere in the multiworld. An extra location is still added to each level.
    """
    
    display_name = "Locked Coordinate Locations"

class TargetLevelCount(Range):
    """
    Sets the value of X for the chosen Victory Condition. 
    If a target number higher than the number of total levels is given, target will automatically cap at 'all levels'. 
    """
    
    display_name = "Target Level Count"
    
    range_start = 1
    range_end = 108
    
    default = 25

class AvailableLevelsAtStart(Range):
    """
    How many levels are available initially.
    If other setting combinations lead to more overall items than locations, this setting may be automatically increased to make generation possible.
    """
    
    display_name = "Available Levels At Start"
    
    range_start = 1
    range_end = 108
    
    default = 2

class TargetTimesAreLocations(DefaultOnToggle):
    """
    Whether target times for levels are Locations."
    """
    
    display_name = "Target Times Are Locations"

class TargetTimeDifficulty(Choice):
    """
    How difficult the target times are per level. 
    Caution is strongly advised when using Rock Hard targets in a multiplayer game - they are very difficult. 
    """
    
    display_name = "Target Time Difficulty"
    
    option_easy = 0
    option_medium = 1
    option_hard = 2
    option_rock_hard = 3
    
    default = 1

class CrystalTargetsAreLocations(Toggle):
    """
    Whether target crystal counts for levels are Locations. 
    """
    
    display_name = "Crystal Targets Are Locations"

class CrystalTargetPercentage(Range):
    """
    The percentage of the total possible crystals required to clear the extra Location.
    Has no effect if Crystal Targets Are Locations is disabled.
    """
 
    display_name = "Crystal Target Percentage"
 
    range_start = 50
    range_end = 95
    
    default = 85

class BuildingsAreItems(DefaultOnToggle):
    """
    Whether Buildings must be found in the multiworld to be unlocked.
    """
    
    display_name = "Buildings Are Items"

class ItemsAreItems(DefaultOnToggle):
    """
    Whether Items (Electric Fences and Dynamite) must be found in the multiworld to be unlocked.
    """
    
    display_name = "Items Are Items"

class VehiclesAreItems(DefaultOnToggle):
    """
    Whether Vehicles must be found in the multiworld to be unlocked.
    """
    
    display_name = "Vehicles Are Items"

class BonusTruck(Toggle):
    """
    Whether to include a bonus starting Small Transport Truck in the Item pool."
    """
    
    display_name = "Chief's Favourite Truck"

class BreathingAlwaysInLogic(Toggle):
    """
    Whether the ability to build a Support Station is logically required for all levels with limited air.
    When enabled, some levels that can be comfortably beaten before the air runs out will remain out of logic. 
    Has no effect if Buildings Are Items is disabled.
    """
    
    display_name = "Breathing Always In Logic"

class FasterBlastingAlwaysInLogic(DefaultOnToggle):
    """
    The Small Mobile Laser Cutter and Small Digger are often in logic for their ability to get through hard rock walls, but both are quite slow at it. The Upgrade Station allows some improvement. 
    When this setting is enabled, any time that the Small Digger or SMLC is required by logic, so is the Upgrade Station. 
    """
    
    display_name = "Faster Blasting Always In Logic"

class BonusClearLocations(Toggle):
    """
    When enabled, clearing a level will award 2-5 Locations instead of 1. Harder levels are worth more.
    This may be automatically enabled if your other settings lead to more items than locations. 
    """
    
    display_name = "Enable Bonus Locations For Clearing Levels"

class CampaignSelectionLRR(DefaultOnToggle):
    """
    Whether your game will include the Standard campaign levels.
    If no campaigns are selected, this one will automatically enable.
    """
    
    display_name = "Include 'Standard' Campaign Levels"
    
class CampaignSelectionLRRR(Toggle):
    """
    Whether your game will include the Remastered campaign levels.
    """
    
    display_name = "Include 'Remastered' Campaign Levels"

class CampaignSelectionLRRC(Toggle):
    """
    Whether your game will include the Classic campaign levels.
    """
    
    display_name = "Include 'Classic' Campaign Levels"

# class CampaignSelectionBAZ(Toggle):
    # """
    # Whether your game will include the Baz's Mod campaign levels.
    # """
    
    # display_name = "Include 'Baz's Mod' Campaign Levels"

class NoDuplicateLevels(Toggle):
    """
    If this is enabled, instead of all selected levels, you will have only one of each, selected randomly from the enabled campaigns. 
    For example, you will have a random Rocky Horror, but only one.
    You are guaranteed to start with Driller Night. 
    """
    
    display_name = "No Duplicate Levels"

# Individual hidden options for each level
class LevelSelectionLRRABreathOfFreshAir(Toggle):
    visibility = Visibility.none
class LevelSelectionLRRAirRaiders(Toggle):
    visibility = Visibility.none
class LevelSelectionLRRBackToBasics(Toggle):
    visibility = Visibility.none
class LevelSelectionLRRBreathless(Toggle):
    visibility = Visibility.none
class LevelSelectionLRRDontPanic(Toggle):
    visibility = Visibility.none
class LevelSelectionLRRDrillerNight(Toggle):
    visibility = Visibility.none
class LevelSelectionLRRErodeWorks(Toggle):
    visibility = Visibility.none
class LevelSelectionLRRExplosiveAction(Toggle):
    visibility = Visibility.none
class LevelSelectionLRRFireAndWater(Toggle):
    visibility = Visibility.none
class LevelSelectionLRRFrozenFrenzy(Toggle):
    visibility = Visibility.none
class LevelSelectionLRRHotStuff(Toggle):
    visibility = Visibility.none
class LevelSelectionLRRIceSpy(Toggle):
    visibility = Visibility.none
class LevelSelectionLRRItsAHoldUp(Toggle):
    visibility = Visibility.none
class LevelSelectionLRRLakeOfFire(Toggle):
    visibility = Visibility.none
class LevelSelectionLRRLavaLaughter(Toggle):
    visibility = Visibility.none
class LevelSelectionLRROresome(Toggle):
    visibility = Visibility.none
class LevelSelectionLRRRockHard(Toggle):
    visibility = Visibility.none
class LevelSelectionLRRRockyHorror(Toggle):
    visibility = Visibility.none
class LevelSelectionLRRRubbleTrouble(Toggle):
    visibility = Visibility.none
class LevelSelectionLRRRunTheGauntlet(Toggle):
    visibility = Visibility.none
class LevelSelectionLRRSearchAndRescue(Toggle):
    visibility = Visibility.none
class LevelSelectionLRRSplitDownTheMiddle(Toggle):
    visibility = Visibility.none
class LevelSelectionLRRThePathToPower(Toggle):
    visibility = Visibility.none
class LevelSelectionLRRWaterLotOfFun(Toggle):
    visibility = Visibility.none
class LevelSelectionLRRWaterWorks(Toggle):
    visibility = Visibility.none

class LevelSelectionLRRRABreathOfFreshAir(Toggle):
    visibility = Visibility.none
class LevelSelectionLRRRAirRaiders(Toggle):
    visibility = Visibility.none
class LevelSelectionLRRRBackToBasics(Toggle):
    visibility = Visibility.none
class LevelSelectionLRRRBreathless(Toggle):
    visibility = Visibility.none
class LevelSelectionLRRRDontPanic(Toggle):
    visibility = Visibility.none
class LevelSelectionLRRRDrillerNight(Toggle):
    visibility = Visibility.none
class LevelSelectionLRRRErodeWorks(Toggle):
    visibility = Visibility.none
class LevelSelectionLRRRExplosiveAction(Toggle):
    visibility = Visibility.none
class LevelSelectionLRRRFireAndWater(Toggle):
    visibility = Visibility.none
class LevelSelectionLRRRFrozenFrenzy(Toggle):
    visibility = Visibility.none
class LevelSelectionLRRRHotStuff(Toggle):
    visibility = Visibility.none
class LevelSelectionLRRRIceSpy(Toggle):
    visibility = Visibility.none
class LevelSelectionLRRRItsAHoldUp(Toggle):
    visibility = Visibility.none
class LevelSelectionLRRRLakeOfFire(Toggle):
    visibility = Visibility.none
class LevelSelectionLRRRLavaLaughter(Toggle):
    visibility = Visibility.none
class LevelSelectionLRRROresome(Toggle):
    visibility = Visibility.none
class LevelSelectionLRRRRockHard(Toggle):
    visibility = Visibility.none
class LevelSelectionLRRRRockyHorror(Toggle):
    visibility = Visibility.none
class LevelSelectionLRRRRubbleTrouble(Toggle):
    visibility = Visibility.none
class LevelSelectionLRRRRunTheGauntlet(Toggle):
    visibility = Visibility.none
class LevelSelectionLRRRSearchAndRescue(Toggle):
    visibility = Visibility.none
class LevelSelectionLRRRSplitDownTheMiddle(Toggle):
    visibility = Visibility.none
class LevelSelectionLRRRThePathToPower(Toggle):
    visibility = Visibility.none
class LevelSelectionLRRRWaterLotOfFun(Toggle):
    visibility = Visibility.none
class LevelSelectionLRRRWaterWorks(Toggle):
    visibility = Visibility.none

class LevelSelectionLRRCABreathOfFreshAir(Toggle):
    visibility = Visibility.none
class LevelSelectionLRRCAirRaiders(Toggle):
    visibility = Visibility.none
class LevelSelectionLRRCBackToBasics(Toggle):
    visibility = Visibility.none
class LevelSelectionLRRCBreathless(Toggle):
    visibility = Visibility.none
class LevelSelectionLRRCDontPanic(Toggle):
    visibility = Visibility.none
class LevelSelectionLRRCDrillerNight(Toggle):
    visibility = Visibility.none
class LevelSelectionLRRCErodeWorks(Toggle):
    visibility = Visibility.none
class LevelSelectionLRRCExplosiveAction(Toggle):
    visibility = Visibility.none
class LevelSelectionLRRCFireAndWater(Toggle):
    visibility = Visibility.none
class LevelSelectionLRRCFrozenFrenzy(Toggle):
    visibility = Visibility.none
class LevelSelectionLRRCHotStuff(Toggle):
    visibility = Visibility.none
class LevelSelectionLRRCIceSpy(Toggle):
    visibility = Visibility.none
class LevelSelectionLRRCItsAHoldUp(Toggle):
    visibility = Visibility.none
class LevelSelectionLRRCLakeOfFire(Toggle):
    visibility = Visibility.none
class LevelSelectionLRRCLavaLaughter(Toggle):
    visibility = Visibility.none
class LevelSelectionLRRCOresome(Toggle):
    visibility = Visibility.none
class LevelSelectionLRRCRockHard(Toggle):
    visibility = Visibility.none
class LevelSelectionLRRCRockyHorror(Toggle):
    visibility = Visibility.none
class LevelSelectionLRRCRubbleTrouble(Toggle):
    visibility = Visibility.none
class LevelSelectionLRRCRunTheGauntlet(Toggle):
    visibility = Visibility.none
class LevelSelectionLRRCSearchAndRescue(Toggle):
    visibility = Visibility.none
class LevelSelectionLRRCSplitDownTheMiddle(Toggle):
    visibility = Visibility.none
class LevelSelectionLRRCThePathToPower(Toggle):
    visibility = Visibility.none
class LevelSelectionLRRCWaterLotOfFun(Toggle):
    visibility = Visibility.none
class LevelSelectionLRRCWaterWorks(Toggle):
    visibility = Visibility.none

class BossLevelLRRRockyHorror(Toggle):
    visibility = Visibility.none
class BossLevelLRRRRockyHorror(Toggle):
    visibility = Visibility.none
class BossLevelLRRCRockyHorror(Toggle):
    visibility = Visibility.none

@dataclass
class ManicMinersOptions(PerGameCommonOptions):
    victory_condition: VictoryCondition
    locked_coordinates: LockedCoordinates
    target_level_count: TargetLevelCount
    available_levels_at_start: AvailableLevelsAtStart
    target_times_are_locations: TargetTimesAreLocations
    target_time_difficulty: TargetTimeDifficulty
    crystal_targets_are_locations: CrystalTargetsAreLocations
    crystal_target_percentage: CrystalTargetPercentage
    buildings_are_items: BuildingsAreItems
    items_are_items: ItemsAreItems
    vehicles_are_items: VehiclesAreItems
    bonus_truck: BonusTruck
    breathing_always_in_logic: BreathingAlwaysInLogic
    faster_blasting_always_in_logic: FasterBlastingAlwaysInLogic
    bonus_clear_locations: BonusClearLocations
    campaign_selection_lrr: CampaignSelectionLRR
    campaign_selection_lrrr: CampaignSelectionLRRR
    campaign_selection_lrrc: CampaignSelectionLRRC
    # campaign_selection_baz: CampaignSelectionBAZ
    no_duplicate_levels: NoDuplicateLevels

    level_selection_lrr_abreathoffreshair: LevelSelectionLRRABreathOfFreshAir
    level_selection_lrr_airraiders: LevelSelectionLRRAirRaiders
    level_selection_lrr_backtobasics: LevelSelectionLRRBackToBasics
    level_selection_lrr_breathless: LevelSelectionLRRBreathless
    level_selection_lrr_dontpanic: LevelSelectionLRRDontPanic
    level_selection_lrr_drillernight: LevelSelectionLRRDrillerNight
    level_selection_lrr_erodeworks: LevelSelectionLRRErodeWorks
    level_selection_lrr_explosiveaction: LevelSelectionLRRExplosiveAction
    level_selection_lrr_fireandwater: LevelSelectionLRRFireAndWater
    level_selection_lrr_frozenfrenzy: LevelSelectionLRRFrozenFrenzy
    level_selection_lrr_hotstuff: LevelSelectionLRRHotStuff
    level_selection_lrr_icespy: LevelSelectionLRRIceSpy
    level_selection_lrr_itsaholdup: LevelSelectionLRRItsAHoldUp
    level_selection_lrr_lakeoffire: LevelSelectionLRRLakeOfFire
    level_selection_lrr_lavalaughter: LevelSelectionLRRLavaLaughter
    level_selection_lrr_oresome: LevelSelectionLRROresome
    level_selection_lrr_rockhard: LevelSelectionLRRRockHard
    level_selection_lrr_rockyhorror: LevelSelectionLRRRockyHorror
    level_selection_lrr_rubbletrouble: LevelSelectionLRRRubbleTrouble
    level_selection_lrr_runthegauntlet: LevelSelectionLRRRunTheGauntlet
    level_selection_lrr_searchandrescue: LevelSelectionLRRSearchAndRescue
    level_selection_lrr_splitdownthemiddle: LevelSelectionLRRSplitDownTheMiddle
    level_selection_lrr_thepathtopower: LevelSelectionLRRThePathToPower
    level_selection_lrr_waterlotoffun: LevelSelectionLRRWaterLotOfFun
    level_selection_lrr_waterworks: LevelSelectionLRRWaterWorks

    level_selection_lrrr_abreathoffreshair: LevelSelectionLRRRABreathOfFreshAir
    level_selection_lrrr_airraiders: LevelSelectionLRRRAirRaiders
    level_selection_lrrr_backtobasics: LevelSelectionLRRRBackToBasics
    level_selection_lrrr_breathless: LevelSelectionLRRRBreathless
    level_selection_lrrr_dontpanic: LevelSelectionLRRRDontPanic
    level_selection_lrrr_drillernight: LevelSelectionLRRRDrillerNight
    level_selection_lrrr_erodeworks: LevelSelectionLRRRErodeWorks
    level_selection_lrrr_explosiveaction: LevelSelectionLRRRExplosiveAction
    level_selection_lrrr_fireandwater: LevelSelectionLRRRFireAndWater
    level_selection_lrrr_frozenfrenzy: LevelSelectionLRRRFrozenFrenzy
    level_selection_lrrr_hotstuff: LevelSelectionLRRRHotStuff
    level_selection_lrrr_icespy: LevelSelectionLRRRIceSpy
    level_selection_lrrr_itsaholdup: LevelSelectionLRRRItsAHoldUp
    level_selection_lrrr_lakeoffire: LevelSelectionLRRRLakeOfFire
    level_selection_lrrr_lavalaughter: LevelSelectionLRRRLavaLaughter
    level_selection_lrrr_oresome: LevelSelectionLRRROresome
    level_selection_lrrr_rockhard: LevelSelectionLRRRRockHard
    level_selection_lrrr_rockyhorror: LevelSelectionLRRRRockyHorror
    level_selection_lrrr_rubbletrouble: LevelSelectionLRRRRubbleTrouble
    level_selection_lrrr_runthegauntlet: LevelSelectionLRRRRunTheGauntlet
    level_selection_lrrr_searchandrescue: LevelSelectionLRRRSearchAndRescue
    level_selection_lrrr_splitdownthemiddle: LevelSelectionLRRRSplitDownTheMiddle
    level_selection_lrrr_thepathtopower: LevelSelectionLRRRThePathToPower
    level_selection_lrrr_waterlotoffun: LevelSelectionLRRRWaterLotOfFun
    level_selection_lrrr_waterworks: LevelSelectionLRRRWaterWorks
    
    level_selection_lrrc_abreathoffreshair: LevelSelectionLRRCABreathOfFreshAir
    level_selection_lrrc_airraiders: LevelSelectionLRRCAirRaiders
    level_selection_lrrc_backtobasics: LevelSelectionLRRCBackToBasics
    level_selection_lrrc_breathless: LevelSelectionLRRCBreathless
    level_selection_lrrc_dontpanic: LevelSelectionLRRCDontPanic
    level_selection_lrrc_drillernight: LevelSelectionLRRCDrillerNight
    level_selection_lrrc_erodeworks: LevelSelectionLRRCErodeWorks
    level_selection_lrrc_explosiveaction: LevelSelectionLRRCExplosiveAction
    level_selection_lrrc_fireandwater: LevelSelectionLRRCFireAndWater
    level_selection_lrrc_frozenfrenzy: LevelSelectionLRRCFrozenFrenzy
    level_selection_lrrc_hotstuff: LevelSelectionLRRCHotStuff
    level_selection_lrrc_icespy: LevelSelectionLRRCIceSpy
    level_selection_lrrc_itsaholdup: LevelSelectionLRRCItsAHoldUp
    level_selection_lrrc_lakeoffire: LevelSelectionLRRCLakeOfFire
    level_selection_lrrc_lavalaughter: LevelSelectionLRRCLavaLaughter
    level_selection_lrrc_oresome: LevelSelectionLRRCOresome
    level_selection_lrrc_rockhard: LevelSelectionLRRCRockHard
    level_selection_lrrc_rockyhorror: LevelSelectionLRRCRockyHorror
    level_selection_lrrc_rubbletrouble: LevelSelectionLRRCRubbleTrouble
    level_selection_lrrc_runthegauntlet: LevelSelectionLRRCRunTheGauntlet
    level_selection_lrrc_searchandrescue: LevelSelectionLRRCSearchAndRescue
    level_selection_lrrc_splitdownthemiddle: LevelSelectionLRRCSplitDownTheMiddle
    level_selection_lrrc_thepathtopower: LevelSelectionLRRCThePathToPower
    level_selection_lrrc_waterlotoffun: LevelSelectionLRRCWaterLotOfFun
    level_selection_lrrc_waterworks: LevelSelectionLRRCWaterWorks
    
    boss_level_lrr_rockyhorror: BossLevelLRRRockyHorror
    boss_level_lrrr_rockyhorror: BossLevelLRRRRockyHorror
    boss_level_lrrc_rockyhorror: BossLevelLRRCRockyHorror

option_groups = [
    OptionGroup(
        "Campaign Selection",
        # [CampaignSelectionLRR,CampaignSelectionLRRR,CampaignSelectionLRRC,CampaignSelectionBAZ]
        [CampaignSelectionLRR,CampaignSelectionLRRR,CampaignSelectionLRRC,NoDuplicateLevels]
    ),
    OptionGroup(
        "Goal",
        [VictoryCondition,LockedCoordinates,TargetLevelCount]
    ),
    OptionGroup(
        "Locations",
        [TargetTimesAreLocations,TargetTimeDifficulty,CrystalTargetsAreLocations,CrystalTargetPercentage,BonusClearLocations]
    ),
    OptionGroup(
        "Items",
        [AvailableLevelsAtStart,BuildingsAreItems,ItemsAreItems,VehiclesAreItems,BonusTruck]
    ),
    OptionGroup(
        "Logic",
        [BreathingAlwaysInLogic,FasterBlastingAlwaysInLogic]
    ),
]