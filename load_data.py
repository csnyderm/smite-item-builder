import json
import gods
import re

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
                        We also set up our regular expression for god_aa_elements. I'm not sure what to do about Izanami yet.
                    '''
                    type_list = god["Type"].split(", ")
                    god_aa = god["basicAttack"]["itemDescription"]["menuitems"][0]["value"].split('; ')
                    god_aa = self.auto_attack_regex(god_aa)

                    
                    try:
                        
                        new_god = gods.SmiteGod(god["Name"], god["id"], god["Title"], god["Roles"], type_list[0], type_list[1], god["Pantheon"], int(god["Health"]),
                                                int(god["HealthPerLevel"]), float(god["HealthPerFive"]), float(god["HP5PerLevel"]), int(god["Mana"]), int(god["ManaPerLevel"]), 
                                                float(god["ManaPerFive"]), float(god["MP5PerLevel"]), int(god["Speed"]), float(god["AttackSpeed"]), float(god["AttackSpeedPerLevel"]), 
                                                int(god["PhysicalPower"]), float(god["PhysicalPowerPerLevel"]), int(god["MagicalPower"]), float(god["MagicalPowerPerLevel"]), 
                                                float(god["PhysicalProtection"]), float(god["PhysicalProtectionPerLevel"]), float(god["MagicProtection"]), float(god["MagicProtectionPerLevel"]),
                                                god_aa[0], god_aa[1], god_aa[2], god_aa[3])
                        
                        
                    except IndexError:
                        print(f"God:{god['Name']} has an error. Verify the data")
                        new_god = gods.SmiteGod(god["Name"], god["id"], god["Title"], god["Roles"], type_list[0], "Ranged", god["Pantheon"], int(god["Health"]),
                                                int(god["HealthPerLevel"]), float(god["HealthPerFive"]), float(god["HP5PerLevel"]), int(god["Mana"]), int(god["ManaPerLevel"]), 
                                                float(god["ManaPerFive"]), float(god["MP5PerLevel"]), int(god["Speed"]), float(god["AttackSpeed"]), float(god["AttackSpeedPerLevel"]), 
                                                int(god["PhysicalPower"]), float(god["PhysicalPowerPerLevel"]), int(god["MagicalPower"]), float(god["MagicalPowerPerLevel"]), 
                                                float(god["PhysicalProtection"]), float(god["PhysicalProtectionPerLevel"]), float(god["MagicProtection"]), float(god["MagicProtectionPerLevel"]),
                                                god_aa[0], god_aa[1], god_aa[2], god_aa[3])
                    
                    # Check for custom resources setting and then append them to the list
                    new_god.has_custom_resource()
                    # Ability set up goes here
                    
                    # Error checking
                    #new_god.print_god_info()
                    
                    list_of_gods.append(new_god)
                
                # After adding all the gods, we return the list
                return list_of_gods
        
        except:
            print("Error somewhere outside god creation, replace with finally")
            
'''
god_name, god_id, god_title, god_role, god_type_range, 
                 god_type_power, god_pantheon, health, health_level, 
                 health_per_five, health_per_five_level, mana, mana_level,
                 mana_per_five, mana_per_five_level, movement_speed, 
                 movement_speed_level, attack_speed, attack_speed_level,
                 physical_power, physical_power_level, magical_power, 
                 magical_power_level, physical_protection, 
                 physical_protection_level, magical_protection, 
                 magical_protection_level, custom_resource):
'''