import json
import god
import ability
import re


# ? == Region: Load God Information

def load_god_information(current_god) -> god.GodInformation:
    """Loads in the information for given god"""
    current_information = None
    try:
        type_list = current_god["Type"].split(", ")
        current_information = god.GodInformation(current_god["Name"], current_god["id"], current_god["Title"], 
                                                 current_god["Roles"], type_list[0], type_list[1], current_god["Pantheon"])
    
    # Persephone had an ongoing issue with her classifications as "Magical, Ranged". Should also cover edge cases for now just in case
    except IndexError:
        current_information = god.GodInformation(current_god["Name"], current_god["id"], current_god["Title"], 
                                                 current_god["Roles"], type_list[0], "Ranged", current_god["Pantheon"])
    
    return current_information

# ? == Load God Information End


# ? == Region: Load Base Stats

def load_base_stats(current_god) -> list:
    """Loads in all base stats for a given god"""
    
    # ! Currently have to manually load in base stat names for pairs
    stat_pairs = {
        'Health':'HealthPerLevel',
        'HealthPerFive':'HP5PerLevel',
        'Mana':'ManaPerLevel',
        'ManaPerFive':'MP5PerLevel',
        'Speed':0.3,
        'AttackSpeed':'AttackSpeedPerLevel',
        'PhysicalPower':'PhysicalPowerPerLevel',
        'MagicalPower':'MagicalPowerPerLevel',
        'PhysicalProtection':'PhysicalProtectionPerLevel',
        'MagicalProtection':'MagicalProtectionPerLevel'
    }
    
    all_base_stats = []
    
    for key in stat_pairs.keys():
        # Speed is the only case but in case there is more in the future
        if type(stat_pairs.get(key)) != str:
            current_stat = god.GodBaseStat(key, current_god[key], stat_pairs.get(key))
            all_base_stats.append(current_stat)
        
        else:
            current_stat = god.GodBaseStat(key, current_god[key], current_god[stat_pairs.get(key)])
            all_base_stats.append(current_stat)
    
    return all_base_stats

# ? == Load Base Stats End

class LoadGod:
    # Might be good to generalize this into a generalized loader class
    def __init__(self, god_file):
        self.god_file = god_file
        
    
    '''
        This function performs regex for the auto_attack section and returns the information as a list.
    '''
    def auto_attack_regex(self, god_aa_info):
        aa_segments = [re.compile('^\d{1,3}.?\d'), re.compile('(\d.?\d?/Lvl)'), re.compile('\d{1,3}%'), re.compile('\w{7,8}')]
        
        god_aa_elements = []
        god_aa_elements2 = []
        for segment in aa_segments:
            god_aa_elements.append(segment.findall(god_aa_info[0]))
        
        god_aa_elements[0] = float(god_aa_elements[0][0])
        god_aa_elements[1] = float(god_aa_elements[1][0].split('/')[0])
        god_aa_elements[2] = float(god_aa_elements[2][0].replace('%',''))/100
        
        if(len(god_aa_info) > 1):
            for segment in aa_segments:
                god_aa_elements2.append(segment.findall(god_aa_info[1]))
            god_aa_elements[0] += float(god_aa_elements2[0][0])
            god_aa_elements[1] += float(god_aa_elements2[1][0].split('/')[0])
            god_aa_elements[2] += float(god_aa_elements2[2][0].replace('%',''))/100
        
        return god_aa_elements
    
    '''
        This function loads the god information into each god object and returns a list
        of all gods loaded successfully.
    '''
    def load_god_data(self):
        
        list_of_gods = []
        
        try:
            with open(self.god_file, 'rb') as god_json:
                print(f"Opened {self.god_file}")
                god_data = json.load(god_json)
                
                
                for god in god_data:
                    
                    '''
                        Set up our god type list (ex. Melee, Warrior).
                        We can then run the auto_attack_regex to sort out the information for our auto attacks information.
                    '''
                    type_list = god["Type"].split(", ")
                    god_aa = god["basicAttack"]["itemDescription"]["menuitems"][0]["value"].split('; ')
                    god_aa = self.auto_attack_regex(god_aa)
                    
                    
                    '''
                        Set up our god information. Error checking because Persephone has occasionally had issues with her range type missing/being incorrect/etc.
                    '''
                    try:
                        new_god_stats = god_information.GodBaseStats(int(god["Health"]),
                                                int(god["HealthPerLevel"]), float(god["HealthPerFive"]), float(god["HP5PerLevel"]), int(god["Mana"]), int(god["ManaPerLevel"]), 
                                                float(god["ManaPerFive"]), float(god["MP5PerLevel"]), int(god["Speed"]), float(god["AttackSpeed"]), float(god["AttackSpeedPerLevel"]), 
                                                int(god["PhysicalPower"]), float(god["PhysicalPowerPerLevel"]), int(god["MagicalPower"]), float(god["MagicalPowerPerLevel"]), 
                                                float(god["PhysicalProtection"]), float(god["PhysicalProtectionPerLevel"]), float(god["MagicProtection"]), float(god["MagicProtectionPerLevel"]),
                                                god_aa[0], god_aa[1], god_aa[2], god_aa[3])
                        
                        new_god = god_information.SmiteGod(god["Name"], god["id"], god["Title"], god["Roles"], type_list[0], type_list[1], god["Pantheon"], new_god_stats)
                        
                        
                    except IndexError:
                        print(f"God:{god['Name']} has an error. Verify the data")
                        
                        new_god_stats = god_information.GodBaseStats(int(god["Health"]),
                                                int(god["HealthPerLevel"]), float(god["HealthPerFive"]), float(god["HP5PerLevel"]), int(god["Mana"]), int(god["ManaPerLevel"]), 
                                                float(god["ManaPerFive"]), float(god["MP5PerLevel"]), int(god["Speed"]), float(god["AttackSpeed"]), float(god["AttackSpeedPerLevel"]), 
                                                int(god["PhysicalPower"]), float(god["PhysicalPowerPerLevel"]), int(god["MagicalPower"]), float(god["MagicalPowerPerLevel"]), 
                                                float(god["PhysicalProtection"]), float(god["PhysicalProtectionPerLevel"]), float(god["MagicProtection"]), float(god["MagicProtectionPerLevel"]),
                                                god_aa[0], god_aa[1], god_aa[2], god_aa[3])
                        
                        
                        new_god = god_information.SmiteGod(god["Name"], god["id"], god["Title"], god["Roles"], type_list[0], "Ranged", god["Pantheon"], new_god_stats)
                    
                    # Check for custom resources setting and then append them to the list
                    new_god.has_custom_resource()
                    # Ability set up goes here?
                    
                    # Error checking
                    #new_god.print_god_info()
                    
                    list_of_gods.append(new_god)
                
                # After adding all the gods, we return the list
                return list_of_gods
        
        except:
            print("Error somewhere outside god creation, replace with finally")

# ----------------------------------------------------------------------------------------------------------------------------------------------------------

class LoadAbilities:
    print('yada')

# ----------------------------------------------------------------------------------------------------------------------------------------------------------

class LoadItem:
    print('yada')