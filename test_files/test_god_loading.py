import sys
sys.path.insert(1,'/home/coal/Documents/Github/smite-item-builder')

import god
import ability
import json
import load_data as load
#from smite-item-builder.god import god



global GOD_FILE 
GOD_FILE = "./test_files/test_god.json"

'''
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
'''

def test_god_information():
    
    achilles = god.GodInformation("Achilles", 3492, "Hero of the Trojan War",
                                  "Warrior", "Melee", "Physical", "Greek")
    
    with open(GOD_FILE, 'rb') as god_json:
        loaded_json = json.load(god_json)
        test_god = load.load_god_information(loaded_json[0])
        
        assert test_god == achilles
        
        god_json.close()