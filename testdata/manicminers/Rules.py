from __future__ import annotations

from worlds.generic.Rules import set_rule, add_rule
from rule_builder.rules import Has, HasAll, HasAny, OptionFilter, Filtered, CanReachRegion
from . import Items
from . import Options as ManicMiners_Options

from typing import TYPE_CHECKING
if TYPE_CHECKING:    
    from .World import ManicMinersWorld

def set_all_rules(world: ManicMinersWorld) -> None:
    set_all_entrance_and_location_rules(world)
    set_completion_condition(world)
    
def set_all_entrance_and_location_rules(world: ManicMinersWorld) -> None:
    
    rule_can_build_toolstore = Has("Building Unlock: Tool Store")
    rule_can_build_teleportpad = HasAll("Building Unlock: Teleport Pad", "Building Unlock: Power Station")
    rule_can_build_powerstation = rule_can_build_teleportpad
    rule_can_build_docks = Has("Building Unlock: Docks") & rule_can_build_powerstation
    rule_can_build_canteen = Has("Building Unlock: Canteen")
    rule_can_build_supportstation = Has("Building Unlock: Support Station") & rule_can_build_powerstation
    rule_can_build_geologicalcenter = Has("Building Unlock: Geological Center") & rule_can_build_powerstation
    rule_can_build_upgradestation = Has("Building Unlock: Upgrade Station") & rule_can_build_powerstation
    rule_can_build_orerefinery = Has("Building Unlock: Ore Refinery") & rule_can_build_powerstation
    rule_can_build_mininglaser = Has("Building Unlock: Mining Laser") & rule_can_build_supportstation
    rule_can_build_superteleport = Has("Building Unlock: Super Teleport") & rule_can_build_supportstation
    rule_can_breathe = rule_can_build_supportstation
    rule_can_always_breathe = Filtered(rule_can_breathe, options = [OptionFilter(ManicMiners_Options.BreathingAlwaysInLogic, 1)], filtered_resolution = True)
    rule_can_build_smalldigger = Has("Vehicle Unlock: Small Digger") & rule_can_build_supportstation & Filtered(rule_can_build_upgradestation, options = [OptionFilter(ManicMiners_Options.FasterBlastingAlwaysInLogic, 1)], filtered_resolution = True)
    rule_can_build_smlc = Has("Vehicle Unlock: Small Mobile Laser Cutter") & rule_can_build_supportstation & Filtered(rule_can_build_upgradestation, options = [OptionFilter(ManicMiners_Options.FasterBlastingAlwaysInLogic, 1)], filtered_resolution = True)
    rule_can_build_rapidrider = rule_can_build_docks & Has("Vehicle Unlock: Rapid Rider")
    rule_can_build_cargocarrier = rule_can_build_docks & Has("Vehicle Unlock: Cargo Carrier")
    rule_can_build_tunnelscout = rule_can_build_teleportpad & Has("Vehicle Unlock: Tunnel Scout")
    rule_can_build_tunneltransport = rule_can_build_superteleport & Has("Vehicle Unlock: Tunnel Transport")
    rule_can_build_hoverscout = rule_can_build_teleportpad & Has("Vehicle Unlock: Tunnel Scout")
    rule_can_build_granitegrinder = rule_can_build_superteleport & Has("Vehicle Unlock: Granite Grinder")
    rule_can_jump = rule_can_build_hoverscout | rule_can_build_granitegrinder
    rule_can_fly = rule_can_build_tunnelscout | rule_can_build_tunneltransport
    rule_can_swim = rule_can_fly | rule_can_build_rapidrider | rule_can_build_cargocarrier
    rule_can_vehicle_lase = rule_can_build_smlc | (HasAny("Vehicle Unlock: Chrome Crusher","Vehicle Unlock: Large Mobile Laser Cutter") & rule_can_build_superteleport)
    rule_can_lase = rule_can_vehicle_lase | rule_can_build_mininglaser
    rule_can_flying_lase = rule_can_vehicle_lase & rule_can_build_tunneltransport
    rule_can_flydrill = (rule_can_build_tunnelscout & rule_can_build_upgradestation) | rule_can_flying_lase
    rule_can_swimdrill = (rule_can_flydrill | rule_can_build_rapidrider)
    rule_can_blast = Has("Item Unlock: Dynamite") | rule_can_lase | rule_can_build_smalldigger | rule_can_build_granitegrinder

    if world.options.level_selection_lrr_abreathoffreshair:
        entrance_lrr_abreathoffreshair = world.get_entrance("Start Level - LRR - A Breath Of Fresh Air")
        world.set_rule(entrance_lrr_abreathoffreshair, (rule_can_breathe & Has("Level Access: LRR - A Breath Of Fresh Air")))
        if world.options.crystal_targets_are_locations:
            location_crystals_lrr_abreathoffreshair = world.get_location("Crystal Target: LRR - A Breath Of Fresh Air")
            world.set_rule(location_crystals_lrr_abreathoffreshair, rule_can_blast)
        if world.options.victory_condition == 2:
            event_crystals_lrr_abreathoffreshair = world.get_location("Crystal Target Beatable: LRR - A Breath Of Fresh Air")
            world.set_rule(event_crystals_lrr_abreathoffreshair, rule_can_blast)
    if world.options.level_selection_lrr_airraiders:
        entrance_lrr_airraiders = world.get_entrance("Start Level - LRR - Air Raiders")
        world.set_rule(entrance_lrr_airraiders, Has("Level Access: LRR - Air Raiders"))
        if world.options.crystal_targets_are_locations:
            location_crystals_lrr_airraiders = world.get_location("Crystal Target: LRR - Air Raiders")
            world.set_rule(location_crystals_lrr_airraiders, rule_can_blast)
        if world.options.victory_condition == 2:
            event_crystals_lrr_airraiders = world.get_location("Crystal Target Beatable: LRR - Air Raiders")
            world.set_rule(event_crystals_lrr_airraiders, rule_can_blast)
    if world.options.level_selection_lrr_backtobasics:
        entrance_lrr_backtobasics = world.get_entrance("Start Level - LRR - Back To Basics")
        world.set_rule(entrance_lrr_backtobasics, (rule_can_breathe & Has("Level Access: LRR - Back To Basics")))
        if world.options.crystal_targets_are_locations:
            location_crystals_lrr_backtobasics = world.get_location("Crystal Target: LRR - Back To Basics")
            world.set_rule(location_crystals_lrr_backtobasics, (rule_can_swim & rule_can_blast))
        if world.options.victory_condition == 2:
            event_crystals_lrr_backtobasics = world.get_location("Crystal Target Beatable: LRR - Back To Basics")
            world.set_rule(event_crystals_lrr_backtobasics, (rule_can_swim & rule_can_blast))
    if world.options.level_selection_lrr_breathless:
        entrance_lrr_breathless = world.get_entrance("Start Level - LRR - Breathless")
        world.set_rule(entrance_lrr_breathless, ((Has("Item Unlock: Dynamite") | rule_can_build_mininglaser | rule_can_build_smlc | rule_can_build_smalldigger | rule_can_build_granitegrinder) & Has("Level Access: LRR - Breathless") & rule_can_always_breathe))
    if world.options.level_selection_lrr_dontpanic:
        entrance_lrr_dontpanic = world.get_entrance("Start Level - LRR - Don't Panic")
        world.set_rule(entrance_lrr_dontpanic, Has("Level Access: LRR - Don't Panic"))
    if world.options.level_selection_lrr_drillernight:
        entrance_lrr_drillernight = world.get_entrance("Start Level - LRR - Driller Night")
        world.set_rule(entrance_lrr_drillernight, Has("Level Access: LRR - Driller Night"))
    if world.options.level_selection_lrr_erodeworks:
        entrance_lrr_erodeworks = world.get_entrance("Start Level - LRR - Erode Works")
        world.set_rule(entrance_lrr_erodeworks, (rule_can_blast & Has("Level Access: LRR - Erode Works")))
        if world.options.crystal_targets_are_locations:
            location_crystals_lrr_erodeworks = world.get_location("Crystal Target: LRR - Erode Works")
            world.set_rule(location_crystals_lrr_erodeworks, rule_can_fly)
        if world.options.victory_condition == 2:
            event_crystals_lrr_erodeworks = world.get_location("Crystal Target Beatable: LRR - Erode Works")
            world.set_rule(event_crystals_lrr_erodeworks, rule_can_fly)
    if world.options.level_selection_lrr_explosiveaction:
        entrance_lrr_explosiveaction = world.get_entrance("Start Level - LRR - Explosive Action")
        world.set_rule(entrance_lrr_explosiveaction, ((Has("Item Unlock: Dynamite") | rule_can_build_smalldigger | rule_can_build_mininglaser) & rule_can_build_supportstation & Has("Level Access: LRR - Explosive Action")))
        if world.options.crystal_targets_are_locations:
            location_crystals_lrr_explosiveaction = world.get_location("Crystal Target: LRR - Explosive Action")
            world.set_rule(location_crystals_lrr_explosiveaction, rule_can_build_rapidrider)
        if world.options.victory_condition == 2:
            event_crystals_lrr_explosiveaction = world.get_location("Crystal Target Beatable: LRR - Explosive Action")
            world.set_rule(event_crystals_lrr_explosiveaction, rule_can_build_rapidrider)
    if world.options.level_selection_lrr_fireandwater:
        entrance_lrr_fireandwater = world.get_entrance("Start Level - LRR - Fire And Water")
        world.set_rule(entrance_lrr_fireandwater, (rule_can_breathe & rule_can_swim & Has("Level Access: LRR - Fire And Water")))
        if world.options.crystal_targets_are_locations:
            location_crystals_lrr_fireandwater = world.get_location("Crystal Target: LRR - Fire And Water")
            world.set_rule(location_crystals_lrr_fireandwater, rule_can_blast)
        if world.options.victory_condition == 2:
            event_crystals_lrr_fireandwater = world.get_location("Crystal Target Beatable: LRR - Fire And Water")
            world.set_rule(event_crystals_lrr_fireandwater, rule_can_blast)
    if world.options.level_selection_lrr_frozenfrenzy:
        entrance_lrr_frozenfrenzy = world.get_entrance("Start Level - LRR - Frozen Frenzy")
        world.set_rule(entrance_lrr_frozenfrenzy, (rule_can_blast & Has("Level Access: LRR - Frozen Frenzy") & rule_can_always_breathe))
    if world.options.level_selection_lrr_hotstuff:
        entrance_lrr_hotstuff = world.get_entrance("Start Level - LRR - Hot Stuff")
        world.set_rule(entrance_lrr_hotstuff, (rule_can_breathe & Has("Level Access: LRR - Hot Stuff")))
        if world.options.crystal_targets_are_locations:
            location_crystals_lrr_hotstuff = world.get_location("Crystal Target: LRR - Hot Stuff")
            world.set_rule(location_crystals_lrr_hotstuff, rule_can_flying_lase)
        if world.options.victory_condition == 2:
            event_crystals_lrr_hotstuff = world.get_location("Crystal Target Beatable: LRR - Hot Stuff")
            world.set_rule(event_crystals_lrr_hotstuff, rule_can_flying_lase)
    if world.options.level_selection_lrr_icespy:
        entrance_lrr_icespy = world.get_entrance("Start Level - LRR - Ice Spy")
        world.set_rule(entrance_lrr_icespy, (rule_can_breathe & Has("Level Access: LRR - Ice Spy")))
    if world.options.level_selection_lrr_itsaholdup:
        entrance_lrr_itsaholdup = world.get_entrance("Start Level - LRR - It's A Hold Up")
        world.set_rule(entrance_lrr_itsaholdup, Has("Level Access: LRR - It's A Hold Up"))
        if world.options.crystal_targets_are_locations:
            location_crystals_lrr_itsaholdup = world.get_location("Crystal Target: LRR - It's A Hold Up")
            world.set_rule(location_crystals_lrr_itsaholdup, (Has("Item Unlock: Dynamite") | rule_can_build_smlc | rule_can_build_smalldigger | rule_can_build_mininglaser))
        if world.options.victory_condition == 2:
            event_crystals_lrr_itsaholdup = world.get_location("Crystal Target Beatable: LRR - It's A Hold Up")
            world.set_rule(event_crystals_lrr_itsaholdup, (Has("Item Unlock: Dynamite") | rule_can_build_smlc | rule_can_build_smalldigger | rule_can_build_mininglaser))
    if world.options.level_selection_lrr_lakeoffire:
        entrance_lrr_lakeoffire = world.get_entrance("Start Level - LRR - Lake Of Fire")
        world.set_rule(entrance_lrr_lakeoffire, Has("Level Access: LRR - Lake Of Fire"))
        if world.options.crystal_targets_are_locations:
            location_crystals_lrr_lakeoffire = world.get_location("Crystal Target: LRR - Lake Of Fire")
            world.set_rule(location_crystals_lrr_lakeoffire, rule_can_flying_lase)
        if world.options.victory_condition == 2:
            event_crystals_lrr_lakeoffire = world.get_location("Crystal Target Beatable: LRR - Lake Of Fire")
            world.set_rule(event_crystals_lrr_lakeoffire, rule_can_flying_lase)
    if world.options.level_selection_lrr_lavalaughter:
        entrance_lrr_lavalaughter = world.get_entrance("Start Level - LRR - Lava Laughter")
        world.set_rule(entrance_lrr_lavalaughter, (rule_can_breathe & Has("Level Access: LRR - Lava Laughter")))
        if world.options.crystal_targets_are_locations:
            location_crystals_lrr_lavalaughter = world.get_location("Crystal Target: LRR - Lava Laughter")
            world.set_rule(location_crystals_lrr_lavalaughter, rule_can_blast)
        if world.options.victory_condition == 2:
            event_crystals_lrr_lavalaughter = world.get_location("Crystal Target Beatable: LRR - Lava Laughter")
            world.set_rule(event_crystals_lrr_lavalaughter, rule_can_blast)
    if world.options.level_selection_lrr_oresome:
        entrance_lrr_oresome = world.get_entrance("Start Level - LRR - Oresome")
        world.set_rule(entrance_lrr_oresome, Has("Level Access: LRR - Oresome"))
        if world.options.crystal_targets_are_locations:
            location_crystals_lrr_oresome = world.get_location("Crystal Target: LRR - Oresome")
            world.set_rule(location_crystals_lrr_oresome, rule_can_flying_lase)
        if world.options.victory_condition == 2:
            event_crystals_lrr_oresome = world.get_location("Crystal Target Beatable: LRR - Oresome")
            world.set_rule(event_crystals_lrr_oresome, rule_can_flying_lase)
    if world.options.level_selection_lrr_rockhard:
        entrance_lrr_rockhard = world.get_entrance("Start Level - LRR - Rock Hard")
        world.set_rule(entrance_lrr_rockhard, ((Has("Item Unlock: Dynamite") | rule_can_build_mininglaser) & Has("Level Access: LRR - Rock Hard") & rule_can_always_breathe))
        if world.options.crystal_targets_are_locations:
            location_crystals_lrr_rockhard = world.get_location("Crystal Target: LRR - Rock Hard")
            world.set_rule(location_crystals_lrr_rockhard, (rule_can_breathe & rule_can_swim))
        if world.options.victory_condition == 2:
            event_crystals_lrr_rockhard = world.get_location("Crystal Target Beatable: LRR - Rock Hard")
            world.set_rule(event_crystals_lrr_rockhard, (rule_can_breathe & rule_can_swim))
    if world.options.level_selection_lrr_rockyhorror:
        entrance_lrr_rockyhorror = world.get_entrance("Start Level - LRR - Rocky Horror")
        world.set_rule(entrance_lrr_rockyhorror, (rule_can_breathe & Has("Level Access: LRR - Rocky Horror") & Has("Transporter Coordinates",world.options.target_level_count.value,options=[OptionFilter(ManicMiners_Options.BossLevelLRRRockyHorror,1)],filtered_resolution=True)))
        if world.options.crystal_targets_are_locations and world.options.boss_level_lrr_rockyhorror == 0:
            location_crystals_lrr_rockyhorror = world.get_location("Crystal Target: LRR - Rocky Horror")
            world.set_rule(location_crystals_lrr_rockyhorror, rule_can_blast)
        if world.options.victory_condition == 2:
            event_crystals_lrr_rockyhorror = world.get_location("Crystal Target Beatable: LRR - Rocky Horror")
            world.set_rule(event_crystals_lrr_rockyhorror, rule_can_blast)
    if world.options.level_selection_lrr_rubbletrouble:
        entrance_lrr_rubbletrouble = world.get_entrance("Start Level - LRR - Rubble Trouble")
        world.set_rule(entrance_lrr_rubbletrouble, Has("Level Access: LRR - Rubble Trouble"))
    if world.options.level_selection_lrr_runthegauntlet:
        entrance_lrr_runthegauntlet = world.get_entrance("Start Level - LRR - Run The Gauntlet")
        world.set_rule(entrance_lrr_runthegauntlet, Has("Level Access: LRR - Run The Gauntlet"))
    if world.options.level_selection_lrr_searchandrescue:
        entrance_lrr_searchandrescue = world.get_entrance("Start Level - LRR - Search And Rescue")
        world.set_rule(entrance_lrr_searchandrescue, (rule_can_swim & Has("Level Access: LRR - Search And Rescue")))
        if world.options.crystal_targets_are_locations:
            location_crystals_lrr_searchandrescue = world.get_location("Crystal Target: LRR - Search And Rescue")
            world.set_rule(location_crystals_lrr_searchandrescue, (rule_can_blast & rule_can_swimdrill))
        if world.options.victory_condition == 2:
            event_crystals_lrr_searchandrescue = world.get_location("Crystal Target Beatable: LRR - Search And Rescue")
            world.set_rule(event_crystals_lrr_searchandrescue, (rule_can_blast & rule_can_swimdrill))
    if world.options.level_selection_lrr_splitdownthemiddle:
        entrance_lrr_splitdownthemiddle = world.get_entrance("Start Level - LRR - Split Down The Middle")
        world.set_rule(entrance_lrr_splitdownthemiddle, Has("Level Access: LRR - Split Down The Middle"))
    if world.options.level_selection_lrr_thepathtopower:
        entrance_lrr_thepathtopower = world.get_entrance("Start Level - LRR - The Path To Power")
        world.set_rule(entrance_lrr_thepathtopower, (rule_can_build_powerstation & Has("Level Access: LRR - The Path To Power")))
        if world.options.crystal_targets_are_locations:
            location_crystals_lrr_thepathtopower = world.get_location("Crystal Target: LRR - The Path To Power")
            world.set_rule(location_crystals_lrr_thepathtopower, (Has("Item Unlock: Dynamite") | rule_can_build_smlc | rule_can_build_smalldigger | rule_can_build_mininglaser))
        if world.options.victory_condition == 2:
            event_crystals_lrr_thepathtopower = world.get_location("Crystal Target Beatable: LRR - The Path To Power")
            world.set_rule(event_crystals_lrr_thepathtopower, (Has("Item Unlock: Dynamite") | rule_can_build_smlc | rule_can_build_smalldigger | rule_can_build_mininglaser))
    if world.options.level_selection_lrr_waterlotoffun:
        entrance_lrr_waterlotoffun = world.get_entrance("Start Level - LRR - Water Lot Of Fun")
        world.set_rule(entrance_lrr_waterlotoffun, ((rule_can_build_rapidrider | rule_can_build_cargocarrier | rule_can_build_tunnelscout) & (rule_can_build_toolstore | ((Has("Item Unlock: Dynamite") | rule_can_build_mininglaser) & rule_can_breathe) | (rule_can_build_rapidrider & rule_can_blast & rule_can_breathe)) & Has("Level Access: LRR - Water Lot Of Fun") & rule_can_always_breathe))
        if world.options.crystal_targets_are_locations:
            location_crystals_lrr_waterlotoffun = world.get_location("Crystal Target: LRR - Water Lot Of Fun")
            world.set_rule(location_crystals_lrr_waterlotoffun, (rule_can_breathe & rule_can_swimdrill & rule_can_blast))
        if world.options.victory_condition == 2:
            event_crystals_lrr_waterlotoffun = world.get_location("Crystal Target Beatable: LRR - Water Lot Of Fun")
            world.set_rule(event_crystals_lrr_waterlotoffun, (rule_can_breathe & rule_can_swimdrill & rule_can_blast))
    if world.options.level_selection_lrr_waterworks:
        entrance_lrr_waterworks = world.get_entrance("Start Level - LRR - Water Works")
        world.set_rule(entrance_lrr_waterworks, (rule_can_swim & Has("Level Access: LRR - Water Works") & rule_can_always_breathe))
        if world.options.crystal_targets_are_locations:
            location_crystals_lrr_waterworks = world.get_location("Crystal Target: LRR - Water Works")
            world.set_rule(location_crystals_lrr_waterworks, (rule_can_breathe & rule_can_blast))
        if world.options.victory_condition == 2:
            event_crystals_lrr_waterworks = world.get_location("Crystal Target Beatable: LRR - Water Works")
            world.set_rule(event_crystals_lrr_waterworks, (rule_can_breathe & rule_can_blast))
    
    if world.options.level_selection_lrrr_abreathoffreshair:
        entrance_lrrr_abreathoffreshair = world.get_entrance("Start Level - LRRR - A Breath Of Fresh Air")
        world.set_rule(entrance_lrrr_abreathoffreshair, (rule_can_breathe & Has("Item Unlock: Dynamite") & Has("Level Access: LRRR - A Breath Of Fresh Air")))
        if world.options.crystal_targets_are_locations:
            location_crystals_lrrr_abreathoffreshair = world.get_location("Crystal Target: LRRR - A Breath Of Fresh Air")
            world.set_rule(location_crystals_lrrr_abreathoffreshair, rule_can_swimdrill)
        if world.options.victory_condition == 2:
            event_crystals_lrrr_abreathoffreshair = world.get_location("Crystal Target Beatable: LRRR - A Breath Of Fresh Air")
            world.set_rule(event_crystals_lrrr_abreathoffreshair, rule_can_swimdrill)
    if world.options.level_selection_lrrr_airraiders:
        entrance_lrrr_airraiders = world.get_entrance("Start Level - LRRR - Air Raiders")
        world.set_rule(entrance_lrrr_airraiders, (rule_can_breathe & rule_can_blast & Has("Level Access: LRRR - Air Raiders")))
        if world.options.crystal_targets_are_locations:
            location_crystals_lrrr_airraiders = world.get_location("Crystal Target: LRRR - Air Raiders")
            world.set_rule(location_crystals_lrrr_airraiders, rule_can_swimdrill)
        if world.options.victory_condition == 2:
            event_crystals_lrrr_airraiders = world.get_location("Crystal Target Beatable: LRRR - Air Raiders")
            world.set_rule(event_crystals_lrrr_airraiders, rule_can_swimdrill)
    if world.options.level_selection_lrrr_backtobasics:
        entrance_lrrr_backtobasics = world.get_entrance("Start Level - LRRR - Back To Basics")
        world.set_rule(entrance_lrrr_backtobasics, (rule_can_breathe & rule_can_build_toolstore & rule_can_build_upgradestation & Has("Item Unlock: Electric Fence") & Has("Level Access: LRRR - Back To Basics")))
        if world.options.crystal_targets_are_locations:
            location_crystals_lrrr_backtobasics = world.get_location("Crystal Target: LRRR - Back To Basics")
            world.set_rule(location_crystals_lrrr_backtobasics, rule_can_flying_lase)
        if world.options.victory_condition == 2:
            event_crystals_lrrr_backtobasics = world.get_location("Crystal Target Beatable: LRRR - Back To Basics")
            world.set_rule(event_crystals_lrrr_backtobasics, rule_can_flying_lase)
    if world.options.level_selection_lrrr_breathless:
        entrance_lrrr_breathless = world.get_entrance("Start Level - LRRR - Breathless")
        world.set_rule(entrance_lrrr_breathless, (rule_can_breathe & rule_can_build_geologicalcenter & Has("Level Access: LRRR - Breathless")))
    if world.options.level_selection_lrrr_dontpanic:
        entrance_lrrr_dontpanic = world.get_entrance("Start Level - LRRR - Don't Panic")
        world.set_rule(entrance_lrrr_dontpanic, Has("Level Access: LRRR - Don't Panic"))
        if world.options.crystal_targets_are_locations:
            location_crystals_lrrr_dontpanic = world.get_location("Crystal Target: LRRR - Don't Panic")
            world.set_rule(location_crystals_lrrr_dontpanic, rule_can_build_tunneltransport)
        if world.options.victory_condition == 2:
            event_crystals_lrrr_dontpanic = world.get_location("Crystal Target Beatable: LRRR - Don't Panic")
            world.set_rule(event_crystals_lrrr_dontpanic, rule_can_build_tunneltransport)
    if world.options.level_selection_lrrr_drillernight:
        entrance_lrrr_drillernight = world.get_entrance("Start Level - LRRR - Driller Night")
        world.set_rule(entrance_lrrr_drillernight, Has("Level Access: LRRR - Driller Night"))
    if world.options.level_selection_lrrr_erodeworks:
        entrance_lrrr_erodeworks = world.get_entrance("Start Level - LRRR - Erode Works")
        world.set_rule(entrance_lrrr_erodeworks, (Has("Item Unlock: Dynamite") & Has("Level Access: LRRR - Erode Works")))
        if world.options.crystal_targets_are_locations:
            location_crystals_lrrr_erodeworks = world.get_location("Crystal Target: LRRR - Erode Works")
            world.set_rule(location_crystals_lrrr_erodeworks, rule_can_flying_lase)
        if world.options.victory_condition == 2:
            event_crystals_lrrr_erodeworks = world.get_location("Crystal Target Beatable: LRRR - Erode Works")
            world.set_rule(event_crystals_lrrr_erodeworks, rule_can_flying_lase)
    if world.options.level_selection_lrrr_explosiveaction:
        entrance_lrrr_explosiveaction = world.get_entrance("Start Level - LRRR - Explosive Action")
        world.set_rule(entrance_lrrr_explosiveaction, (rule_can_swim & rule_can_build_supportstation & Has("Level Access: LRRR - Explosive Action")))
    if world.options.level_selection_lrrr_fireandwater:
        entrance_lrrr_fireandwater = world.get_entrance("Start Level - LRRR - Fire And Water")
        world.set_rule(entrance_lrrr_fireandwater, (rule_can_breathe & (rule_can_build_rapidrider | rule_can_fly) & Has("Level Access: LRRR - Fire And Water")))
        if world.options.crystal_targets_are_locations:
            location_crystals_lrrr_fireandwater = world.get_location("Crystal Target: LRRR - Fire And Water")
            world.set_rule(location_crystals_lrrr_fireandwater, rule_can_flying_lase)
        if world.options.victory_condition == 2:
            event_crystals_lrrr_fireandwater = world.get_location("Crystal Target Beatable: LRRR - Fire And Water")
            world.set_rule(event_crystals_lrrr_fireandwater, rule_can_flying_lase)
    if world.options.level_selection_lrrr_frozenfrenzy:
        entrance_lrrr_frozenfrenzy = world.get_entrance("Start Level - LRRR - Frozen Frenzy")
        world.set_rule(entrance_lrrr_frozenfrenzy, (rule_can_breathe & rule_can_blast & rule_can_swimdrill & Has("Level Access: LRRR - Frozen Frenzy")))
        if world.options.crystal_targets_are_locations:
            location_crystals_lrrr_frozenfrenzy = world.get_location("Crystal Target: LRRR - Frozen Frenzy")
            world.set_rule(location_crystals_lrrr_frozenfrenzy, rule_can_vehicle_lase)
        if world.options.victory_condition == 2:
            event_crystals_lrrr_frozenfrenzy = world.get_location("Crystal Target Beatable: LRRR - Frozen Frenzy")
            world.set_rule(event_crystals_lrrr_frozenfrenzy, rule_can_vehicle_lase)
    if world.options.level_selection_lrrr_hotstuff:
        entrance_lrrr_hotstuff = world.get_entrance("Start Level - LRRR - Hot Stuff")
        world.set_rule(entrance_lrrr_hotstuff, (rule_can_breathe & rule_can_build_toolstore & rule_can_fly & Has("Level Access: LRRR - Hot Stuff")))
        if world.options.crystal_targets_are_locations:
            location_crystals_lrrr_hotstuff = world.get_location("Crystal Target: LRRR - Hot Stuff")
            world.set_rule(location_crystals_lrrr_hotstuff, rule_can_flying_lase)
        if world.options.victory_condition == 2:
            event_crystals_lrrr_hotstuff = world.get_location("Crystal Target Beatable: LRRR - Hot Stuff")
            world.set_rule(event_crystals_lrrr_hotstuff, rule_can_flying_lase)
    if world.options.level_selection_lrrr_icespy:
        entrance_lrrr_icespy = world.get_entrance("Start Level - LRRR - Ice Spy")
        world.set_rule(entrance_lrrr_icespy, (rule_can_breathe & Has("Level Access: LRRR - Ice Spy")))
        if world.options.crystal_targets_are_locations:
            location_crystals_lrrr_icespy = world.get_location("Crystal Target: LRRR - Ice Spy")
            world.set_rule(location_crystals_lrrr_icespy, (Has("Item Unlock: Electric Fence") & rule_can_swim & rule_can_blast))
        if world.options.victory_condition == 2:
            event_crystals_lrrr_icespy = world.get_location("Crystal Target Beatable: LRRR - Ice Spy")
            world.set_rule(event_crystals_lrrr_icespy, (Has("Item Unlock: Electric Fence") & rule_can_swim & rule_can_blast))
    if world.options.level_selection_lrrr_itsaholdup:
        entrance_lrrr_itsaholdup = world.get_entrance("Start Level - LRRR - It's A Hold Up")
        world.set_rule(entrance_lrrr_itsaholdup, (rule_can_build_orerefinery & (rule_can_lase | rule_can_swim | rule_can_jump | Has("Item Unlock: Dynamite")) & Has("Level Access: LRRR - It's A Hold Up")))
        if world.options.crystal_targets_are_locations:
            location_crystals_lrrr_itsaholdup = world.get_location("Crystal Target: LRRR - It's A Hold Up")
            world.set_rule(location_crystals_lrrr_itsaholdup, (rule_can_blast & (rule_can_swim | rule_can_jump) & (rule_can_fly | rule_can_jump | rule_can_lase)))
        if world.options.victory_condition == 2:
            event_crystals_lrrr_itsaholdup = world.get_location("Crystal Target Beatable: LRRR - It's A Hold Up")
            world.set_rule(event_crystals_lrrr_itsaholdup, (rule_can_blast & (rule_can_swim | rule_can_jump) & (rule_can_fly | rule_can_jump | rule_can_lase)))
    if world.options.level_selection_lrrr_lakeoffire:
        entrance_lrrr_lakeoffire = world.get_entrance("Start Level - LRRR - Lake Of Fire")
        world.set_rule(entrance_lrrr_lakeoffire, (rule_can_breathe & rule_can_flying_lase & Has("Level Access: LRRR - Lake Of Fire")))
        if world.options.crystal_targets_are_locations:
            location_crystals_lrrr_lakeoffire = world.get_location("Crystal Target: LRRR - Lake Of Fire")
            world.set_rule(location_crystals_lrrr_lakeoffire, (rule_can_build_granitegrinder | (rule_can_build_hoverscout & rule_can_build_toolstore & Has("Item Unlock: Dynamite"))))
        if world.options.victory_condition == 2:
            event_crystals_lrrr_lakeoffire = world.get_location("Crystal Target Beatable: LRRR - Lake Of Fire")
            world.set_rule(event_crystals_lrrr_lakeoffire, (rule_can_build_granitegrinder | (rule_can_build_hoverscout & rule_can_build_toolstore & Has("Item Unlock: Dynamite"))))
    if world.options.level_selection_lrrr_lavalaughter:
        entrance_lrrr_lavalaughter = world.get_entrance("Start Level - LRRR - Lava Laughter")
        world.set_rule(entrance_lrrr_lavalaughter, (rule_can_breathe & Has("Level Access: LRRR - Lava Laughter")))
        if world.options.crystal_targets_are_locations:
            location_crystals_lrrr_lavalaughter = world.get_location("Crystal Target: LRRR - Lava Laughter")
            world.set_rule(location_crystals_lrrr_lavalaughter, rule_can_blast)
        if world.options.victory_condition == 2:
            event_crystals_lrrr_lavalaughter = world.get_location("Crystal Target Beatable: LRRR - Lava Laughter")
            world.set_rule(event_crystals_lrrr_lavalaughter, rule_can_blast)
    if world.options.level_selection_lrrr_oresome:
        entrance_lrrr_oresome = world.get_entrance("Start Level - LRRR - Oresome")
        world.set_rule(entrance_lrrr_oresome, (rule_can_breathe & rule_can_build_upgradestation & Has("Level Access: LRRR - Oresome")))
        if world.options.crystal_targets_are_locations:
            location_crystals_lrrr_oresome = world.get_location("Crystal Target: LRRR - Oresome")
            world.set_rule(location_crystals_lrrr_oresome, (rule_can_blast & rule_can_fly & rule_can_lase))
        if world.options.victory_condition == 2:
            event_crystals_lrrr_oresome = world.get_location("Crystal Target Beatable: LRRR - Oresome")
            world.set_rule(event_crystals_lrrr_oresome, (rule_can_blast & rule_can_fly & rule_can_lase))
    if world.options.level_selection_lrrr_rockhard:
        entrance_lrrr_rockhard = world.get_entrance("Start Level - LRRR - Rock Hard")
        world.set_rule(entrance_lrrr_rockhard, ((rule_can_build_smalldigger | rule_can_build_mininglaser | Has("Item Unlock: Dynamite")) & rule_can_breathe & Has("Level Access: LRRR - Rock Hard")))
        if world.options.crystal_targets_are_locations:
            location_crystals_lrrr_rockhard = world.get_location("Crystal Target: LRRR - Rock Hard")
            world.set_rule(location_crystals_lrrr_rockhard, (rule_can_swim & rule_can_lase))
        if world.options.victory_condition == 2:
            event_crystals_lrrr_rockhard = world.get_location("Crystal Target Beatable: LRRR - Rock Hard")
            world.set_rule(event_crystals_lrrr_rockhard, (rule_can_swim & rule_can_lase))
    if world.options.level_selection_lrrr_rockyhorror:
        entrance_lrrr_rockyhorror = world.get_entrance("Start Level - LRRR - Rocky Horror")
        world.set_rule(entrance_lrrr_rockyhorror, (rule_can_breathe & rule_can_build_toolstore & rule_can_build_canteen & Has("Vehicle Unlock: Small Transport Truck") & Has("Level Access: LRRR - Rocky Horror") & Has("Transporter Coordinates",world.options.target_level_count.value,options=[OptionFilter(ManicMiners_Options.BossLevelLRRRRockyHorror,1)],filtered_resolution=True)))
        if world.options.crystal_targets_are_locations and world.options.boss_level_lrrr_rockyhorror == 0:
            location_crystals_lrrr_rockyhorror = world.get_location("Crystal Target: LRRR - Rocky Horror")
            world.set_rule(location_crystals_lrrr_rockyhorror, rule_can_flying_lase)
        if world.options.victory_condition == 2:
            event_crystals_lrrr_rockyhorror = world.get_location("Crystal Target Beatable: LRRR - Rocky Horror")
            world.set_rule(event_crystals_lrrr_rockyhorror, rule_can_flying_lase)
    if world.options.level_selection_lrrr_rubbletrouble:
        entrance_lrrr_rubbletrouble = world.get_entrance("Start Level - LRRR - Rubble Trouble")
        world.set_rule(entrance_lrrr_rubbletrouble, (Has("Building Unlock: Tool Store") & Has("Level Access: LRRR - Rubble Trouble")))
        if world.options.crystal_targets_are_locations:
            location_crystals_lrrr_rubbletrouble = world.get_location("Crystal Target: LRRR - Rubble Trouble")
            world.set_rule(location_crystals_lrrr_rubbletrouble, rule_can_blast)
        if world.options.victory_condition == 2:
            event_crystals_lrrr_rubbletrouble = world.get_location("Crystal Target Beatable: LRRR - Rubble Trouble")
            world.set_rule(event_crystals_lrrr_rubbletrouble, rule_can_blast)
    if world.options.level_selection_lrrr_runthegauntlet:
        entrance_lrrr_runthegauntlet = world.get_entrance("Start Level - LRRR - Run The Gauntlet")
        world.set_rule(entrance_lrrr_runthegauntlet, Has("Level Access: LRRR - Run The Gauntlet"))
    if world.options.level_selection_lrrr_searchandrescue:
        entrance_lrrr_searchandrescue = world.get_entrance("Start Level - LRRR - Search And Rescue")
        world.set_rule(entrance_lrrr_searchandrescue, (rule_can_build_rapidrider | (rule_can_build_tunnelscout & rule_can_build_upgradestation) | (rule_can_build_smlc & rule_can_build_cargocarrier)) & Has("Level Access: LRRR - Search And Rescue"))
        if world.options.crystal_targets_are_locations:
            location_crystals_lrrr_searchandrescue = world.get_location("Crystal Target: LRRR - Search And Rescue")
            world.set_rule(location_crystals_lrrr_searchandrescue, (rule_can_build_rapidrider & rule_can_blast))
        if world.options.victory_condition == 2:
            event_crystals_lrrr_searchandrescue = world.get_location("Crystal Target Beatable: LRRR - Search And Rescue")
            world.set_rule(event_crystals_lrrr_searchandrescue, (rule_can_build_rapidrider & rule_can_blast))
    if world.options.level_selection_lrrr_splitdownthemiddle:
        entrance_lrrr_splitdownthemiddle = world.get_entrance("Start Level - LRRR - Split Down The Middle")
        world.set_rule(entrance_lrrr_splitdownthemiddle, ((Has("Item Unlock: Dynamite") | rule_can_build_smlc) & Has("Level Access: LRRR - Split Down The Middle")))
        if world.options.crystal_targets_are_locations:
            location_crystals_lrrr_splitdownthemiddle = world.get_location("Crystal Target: LRRR - Split Down The Middle")
            world.set_rule(location_crystals_lrrr_splitdownthemiddle, (rule_can_build_tunneltransport & rule_can_build_smlc))
        if world.options.victory_condition == 2:
            event_crystals_lrrr_splitdownthemiddle = world.get_location("Crystal Target Beatable: LRRR - Split Down The Middle")
            world.set_rule(event_crystals_lrrr_splitdownthemiddle, (rule_can_build_tunneltransport & rule_can_build_smlc))
    if world.options.level_selection_lrrr_thepathtopower:
        entrance_lrrr_thepathtopower = world.get_entrance("Start Level - LRRR - The Path To Power")
        world.set_rule(entrance_lrrr_thepathtopower, (rule_can_build_powerstation & Has("Item Unlock: Electric Fence") & Has("Level Access: LRRR - The Path To Power")))
        if world.options.crystal_targets_are_locations:
            location_crystals_lrrr_thepathtopower = world.get_location("Crystal Target: LRRR - The Path To Power")
            world.set_rule(location_crystals_lrrr_thepathtopower, (rule_can_blast & rule_can_swimdrill))
        if world.options.victory_condition == 2:
            event_crystals_lrrr_thepathtopower = world.get_location("Crystal Target Beatable: LRRR - The Path To Power")
            world.set_rule(event_crystals_lrrr_thepathtopower, (rule_can_blast & rule_can_swimdrill))
    if world.options.level_selection_lrrr_waterlotoffun:
        entrance_lrrr_waterlotoffun = world.get_entrance("Start Level - LRRR - Water Lot Of Fun")
        world.set_rule(entrance_lrrr_waterlotoffun, (rule_can_build_docks & (rule_can_build_rapidrider | rule_can_build_tunnelscout) & Has("Item Unlock: Dynamite") & Has("Building Unlock: Tool Store") & Has("Level Access: LRRR - Water Lot Of Fun") & rule_can_always_breathe))
    if world.options.level_selection_lrrr_waterworks:
        entrance_lrrr_waterworks = world.get_entrance("Start Level - LRRR - Water Works")   
        world.set_rule(entrance_lrrr_waterworks, (rule_can_build_docks & (rule_can_build_toolstore | rule_can_build_tunneltransport) & (rule_can_build_tunnelscout | rule_can_build_rapidrider) & Has("Level Access: LRRR - Water Works")))
        if world.options.crystal_targets_are_locations:
            location_crystals_lrrr_waterworks = world.get_location("Crystal Target: LRRR - Water Works")
            world.set_rule(location_crystals_lrrr_waterworks, (rule_can_blast & rule_can_swimdrill))
        if world.options.victory_condition == 2:
            event_crystals_lrrr_waterworks = world.get_location("Crystal Target Beatable: LRRR - Water Works")
            world.set_rule(event_crystals_lrrr_waterworks, (rule_can_blast & rule_can_swimdrill))
    
    if world.options.level_selection_lrrc_abreathoffreshair:
        entrance_lrrc_abreathoffreshair = world.get_entrance("Start Level - LRRC - A Breath Of Fresh Air")
        world.set_rule(entrance_lrrc_abreathoffreshair, (rule_can_breathe & Has("Level Access: LRRC - A Breath Of Fresh Air")))
    if world.options.level_selection_lrrc_airraiders:
        entrance_lrrc_airraiders = world.get_entrance("Start Level - LRRC - Air Raiders")
        world.set_rule(entrance_lrrc_airraiders, Has("Level Access: LRRC - Air Raiders"))
    if world.options.level_selection_lrrc_backtobasics:
        entrance_lrrc_backtobasics = world.get_entrance("Start Level - LRRC - Back To Basics")
        world.set_rule(entrance_lrrc_backtobasics, (rule_can_breathe & Has("Level Access: LRRC - Back To Basics")))
        if world.options.crystal_targets_are_locations:
            location_crystals_lrrc_backtobasics = world.get_location("Crystal Target: LRRC - Back To Basics")
            world.set_rule(location_crystals_lrrc_backtobasics, (rule_can_swim & rule_can_blast))
        if world.options.victory_condition == 2:
            event_crystals_lrrc_backtobasics = world.get_location("Crystal Target Beatable: LRRC - Back To Basics")
            world.set_rule(event_crystals_lrrc_backtobasics, (rule_can_swim & rule_can_blast))
    if world.options.level_selection_lrrc_breathless:
        entrance_lrrc_breathless = world.get_entrance("Start Level - LRRC - Breathless")
        world.set_rule(entrance_lrrc_breathless, ((Has("Item Unlock: Dynamite") | rule_can_build_smalldigger | rule_can_build_granitegrinder | rule_can_build_mininglaser | rule_can_build_smlc) & Has("Level Access: LRRC - Breathless") & rule_can_always_breathe))
        if world.options.crystal_targets_are_locations:
            location_crystals_lrrc_breathless = world.get_location("Crystal Target: LRRC - Breathless")
            world.set_rule(location_crystals_lrrc_breathless, (Has("Item Unlock: Dynamite") | rule_can_build_mininglaser | rule_can_build_smalldigger | rule_can_build_smlc | rule_can_build_granitegrinder))
        if world.options.victory_condition == 2:
            event_crystals_lrrc_breathless = world.get_location("Crystal Target Beatable: LRRC - Breathless")
            world.set_rule(event_crystals_lrrc_breathless, (Has("Item Unlock: Dynamite") | rule_can_build_mininglaser | rule_can_build_smalldigger | rule_can_build_smlc | rule_can_build_granitegrinder))
    if world.options.level_selection_lrrc_dontpanic:
        entrance_lrrc_dontpanic = world.get_entrance("Start Level - LRRC - Don't Panic")
        world.set_rule(entrance_lrrc_dontpanic, Has("Level Access: LRRC - Don't Panic"))
    if world.options.level_selection_lrrc_drillernight:
        entrance_lrrc_drillernight = world.get_entrance("Start Level - LRRC - Driller Night")
        world.set_rule(entrance_lrrc_drillernight, Has("Level Access: LRRC - Driller Night"))
    if world.options.level_selection_lrrc_erodeworks:
        entrance_lrrc_erodeworks = world.get_entrance("Start Level - LRRC - Erode Works")
        world.set_rule(entrance_lrrc_erodeworks, (rule_can_blast & Has("Level Access: LRRC - Erode Works")))
    if world.options.level_selection_lrrc_explosiveaction:
        entrance_lrrc_explosiveaction = world.get_entrance("Start Level - LRRC - Explosive Action")
        world.set_rule(entrance_lrrc_explosiveaction, ((rule_can_build_smalldigger | rule_can_build_mininglaser | Has("Item Unlock: Dynamite")) & rule_can_build_supportstation & Has("Level Access: LRRC - Explosive Action")))
        if world.options.crystal_targets_are_locations:
            location_crystals_lrrc_explosiveaction = world.get_location("Crystal Target: LRRC - Explosive Action")
            world.set_rule(location_crystals_lrrc_explosiveaction, (rule_can_build_rapidrider | (rule_can_build_mininglaser & rule_can_build_tunneltransport)))
        if world.options.victory_condition == 2:
            event_crystals_lrrc_explosiveaction = world.get_location("Crystal Target Beatable: LRRC - Explosive Action")
            world.set_rule(event_crystals_lrrc_explosiveaction, (rule_can_build_rapidrider | (rule_can_build_mininglaser & rule_can_build_tunneltransport)))
    if world.options.level_selection_lrrc_fireandwater:
        entrance_lrrc_fireandwater = world.get_entrance("Start Level - LRRC - Fire And Water")
        world.set_rule(entrance_lrrc_fireandwater, (rule_can_breathe & rule_can_swim & (rule_can_build_toolstore | rule_can_build_tunneltransport) & Has("Level Access: LRRC - Fire And Water")))
    if world.options.level_selection_lrrc_frozenfrenzy:
        entrance_lrrc_frozenfrenzy = world.get_entrance("Start Level - LRRC - Frozen Frenzy")
        world.set_rule(entrance_lrrc_frozenfrenzy, (rule_can_blast & Has("Level Access: LRRC - Frozen Frenzy") & rule_can_always_breathe))
    if world.options.level_selection_lrrc_hotstuff:
        entrance_lrrc_hotstuff = world.get_entrance("Start Level - LRRC - Hot Stuff")
        world.set_rule(entrance_lrrc_hotstuff, (rule_can_breathe & Has("Level Access: LRRC - Hot Stuff")))
        if world.options.crystal_targets_are_locations:
            location_crystals_lrrc_hotstuff = world.get_location("Crystal Target: LRRC - Hot Stuff")
            world.set_rule(location_crystals_lrrc_hotstuff, rule_can_flying_lase)
        if world.options.victory_condition == 2:
            event_crystals_lrrc_hotstuff = world.get_location("Crystal Target Beatable: LRRC - Hot Stuff")
            world.set_rule(event_crystals_lrrc_hotstuff, rule_can_flying_lase)
    if world.options.level_selection_lrrc_icespy:
        entrance_lrrc_icespy = world.get_entrance("Start Level - LRRC - Ice Spy")
        world.set_rule(entrance_lrrc_icespy, (Has("Level Access: LRRC - Ice Spy") & rule_can_always_breathe))
    if world.options.level_selection_lrrc_itsaholdup:
        entrance_lrrc_itsaholdup = world.get_entrance("Start Level - LRRC - It's A Hold Up")
        world.set_rule(entrance_lrrc_itsaholdup, Has("Level Access: LRRC - It's A Hold Up"))
        if world.options.crystal_targets_are_locations:
            location_crystals_lrrc_itsaholdup = world.get_location("Crystal Target: LRRC - It's A Hold Up")
            world.set_rule(location_crystals_lrrc_itsaholdup, (Has("Item Unlock: Dynamite") | rule_can_build_smlc | rule_can_build_smalldigger | rule_can_build_mininglaser))
        if world.options.victory_condition == 2:
            event_crystals_lrrc_itsaholdup = world.get_location("Crystal Target Beatable: LRRC - It's A Hold Up")
            world.set_rule(event_crystals_lrrc_itsaholdup, (Has("Item Unlock: Dynamite") | rule_can_build_smlc | rule_can_build_smalldigger | rule_can_build_mininglaser))
    if world.options.level_selection_lrrc_lakeoffire:
        entrance_lrrc_lakeoffire = world.get_entrance("Start Level - LRRC - Lake Of Fire")
        world.set_rule(entrance_lrrc_lakeoffire, Has("Level Access: LRRC - Lake Of Fire"))
        if world.options.crystal_targets_are_locations:
            location_crystals_lrrc_lakeoffire = world.get_location("Crystal Target: LRRC - Lake Of Fire")
            world.set_rule(location_crystals_lrrc_lakeoffire, rule_can_flying_lase)
        if world.options.victory_condition == 2:
            event_crystals_lrrc_lakeoffire = world.get_location("Crystal Target Beatable: LRRC - Lake Of Fire")
            world.set_rule(event_crystals_lrrc_lakeoffire, rule_can_flying_lase)
    if world.options.level_selection_lrrc_lavalaughter:
        entrance_lrrc_lavalaughter = world.get_entrance("Start Level - LRRC - Lava Laughter")
        world.set_rule(entrance_lrrc_lavalaughter, (Has("Level Access: LRRC - Lava Laughter") & rule_can_always_breathe))
        if world.options.crystal_targets_are_locations:
            location_crystals_lrrc_lavalaughter = world.get_location("Crystal Target: LRRC - Lava Laughter")
            world.set_rule(location_crystals_lrrc_lavalaughter, rule_can_breathe)
        if world.options.victory_condition == 2:
            event_crystals_lrrc_lavalaughter = world.get_location("Crystal Target Beatable: LRRC - Lava Laughter")
            world.set_rule(event_crystals_lrrc_lavalaughter, rule_can_breathe)
    if world.options.level_selection_lrrc_oresome:
        entrance_lrrc_oresome = world.get_entrance("Start Level - LRRC - Oresome")
        world.set_rule(entrance_lrrc_oresome, Has("Level Access: LRRC - Oresome"))
    if world.options.level_selection_lrrc_rockhard:
        entrance_lrrc_rockhard = world.get_entrance("Start Level - LRRC - Rock Hard")
        world.set_rule(entrance_lrrc_rockhard, (rule_can_blast & Has("Level Access: LRRC - Rock Hard") & rule_can_always_breathe))
        if world.options.crystal_targets_are_locations:
            location_crystals_lrrc_rockhard = world.get_location("Crystal Target: LRRC - Rock Hard")
            world.set_rule(location_crystals_lrrc_rockhard, rule_can_swim)
        if world.options.victory_condition == 2:
            event_crystals_lrrc_rockhard = world.get_location("Crystal Target Beatable: LRRC - Rock Hard")
            world.set_rule(event_crystals_lrrc_rockhard, rule_can_swim)
    if world.options.level_selection_lrrc_rockyhorror:
        entrance_lrrc_rockyhorror = world.get_entrance("Start Level - LRRC - Rocky Horror")
        world.set_rule(entrance_lrrc_rockyhorror, (rule_can_breathe & Has("Level Access: LRRC - Rocky Horror") & Has("Transporter Coordinates",world.options.target_level_count.value,options=[OptionFilter(ManicMiners_Options.BossLevelLRRCRockyHorror,1)],filtered_resolution=True)))
        if world.options.crystal_targets_are_locations and world.options.boss_level_lrrc_rockyhorror == 0:
            location_crystals_lrrc_rockyhorror = world.get_location("Crystal Target: LRRC - Rocky Horror")
            world.set_rule(location_crystals_lrrc_rockyhorror, rule_can_blast)
        if world.options.victory_condition == 2:
            event_crystals_lrrc_rockyhorror = world.get_location("Crystal Target Beatable: LRRC - Rocky Horror")
            world.set_rule(event_crystals_lrrc_rockyhorror, rule_can_blast)
    if world.options.level_selection_lrrc_rubbletrouble:
        entrance_lrrc_rubbletrouble = world.get_entrance("Start Level - LRRC - Rubble Trouble")
        world.set_rule(entrance_lrrc_rubbletrouble, Has("Level Access: LRRC - Rubble Trouble"))
    if world.options.level_selection_lrrc_runthegauntlet:
        entrance_lrrc_runthegauntlet = world.get_entrance("Start Level - LRRC - Run The Gauntlet")
        world.set_rule(entrance_lrrc_runthegauntlet, Has("Level Access: LRRC - Run The Gauntlet"))
    if world.options.level_selection_lrrc_searchandrescue:
        entrance_lrrc_searchandrescue = world.get_entrance("Start Level - LRRC - Search And Rescue")
        world.set_rule(entrance_lrrc_searchandrescue, (rule_can_swim & Has("Level Access: LRRC - Search And Rescue")))
        if world.options.crystal_targets_are_locations:
            location_crystals_lrrc_searchandrescue = world.get_location("Crystal Target: LRRC - Search And Rescue")
            world.set_rule(location_crystals_lrrc_searchandrescue, (rule_can_swimdrill & rule_can_blast))
        if world.options.victory_condition == 2:
            event_crystals_lrrc_searchandrescue = world.get_location("Crystal Target Beatable: LRRC - Search And Rescue")
            world.set_rule(event_crystals_lrrc_searchandrescue, (rule_can_swimdrill & rule_can_blast))
    if world.options.level_selection_lrrc_splitdownthemiddle:
        entrance_lrrc_splitdownthemiddle = world.get_entrance("Start Level - LRRC - Split Down The Middle")
        world.set_rule(entrance_lrrc_splitdownthemiddle, Has("Level Access: LRRC - Split Down The Middle"))
    if world.options.level_selection_lrrc_thepathtopower:
        entrance_lrrc_thepathtopower = world.get_entrance("Start Level - LRRC - The Path To Power")
        world.set_rule(entrance_lrrc_thepathtopower, (rule_can_build_powerstation & Has("Level Access: LRRC - The Path To Power")))
        if world.options.crystal_targets_are_locations:
            location_crystals_lrrc_thepathtopower = world.get_location("Crystal Target: LRRC - The Path To Power")
            world.set_rule(location_crystals_lrrc_thepathtopower, (Has("Item Unlock: Dynamite") | rule_can_build_smlc | rule_can_build_smalldigger | rule_can_build_mininglaser))
        if world.options.victory_condition == 2:
            event_crystals_lrrc_thepathtopower = world.get_location("Crystal Target Beatable: LRRC - The Path To Power")
            world.set_rule(event_crystals_lrrc_thepathtopower, (Has("Item Unlock: Dynamite") | rule_can_build_smlc | rule_can_build_smalldigger | rule_can_build_mininglaser))
    if world.options.level_selection_lrrc_waterlotoffun:
        entrance_lrrc_waterlotoffun = world.get_entrance("Start Level - LRRC - Water Lot Of Fun")
        world.set_rule(entrance_lrrc_waterlotoffun, ((rule_can_build_smalldigger | rule_can_build_mininglaser | rule_can_build_smlc | Has("Item Unlock: Dynamite") | rule_can_build_cargocarrier | rule_can_build_rapidrider | rule_can_build_tunnelscout) & Has("Level Access: LRRC - Water Lot Of Fun") & rule_can_always_breathe))
        if world.options.crystal_targets_are_locations:
            location_crystals_lrrc_waterlotoffun = world.get_location("Crystal Target: LRRC - Water Lot Of Fun")
            world.set_rule(location_crystals_lrrc_waterlotoffun, (rule_can_breathe & rule_can_blast & (rule_can_build_cargocarrier | rule_can_build_rapidrider)))
        if world.options.victory_condition == 2:
            event_crystals_lrrc_waterlotoffun = world.get_location("Crystal Target Beatable: LRRC - Water Lot Of Fun")
            world.set_rule(event_crystals_lrrc_waterlotoffun, (rule_can_breathe & rule_can_blast & (rule_can_build_cargocarrier | rule_can_build_rapidrider)))
    if world.options.level_selection_lrrc_waterworks:
        entrance_lrrc_waterworks = world.get_entrance("Start Level - LRRC - Water Works")
        world.set_rule(entrance_lrrc_waterworks, (Has("Level Access: LRRC - Water Works") & rule_can_always_breathe))
        if world.options.crystal_targets_are_locations:
            location_crystals_lrrc_waterworks = world.get_location("Crystal Target: LRRC - Water Works")
            world.set_rule(location_crystals_lrrc_waterworks, rule_can_swim)
        if world.options.victory_condition == 2:
            event_crystals_lrrc_waterworks = world.get_location("Crystal Target Beatable: LRRC - Water Works")
            world.set_rule(event_crystals_lrrc_waterworks, rule_can_swim)
    
    goal_achievable = world.get_location("Goal Conditions Achievable")
    if world.options.victory_condition == 0:
        world.set_rule(goal_achievable, Has("Level Completed", world.options.target_level_count.value))
    elif world.options.victory_condition == 1:
        world.set_rule(goal_achievable, Has("Par Time Beaten", world.options.target_level_count.value))
    elif world.options.victory_condition == 2:
        world.set_rule(goal_achievable, Has("Crystal Target Beaten", world.options.target_level_count.value))
    elif world.options.victory_condition == 3:
        if world.options.boss_level_lrr_rockyhorror:
            world.set_rule(goal_achievable, CanReachRegion("LRR - Rocky Horror"))
        elif world.options.boss_level_lrrr_rockyhorror:
            world.set_rule(goal_achievable, CanReachRegion("LRRR - Rocky Horror"))
        elif world.options.boss_level_lrrc_rockyhorror:
            world.set_rule(goal_achievable, CanReachRegion("LRRC - Rocky Horror"))
    
def set_completion_condition(world: ManicMinersWorld) -> None:
    world.set_completion_rule(Has("Victory"))
