from collections.abc import Mapping
from typing import Any

import settings

from worlds.AutoWorld import World

from . import Items, Locations, Regions, Rules
from . import Options as ManicMiners_Options

class ManicMinersSettings(settings.Group):
    class ManicMinersInstallDirectory(settings.UserFolderPath):
        """The directory that contains your Manic Miners installation, i.e. the directory containing ManicMiners.exe. Needed for base copy of the levels."""
        description = "Manic Miners Install Directory"
    
    class ManicMinersLevelDirectory(settings.UserFolderPath):
        """The directory that contains your Manic Miners custom levels, i.e. ..../YourUser/Documents/ManicMiners. Needed for inserting Archipelago's copy of the levels."""
        description = "Manic Miners Level Directory"

    class ManicMinersSaveDirectory(settings.UserFolderPath):
        """The directory that contains your Manic Miners save files under Wine, e.g. ..../users/steamuser/AppData/Local/ManicMiners/Saved/SaveGames/Profiles. Needed for reading save file data, on Linux only."""
        description = "Manic Miners Save Directory"

    manic_miners_install_dir: ManicMinersInstallDirectory = ManicMinersInstallDirectory("ManicMiners")
    manic_miners_level_dir: ManicMinersLevelDirectory = ManicMinersLevelDirectory("ManicMiners")
    manic_miners_save_dir: ManicMinersSaveDirectory = ManicMinersSaveDirectory("ManicMiners")

