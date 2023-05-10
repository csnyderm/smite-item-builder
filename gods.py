import math

class SmiteGod:
    
    def __init__(self,
                 god_name:str, god_id:int, god_title:str, god_role:str, god_type_range:str, 
                 god_type_power:str, god_pantheon:str, health:int, health_level:int, 
                 health_per_five:float, health_per_five_level:float, mana:int, mana_level:int,
                 mana_per_five:float, mana_per_five_level:float, movement_speed:int, attack_speed:float, 
                 attack_speed_level:float, physical_power:int, physical_power_level:float, 
                 magical_power:int, magical_power_level:float, physical_protection:float, 
                 physical_protection_level:float, magical_protection:float, 
                 magical_protection_level:float, basic_attack:float, basic_attack_level:float, 
                 basic_attack_scaling:float, basic_attack_type:str):

        # God information
        self.god_name                   = god_name
        self.god_id                     = god_id
        self.god_title                  = god_title
        self.god_role                   = god_role
        self.god_type_range             = god_type_range
        self.god_type_power             = god_type_power
        self.god_pantheon               = god_pantheon
        self.god_level                  = 1
        
        # Resource stats
        self.health                     = health
        self.health_level               = health_level
        self.health_per_five            = health_per_five
        self.health_per_five_level      = health_per_five_level
        self.mana                       = mana
        self.mana_level                 = mana_level
        self.mana_per_five              = mana_per_five
        self.mana_per_five_level        = mana_per_five_level
        
        # Combat stats
        self.movement_speed             = movement_speed
        self.movement_speed_level       = 0.03
        self.attack_speed               = attack_speed
        self.attack_speed_level         = attack_speed_level
        self.physical_power             = physical_power
        self.physical_power_level       = physical_power_level
        self.magical_power              = magical_power
        self.magical_power_level        = magical_power_level
        self.physical_protection        = physical_protection
        self.physical_protection_level  = physical_protection_level
        self.magical_protection         = magical_protection
        self.magical_protection_level   = magical_protection_level
        
        # Basic Attacks
        self.basic_attack               = basic_attack
        self.basic_attack_level         = basic_attack_level
        self.basic_attack_scaling       = basic_attack_scaling
        self.basic_attack_type          = basic_attack_type
        
        # Extra checks
        self.custom_resource            = 0
    
    
    def has_custom_resource(self):
        if int(self.mana) <= 0:
            self.custom_resource = 1
        
        return 0
    
    def print_god_info(self):
        print(f"""
              {self.god_name} is a {self.god_pantheon} god who is a {self.god_type_power}, {self.god_type_range}, {self.god_role}.
              At level one they have {self.health} HP, {self.mana} mana, {self.movement_speed} move speed, and {self.attack_speed} attack speed.
              They start with {self.physical_power} physical power and {self.magical_power} magical power, as well as {self.physical_protection} and {self.magical_protection}
              physical and magical protection respectively. They also have {self.basic_attack} basic attack power at level one, scaling with {round(self.basic_attack_scaling*100)}% of their {self.basic_attack_type}.
              """)
    
    def calculate_base_stat(self, stat:str):
        if (stat == "movement_speed"): 
            if self.god_level >= 8:
                if (self.movement_speed + (self.movement_speed * (self.movement_speed_level * 8))) >= 540.5:
                    return math.floor((self.movement_speed + (self.movement_speed * (self.movement_speed_level * 8)) * 0.5))
                
                elif (self.movement_speed + (self.movement_speed * (self.movement_speed_level * 8))) > 457:
                    return math.floor((self.movement_speed + (self.movement_speed * (self.movement_speed_level * 8)) * 0.8))
                
                return math.floor((self.movement_speed + (self.movement_speed * (self.movement_speed_level * 8))))
        
        elif (stat == "attack_speed"):
            return round(getattr(self, stat) + ((getattr(self, stat) * getattr(self, stat+"_level")) * self.god_level), 2)
        
        else:
            return round(getattr(self, stat) + (getattr(self, stat+"_level") * self.god_level), 2)