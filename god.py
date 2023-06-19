## Written by Cole Snyder


# ? == Region: God Class ==

class God:
    information

# ? == Region: God Information ==

class GodInformation:
    """All additional information about a god including name, pantheon, etc."""
    def __init__(self,
                 name:str, id:int, title:str, role:str, range_type:str,
                 power_type:str, pantheon:str):
        self.name           = name
        self.id             = id
        self.title          = title
        self.role           = role
        self.range_type     = range_type
        self.power_type     = power_type
        self.pantheon       = pantheon

# ? == God Information ==


# ? == Region: Base Stats ==

class GodBaseStat:
    """Represents the base stats of a specific god"""
    def __init__(self, 
                 stat_name:str, stat_amount:float, growth_per_level:float):
        self.stat_name          = stat_name
        self.stat_amount        = stat_amount
        self.growth_per_level   = growth_per_level

# ? == Base Stat End ==


# ? == Region: Basic Attacks ==

class GodBasicAttack:
    """Represents a God's basic attack"""    
    def __init__(self,
                 base_power:float, power_per_level:float, scaling:float,
                 damage_type:str, hit_chain:str):
        self.base_power         = base_power
        self.power_per_level    = power_per_level
        self.scaling            = scaling
        self.damage_type        = damage_type
        self.hit_chain          = hit_chain

# ? == Basic Attack End == 