class ManicMinersWorld(World):
    """
    Manic Miners is a fan-made remake of the cult classic LEGO Rock Raiders.
    
    This APWorld allows Manic Miners to be combined with the Archipelago multiworld randomizer software, as you play through the campaign in a random order and with building or vehicle restrictions.
    """
    
    game = "Manic Miners"
    
    options_dataclass = ManicMiners_Options.ManicMinersOptions
    options: ManicMiners_Options.ManicMinersOptions
    
    settings: ManicMinersSettings
    
    location_name_to_id = Locations.LOCATION_NAME_TO_ID
    item_name_to_id = Items.ITEM_NAME_TO_ID
    
    origin_region_name = "Menu"
    
    def generate_early(self) -> None:
        # Fix some potentially fatal option combinations
        
        # Must have at least one campaign selected, default to LRR if all unticked
        if ((self.options.campaign_selection_lrr == 0) & (self.options.campaign_selection_lrrr == 0) & (self.options.campaign_selection_lrrc == 0)):
            self.options.campaign_selection_lrr.value = 1
        
        # Identify number of levels and locations for clearing
        number_levels = 0
        number_locations = 0
        
        if self.options.campaign_selection_lrr:
            number_levels += 25
            number_locations += 25
            if self.options.bonus_clear_locations:
                number_locations += 56
        
        if self.options.campaign_selection_lrrr:
            number_levels += 25
            number_locations += 25
            if self.options.bonus_clear_locations:
                number_locations += 56

        if self.options.campaign_selection_lrrc:
            number_levels += 25
            number_locations += 25
            if self.options.bonus_clear_locations:
                number_locations += 56

        # if self.options.campaign_selection_baz:
            # number_levels += 33
            # number_locations += 33
            # if self.options.bonus_clear_locations:
                # number_locations += ???
        
        # Select levels
        if self.options.no_duplicate_levels == 0:
            if self.options.campaign_selection_lrr:
                self.options.level_selection_lrr_abreathoffreshair.value = 1
                self.options.level_selection_lrr_airraiders.value = 1
                self.options.level_selection_lrr_backtobasics.value = 1
                self.options.level_selection_lrr_breathless.value = 1
                self.options.level_selection_lrr_dontpanic.value = 1
                self.options.level_selection_lrr_drillernight.value = 1
                self.options.level_selection_lrr_erodeworks.value = 1
                self.options.level_selection_lrr_explosiveaction.value = 1
                self.options.level_selection_lrr_fireandwater.value = 1
                self.options.level_selection_lrr_frozenfrenzy.value = 1
                self.options.level_selection_lrr_hotstuff.value = 1
                self.options.level_selection_lrr_icespy.value = 1
                self.options.level_selection_lrr_itsaholdup.value = 1
                self.options.level_selection_lrr_lakeoffire.value = 1
                self.options.level_selection_lrr_lavalaughter.value = 1
                self.options.level_selection_lrr_oresome.value = 1
                self.options.level_selection_lrr_rockhard.value = 1
                self.options.level_selection_lrr_rockyhorror.value = 1
                self.options.level_selection_lrr_rubbletrouble.value = 1
                self.options.level_selection_lrr_runthegauntlet.value = 1
                self.options.level_selection_lrr_searchandrescue.value = 1
                self.options.level_selection_lrr_splitdownthemiddle.value = 1
                self.options.level_selection_lrr_thepathtopower.value = 1
                self.options.level_selection_lrr_waterlotoffun.value = 1
                self.options.level_selection_lrr_waterworks.value = 1

            if self.options.campaign_selection_lrrr:
                self.options.level_selection_lrrr_abreathoffreshair.value = 1
                self.options.level_selection_lrrr_airraiders.value = 1
                self.options.level_selection_lrrr_backtobasics.value = 1
                self.options.level_selection_lrrr_breathless.value = 1
                self.options.level_selection_lrrr_dontpanic.value = 1
                self.options.level_selection_lrrr_drillernight.value = 1
                self.options.level_selection_lrrr_erodeworks.value = 1
                self.options.level_selection_lrrr_explosiveaction.value = 1
                self.options.level_selection_lrrr_fireandwater.value = 1
                self.options.level_selection_lrrr_frozenfrenzy.value = 1
                self.options.level_selection_lrrr_hotstuff.value = 1
                self.options.level_selection_lrrr_icespy.value = 1
                self.options.level_selection_lrrr_itsaholdup.value = 1
                self.options.level_selection_lrrr_lakeoffire.value = 1
                self.options.level_selection_lrrr_lavalaughter.value = 1
                self.options.level_selection_lrrr_oresome.value = 1
                self.options.level_selection_lrrr_rockhard.value = 1
                self.options.level_selection_lrrr_rockyhorror.value = 1
                self.options.level_selection_lrrr_rubbletrouble.value = 1
                self.options.level_selection_lrrr_runthegauntlet.value = 1
                self.options.level_selection_lrrr_searchandrescue.value = 1
                self.options.level_selection_lrrr_splitdownthemiddle.value = 1
                self.options.level_selection_lrrr_thepathtopower.value = 1
                self.options.level_selection_lrrr_waterlotoffun.value = 1
                self.options.level_selection_lrrr_waterworks.value = 1

            if self.options.campaign_selection_lrrc:
                self.options.level_selection_lrrc_abreathoffreshair.value = 1
                self.options.level_selection_lrrc_airraiders.value = 1
                self.options.level_selection_lrrc_backtobasics.value = 1
                self.options.level_selection_lrrc_breathless.value = 1
                self.options.level_selection_lrrc_dontpanic.value = 1
                self.options.level_selection_lrrc_drillernight.value = 1
                self.options.level_selection_lrrc_erodeworks.value = 1
                self.options.level_selection_lrrc_explosiveaction.value = 1
                self.options.level_selection_lrrc_fireandwater.value = 1
                self.options.level_selection_lrrc_frozenfrenzy.value = 1
                self.options.level_selection_lrrc_hotstuff.value = 1
                self.options.level_selection_lrrc_icespy.value = 1
                self.options.level_selection_lrrc_itsaholdup.value = 1
                self.options.level_selection_lrrc_lakeoffire.value = 1
                self.options.level_selection_lrrc_lavalaughter.value = 1
                self.options.level_selection_lrrc_oresome.value = 1
                self.options.level_selection_lrrc_rockhard.value = 1
                self.options.level_selection_lrrc_rockyhorror.value = 1
                self.options.level_selection_lrrc_rubbletrouble.value = 1
                self.options.level_selection_lrrc_runthegauntlet.value = 1
                self.options.level_selection_lrrc_searchandrescue.value = 1
                self.options.level_selection_lrrc_splitdownthemiddle.value = 1
                self.options.level_selection_lrrc_thepathtopower.value = 1
                self.options.level_selection_lrrc_waterlotoffun.value = 1
                self.options.level_selection_lrrc_waterworks.value = 1
            
        else:
            number_levels = 25
            number_locations = 25
            if self.options.bonus_clear_locations:
                number_locations += 56
            level_list = []
            if self.options.campaign_selection_lrr:
                level_list.append(self.options.level_selection_lrr_abreathoffreshair)
            if self.options.campaign_selection_lrrr:
                level_list.append(self.options.level_selection_lrrr_abreathoffreshair)
            if self.options.campaign_selection_lrrc:
                level_list.append(self.options.level_selection_lrrc_abreathoffreshair)
            random_index = self.random.randint(0,len(level_list)-1)
            level_list[random_index].value = 1
            level_list.clear()
            if self.options.campaign_selection_lrr:
                level_list.append(self.options.level_selection_lrr_airraiders)
            if self.options.campaign_selection_lrrr:
                level_list.append(self.options.level_selection_lrrr_airraiders)
            if self.options.campaign_selection_lrrc:
                level_list.append(self.options.level_selection_lrrc_airraiders)
            random_index = self.random.randint(0,len(level_list)-1)
            level_list[random_index].value = 1
            level_list.clear()
            if self.options.campaign_selection_lrr:
                level_list.append(self.options.level_selection_lrr_backtobasics)
            if self.options.campaign_selection_lrrr:
                level_list.append(self.options.level_selection_lrrr_backtobasics)
            if self.options.campaign_selection_lrrc:
                level_list.append(self.options.level_selection_lrrc_backtobasics)
            random_index = self.random.randint(0,len(level_list)-1)
            level_list[random_index].value = 1
            level_list.clear()
            if self.options.campaign_selection_lrr:
                level_list.append(self.options.level_selection_lrr_breathless)
            if self.options.campaign_selection_lrrr:
                level_list.append(self.options.level_selection_lrrr_breathless)
            if self.options.campaign_selection_lrrc:
                level_list.append(self.options.level_selection_lrrc_breathless)
            random_index = self.random.randint(0,len(level_list)-1)
            level_list[random_index].value = 1
            level_list.clear()
            if self.options.campaign_selection_lrr:
                level_list.append(self.options.level_selection_lrr_dontpanic)
            if self.options.campaign_selection_lrrr:
                level_list.append(self.options.level_selection_lrrr_dontpanic)
            if self.options.campaign_selection_lrrc:
                level_list.append(self.options.level_selection_lrrc_dontpanic)
            random_index = self.random.randint(0,len(level_list)-1)
            level_list[random_index].value = 1
            level_list.clear()
            if self.options.campaign_selection_lrr:
                level_list.append(self.options.level_selection_lrr_drillernight)
            if self.options.campaign_selection_lrrr:
                level_list.append(self.options.level_selection_lrrr_drillernight)
            if self.options.campaign_selection_lrrc:
                level_list.append(self.options.level_selection_lrrc_drillernight)
            random_index = self.random.randint(0,len(level_list)-1)
            level_list[random_index].value = 1
            level_list.clear()
            if self.options.campaign_selection_lrr:
                level_list.append(self.options.level_selection_lrr_erodeworks)
            if self.options.campaign_selection_lrrr:
                level_list.append(self.options.level_selection_lrrr_erodeworks)
            if self.options.campaign_selection_lrrc:
                level_list.append(self.options.level_selection_lrrc_erodeworks)
            random_index = self.random.randint(0,len(level_list)-1)
            level_list[random_index].value = 1
            level_list.clear()
            if self.options.campaign_selection_lrr:
                level_list.append(self.options.level_selection_lrr_explosiveaction)
            if self.options.campaign_selection_lrrr:
                level_list.append(self.options.level_selection_lrrr_explosiveaction)
            if self.options.campaign_selection_lrrc:
                level_list.append(self.options.level_selection_lrrc_explosiveaction)
            random_index = self.random.randint(0,len(level_list)-1)
            level_list[random_index].value = 1
            level_list.clear()
            if self.options.campaign_selection_lrr:
                level_list.append(self.options.level_selection_lrr_fireandwater)
            if self.options.campaign_selection_lrrr:
                level_list.append(self.options.level_selection_lrrr_fireandwater)
            if self.options.campaign_selection_lrrc:
                level_list.append(self.options.level_selection_lrrc_fireandwater)
            random_index = self.random.randint(0,len(level_list)-1)
            level_list[random_index].value = 1
            level_list.clear()
            if self.options.campaign_selection_lrr:
                level_list.append(self.options.level_selection_lrr_frozenfrenzy)
            if self.options.campaign_selection_lrrr:
                level_list.append(self.options.level_selection_lrrr_frozenfrenzy)
            if self.options.campaign_selection_lrrc:
                level_list.append(self.options.level_selection_lrrc_frozenfrenzy)
            random_index = self.random.randint(0,len(level_list)-1)
            level_list[random_index].value = 1
            level_list.clear()
            if self.options.campaign_selection_lrr:
                level_list.append(self.options.level_selection_lrr_hotstuff)
            if self.options.campaign_selection_lrrr:
                level_list.append(self.options.level_selection_lrrr_hotstuff)
            if self.options.campaign_selection_lrrc:
                level_list.append(self.options.level_selection_lrrc_hotstuff)
            random_index = self.random.randint(0,len(level_list)-1)
            level_list[random_index].value = 1
            level_list.clear()
            if self.options.campaign_selection_lrr:
                level_list.append(self.options.level_selection_lrr_icespy)
            if self.options.campaign_selection_lrrr:
                level_list.append(self.options.level_selection_lrrr_icespy)
            if self.options.campaign_selection_lrrc:
                level_list.append(self.options.level_selection_lrrc_icespy)
            random_index = self.random.randint(0,len(level_list)-1)
            level_list[random_index].value = 1
            level_list.clear()
            if self.options.campaign_selection_lrr:
                level_list.append(self.options.level_selection_lrr_itsaholdup)
            if self.options.campaign_selection_lrrr:
                level_list.append(self.options.level_selection_lrrr_itsaholdup)
            if self.options.campaign_selection_lrrc:
                level_list.append(self.options.level_selection_lrrc_itsaholdup)
            random_index = self.random.randint(0,len(level_list)-1)
            level_list[random_index].value = 1
            level_list.clear()
            if self.options.campaign_selection_lrr:
                level_list.append(self.options.level_selection_lrr_lakeoffire)
            if self.options.campaign_selection_lrrr:
                level_list.append(self.options.level_selection_lrrr_lakeoffire)
            if self.options.campaign_selection_lrrc:
                level_list.append(self.options.level_selection_lrrc_lakeoffire)
            random_index = self.random.randint(0,len(level_list)-1)
            level_list[random_index].value = 1
            level_list.clear()
            if self.options.campaign_selection_lrr:
                level_list.append(self.options.level_selection_lrr_lavalaughter)
            if self.options.campaign_selection_lrrr:
                level_list.append(self.options.level_selection_lrrr_lavalaughter)
            if self.options.campaign_selection_lrrc:
                level_list.append(self.options.level_selection_lrrc_lavalaughter)
            random_index = self.random.randint(0,len(level_list)-1)
            level_list[random_index].value = 1
            level_list.clear()
            if self.options.campaign_selection_lrr:
                level_list.append(self.options.level_selection_lrr_oresome)
            if self.options.campaign_selection_lrrr:
                level_list.append(self.options.level_selection_lrrr_oresome)
            if self.options.campaign_selection_lrrc:
                level_list.append(self.options.level_selection_lrrc_oresome)
            random_index = self.random.randint(0,len(level_list)-1)
            level_list[random_index].value = 1
            level_list.clear()
            if self.options.campaign_selection_lrr:
                level_list.append(self.options.level_selection_lrr_rockhard)
            if self.options.campaign_selection_lrrr:
                level_list.append(self.options.level_selection_lrrr_rockhard)
            if self.options.campaign_selection_lrrc:
                level_list.append(self.options.level_selection_lrrc_rockhard)
            random_index = self.random.randint(0,len(level_list)-1)
            level_list[random_index].value = 1
            level_list.clear()
            if self.options.campaign_selection_lrr:
                level_list.append(self.options.level_selection_lrr_rockyhorror)
            if self.options.campaign_selection_lrrr:
                level_list.append(self.options.level_selection_lrrr_rockyhorror)
            if self.options.campaign_selection_lrrc:
                level_list.append(self.options.level_selection_lrrc_rockyhorror)
            random_index = self.random.randint(0,len(level_list)-1)
            level_list[random_index].value = 1
            level_list.clear()
            if self.options.campaign_selection_lrr:
                level_list.append(self.options.level_selection_lrr_rubbletrouble)
            if self.options.campaign_selection_lrrr:
                level_list.append(self.options.level_selection_lrrr_rubbletrouble)
            if self.options.campaign_selection_lrrc:
                level_list.append(self.options.level_selection_lrrc_rubbletrouble)
            random_index = self.random.randint(0,len(level_list)-1)
            level_list[random_index].value = 1
            level_list.clear()
            if self.options.campaign_selection_lrr:
                level_list.append(self.options.level_selection_lrr_runthegauntlet)
            if self.options.campaign_selection_lrrr:
                level_list.append(self.options.level_selection_lrrr_runthegauntlet)
            if self.options.campaign_selection_lrrc:
                level_list.append(self.options.level_selection_lrrc_runthegauntlet)
            random_index = self.random.randint(0,len(level_list)-1)
            level_list[random_index].value = 1
            level_list.clear()
            if self.options.campaign_selection_lrr:
                level_list.append(self.options.level_selection_lrr_searchandrescue)
            if self.options.campaign_selection_lrrr:
                level_list.append(self.options.level_selection_lrrr_searchandrescue)
            if self.options.campaign_selection_lrrc:
                level_list.append(self.options.level_selection_lrrc_searchandrescue)
            random_index = self.random.randint(0,len(level_list)-1)
            level_list[random_index].value = 1
            level_list.clear()
            if self.options.campaign_selection_lrr:
                level_list.append(self.options.level_selection_lrr_splitdownthemiddle)
            if self.options.campaign_selection_lrrr:
                level_list.append(self.options.level_selection_lrrr_splitdownthemiddle)
            if self.options.campaign_selection_lrrc:
                level_list.append(self.options.level_selection_lrrc_splitdownthemiddle)
            random_index = self.random.randint(0,len(level_list)-1)
            level_list[random_index].value = 1
            level_list.clear()
            if self.options.campaign_selection_lrr:
                level_list.append(self.options.level_selection_lrr_thepathtopower)
            if self.options.campaign_selection_lrrr:
                level_list.append(self.options.level_selection_lrrr_thepathtopower)
            if self.options.campaign_selection_lrrc:
                level_list.append(self.options.level_selection_lrrc_thepathtopower)
            random_index = self.random.randint(0,len(level_list)-1)
            level_list[random_index].value = 1
            level_list.clear()
            if self.options.campaign_selection_lrr:
                level_list.append(self.options.level_selection_lrr_waterlotoffun)
            if self.options.campaign_selection_lrrr:
                level_list.append(self.options.level_selection_lrrr_waterlotoffun)
            if self.options.campaign_selection_lrrc:
                level_list.append(self.options.level_selection_lrrc_waterlotoffun)
            random_index = self.random.randint(0,len(level_list)-1)
            level_list[random_index].value = 1
            level_list.clear()
            if self.options.campaign_selection_lrr:
                level_list.append(self.options.level_selection_lrr_waterworks)
            if self.options.campaign_selection_lrrr:
                level_list.append(self.options.level_selection_lrrr_waterworks)
            if self.options.campaign_selection_lrrc:
                level_list.append(self.options.level_selection_lrrc_waterworks)
            random_index = self.random.randint(0,len(level_list)-1)
            level_list[random_index].value = 1
            level_list.clear()
        
        # Select boss level
        if self.options.victory_condition == 3:
            level_list = []
            if self.options.level_selection_lrr_rockyhorror:
                level_list.append(self.options.boss_level_lrr_rockyhorror)
            if self.options.level_selection_lrrr_rockyhorror:
                level_list.append(self.options.boss_level_lrrr_rockyhorror)
            if self.options.level_selection_lrrc_rockyhorror:
                level_list.append(self.options.boss_level_lrrc_rockyhorror)
            random_index = self.random.randint(0,len(level_list)-1)
            level_list[random_index].value = 1
            level_list.clear()

        # Add locations for par times
        if self.options.target_times_are_locations:
            number_locations += number_levels
        
        # Add locations for crystal targets
        if self.options.crystal_targets_are_locations:
            number_locations += number_levels

        # Can't start with more levels than there are levels
        if self.options.available_levels_at_start >= (number_levels):
            self.options.available_levels_at_start.value = number_levels
            # And -1 again if we get given one free boss level access item for Coordinate Hunt
            if self.options.victory_condition == 3:
                self.options.available_levels_at_start.value -= 1
        
        # Identify number of Items
        number_items = 0
        number_items += number_levels # Level Unlocks
        if self.options.buildings_are_items:
            number_items += 11 # Building Unlocks
        if self.options.items_are_items:
            number_items += 2 # Item Unlocks
        if self.options.vehicles_are_items:
            number_items += 12 # Vehicle Unlocks
        if self.options.bonus_truck:
            number_items += 1 # Chief's Favourite Truck
        number_items -= self.options.available_levels_at_start
        
        # Check we haven't got more Items than Locations, handle if so
        item_location_diffcount = number_items - number_locations
        if item_location_diffcount > 0:
            if self.options.bonus_clear_locations == 0:
                self.options.bonus_clear_locations.value = 1
                if self.options.no_duplicate_levels:
                    number_locations += 56
                else:
                    if self.options.campaign_selection_lrr:
                        number_locations += 56
                    if self.options.campaign_selection_lrrr:
                        number_locations += 56
                    if self.options.campaign_selection_lrrc:
                        number_locations += 56
        item_location_diffcount = number_items - number_locations
        if item_location_diffcount > 0:
            self.options.available_levels_at_start.value += item_location_diffcount

        # If more levels are required than are available, reduce number required
        elif self.options.target_level_count >= number_levels:
            self.options.target_level_count.value = number_levels
            # And -1 again if we need coordinates that were placed on the boss level
            if self.options.victory_condition == 3 and self.options.locked_coordinates:
                self.options.target_level_count.value -= 1
    
    def create_regions(self) -> None:
        Regions.create_and_connect_regions(self)
        Locations.create_all_locations(self)
    
    def set_rules(self) -> None:
        Rules.set_all_rules(self)
        
    def create_items(self) -> None:
        Items.create_all_items(self)
        
    def create_item(self, name: str) -> Items.ManicMinersItem:
        return Items.create_item_with_correct_classification(self, name)

    def get_filler_item_name(self) -> str:
        return Items.get_random_filler_item_name(self)
    
    def fill_slot_data(self) -> Mapping[str, Any]:
        return self.options.as_dict(
        # "victory_condition", "target_level_count", "target_times_are_locations", "target_time_difficulty", "buildings_are_items", "items_are_items", "vehicles_are_items", "campaign_selection_lrr", "campaign_selection_lrrr", "campaign_selection_lrrc", "campaign_selection_baz"
        "victory_condition", "locked_coordinates", "target_level_count", "target_times_are_locations", "target_time_difficulty", "crystal_targets_are_locations", "crystal_target_percentage", "buildings_are_items", "items_are_items", "vehicles_are_items", "bonus_clear_locations", "campaign_selection_lrr", "campaign_selection_lrrr", "campaign_selection_lrrc", "no_duplicate_levels", "boss_level_lrr_rockyhorror", "boss_level_lrrr_rockyhorror", "boss_level_lrrc_rockyhorror"
        )

def launch_client(*args):
    from .Client import launch
    from worlds.LauncherComponents import launch as launch_component
    launch_component(launch, name="Manic Miners Client", args=args)

from worlds.LauncherComponents import Component, components, Type, launch as launch_component, icon_paths
components.append(Component("Manic Miners Client", 
                           game_name="Manic Miners", 
                           func=launch_client, 
                           component_type=Type.CLIENT,
                           icon="manic_miners_logo"))

icon_paths["manic_miners_logo"] = f"ap:{__name__}/icons/manic_miners_logo.png"
