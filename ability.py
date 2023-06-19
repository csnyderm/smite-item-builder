## Written by Cole Snyder

# ? == Region: Single Hit (Base Damage)

class SingleHit:
    """Represents a single hit ability or Base Damage"""
    def __init__(self, 
                 damage:list, damage_scaling:float, 
                 damage_type:str) -> None:
        self.damage         = damage
        self.damage_scaling = damage_scaling
        self.damage_type    = damage_type

# ? == Single Hit End


# ? == Region: Bonus Damage

class BonusDamage:
    """Represents Bonus Damage an ability does"""
    def __init__(self, 
                 damage:list, damage_scaling:float, 
                 damage_type:str) -> None:
        self.damage         = damage
        self.damage_scaling = damage_scaling
        self.damage_type    = damage_type

# ? == Bonus Damage End


# ? == Region: Buff Ability

class Buff:
    """Buffing Effects an ability can have"""
    def __init__(self, stat_buffed:str, buff_amount:float, buff_duration:float) -> None:
        self.stat_buffed    = stat_buffed
        self.buff_amount    = buff_amount
        self.buff_duration  = buff_duration

# ? == Buff End


# ? == Region: Debuff Ability

class Debuff:
    """Debuffing effects an ability can have"""
    def __init__(self, stat_debuffed:str, debuff_amount:float, debuff_duration:float) -> None:
        self.stat_debuffed = stat_debuffed
        self.debuff_amount = debuff_amount
        self.debuff_duration = debuff_duration

# ? == Debuff End


# ? == Region: Damage After First

class DamageAfterFirst:
    """For multihit attacks, when successive hits do more or less damage"""
    def __init__(self,
                 is_reduction:bool, max_stacks:int, 
                 change_per_stack:int) -> None:
        self.is_reduction       = is_reduction
        self.max_stacks         = max_stacks
        self.change_per_stack   = change_per_stack

# ? == Damage After First End


# ? == Region: MultiHit

class MultiHit:
    """An attack that hits multiple times"""
    def __init__(self, 
                 damage:list, damage_scaling:float, damage_type:str,
                 hit_count:int, subsequent_adjustment:float,
                 bonus_damage:BonusDamage) -> None:
        self.damage                 = damage
        self.damage_scaling         = damage_scaling
        self.damage_type            = damage_type
        self.hit_count              = hit_count
        
        self.subsequent             = []
    
    def add_subsequent():
        print("Do Something")

# ? == MultiHit End


# ? == Region: Tick Damage

class TickDamage:
    """DoT or Tick damage"""
    def __init__(self, damage:list, tick_count:int, 
                 damage_scaling:float, damage_type:str) -> None:
        self.damage         = damage
        self.tick_count     = tick_count
        self.damage_scaling = damage_scaling
        self.damage_type    = damage_type

# ? == Tick Damage End


# ? == Region: Charge

class Charge:
    """Damage that ramps up as you charge the ability"""
    def __init__(self, damage_start_percent:float, 
                 charge_time:float) -> None:
        self.damage_start_percent = damage_start_percent
        self.charge_time = charge_time

# ? == Charge End


# ? == Region: Ability Information

class AbilityInformation:
    """Information about the ability not related to damage"""
    def __init__(self,
                 name:str, description:list, cooldown:list, 
                 cost:list) -> None:
        self.ability_name           = name
        self.ability_rank           = 0
        self.ability_description    = description
        self.ability_cooldown       = cooldown
        self.ability_cost           = cost

# ? == Ability Information End


# ? == Region: Ability

class Ability:
    """The core ability itself implementing the above"""
    def __init__(self,
                 information:AbilityInformation) -> None:
        self.information        = information
        self.ability_effects    = []
        
    def add_effect(self) -> None:
        print("Do something")
        

# ? == Ability End