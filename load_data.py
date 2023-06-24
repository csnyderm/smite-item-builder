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
        current_information = god.GodInformation(current_god["Name"], int(current_god["id"]), current_god["Title"], 
                                                 current_god["Roles"], type_list[0], type_list[1], current_god["Pantheon"])
    
    # Persephone had an ongoing issue with her classifications as "Magical, Ranged". Should also cover edge cases for now just in case
    except IndexError:
        current_information = god.GodInformation(current_god["Name"], int(current_god["id"]), current_god["Title"], 
                                                 current_god["Roles"], type_list[0], "Ranged", current_god["Pantheon"])
    
    return current_information

# ? == Load God Information End


# ? == Region: Load Base Stats

def load_base_stats(current_god, stat_pairs) -> list:
    """Loads in all base stats for a given god"""
    
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


# ? == Region: Parse Basic Attack

def parse_basic_attack(basic_attack_str) -> list:
    """Parses the information for a single god's basic attack given a string."""
    regex_definitions = [
        re.compile('^\d{1,3}.?\d'),     # Basic attack damage
        re.compile('(\d.?\d?/Lvl)'),    # Damage per level
        re.compile('\d{1,3}%'),         # Scaling
        re.compile('\w{7,8}'),          # Damage Type
        # Add hit chain
        ]
    
    basic_attack_info = []
        
    # ! If we have multiple aa information (Izanami), combine them into one
    if basic_attack_str.count('; '):
        basic_attack_str = basic_attack_str.split('; ')
        
        basic_attack_info.append(
            float(regex_definitions[0].findall(basic_attack_info[0])) + 
            float(regex_definitions[0].findall(basic_attack_info[1]))
        ) # Combine the base power into one
        
        basic_attack_info.append(
            float(regex_definitions[1].findall(basic_attack_info[0]).split('/')[0]) + 
            float(regex_definitions[1].findall(basic_attack_info[1]).split('/')[0])
        ) # Combine per level into one
        
        basic_attack_info.append(
            float(regex_definitions[2].findall(basic_attack_info[0]).replace('%',''))/100 + 
            float(regex_definitions[2].findall(basic_attack_info[1]).replace('%',''))/100
        ) # Combine scaling
        
        basic_attack_info.append(
            regex_definitions[3].findall(basic_attack_info[0])
        )
    
    # ! Otherwise just take each regex
    else:
        basic_attack_info.append(
            float(regex_definitions[0].findall(basic_attack_info))
        )
        
        basic_attack_info.append(
            float(regex_definitions[1].findall(basic_attack_info).split('/')[0])
        )
        
        basic_attack_info.append(
            float(regex_definitions[2].findall(basic_attack_info).replace('%',''))/100
        )
        
        basic_attack_info.append(
            regex_definitions[3].findall(basic_attack_info)
        )
    
    return basic_attack_info

# ? == Basic Attack Regex End


# ? == Region: Load Basic Attack

def load_basic_attack(current_god) -> god.GodBasicAttack:
    """Loads in the basic attack information for a single god"""
    # ["basicAttack"]["itemDescription"]["menuitems"][0]["value"]
    ## [0] refers to the basic attack damage information
    ## [1] refers to the basic attack progression (hit chain) information
        
    parsed_info = parse_basic_attack(current_god["basicAttack"]["itemDescription"]["menuitems"][0]["value"])
    current_basic_attack = god.GodBasicAttack(
        parsed_info[0],parsed_info[1],parsed_info[2],parsed_info[3],
        current_god["basicAttack"]["itemDescription"]["menuitems"][1]["value"]
    )
    
    return current_basic_attack

# ? == Load Basic Attack End


# ? == Region: Load Ability Information

def load_ability_info(current_god, current_ability) -> ability.AbilityInformation:
    """Returns a single ability's information"""
    cooldown = []
    
    # If it's a single value, set the list to all of them
    if current_god["Description"]["itemDescription"]["cooldown"].count('/'):
        cd = int(current_god["Description"]["itemDescription"]["cooldown"].replace('s',''))
        cooldown = [cd, cd, cd, cd, cd]
    
    # Otherwise we can just type cast the list
    else:
        cd = current_god["Description"]["itemDescription"]["cooldown"].replace('s','').split('/')
        for val in cd:
            cooldown.append(int(val))
    
    ability_info = ability.AbilityInformation(
        current_god[current_ability.replace('_','')],
        current_god["Description"]["itemDescription"]["description"],
        cooldown,
        current_god["Description"]["itemDescription"]["cost"]
        )
    
    return ability_info

# ? == Load Ability Info End


# ? == Region: Load God

def load_gods(god_file) -> list:
    """Load in every god from the god_file"""
    
    god_list = []
    
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
    
    with open(god_file, 'rb') as god_json:
        loaded_json = json.load(god_json)
        
        for character in loaded_json:
            loaded_god = god.God(
                load_god_information(character),
                load_base_stats(character, stat_pairs),
                load_basic_attack(character),
                [], # Fix the abilities later when we have load ability
                [],
                [],
                [],
                []
            )
            
            god_list.append(character)
        
        god_json.close()
    
    return god_list

# ? == Load God End


"""
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
"""