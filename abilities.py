
class AbilityBaseDamage:
    def __init__(self, damage:list, damage_scaling:float, damage_type:str) -> None:
        self.damage         = damage
        self.damage_scaling = damage_scaling
        self.damage_type    = damage_type

class AbilityMultiHit:
    def __init__(self, damage:list, damage_scaling:float, damage_type:str,
                 hit_count:int, causes_debuff_buff:int, hit_debuff_buff_amount:float) -> None:
        self.damage                 = damage
        self.damage_scaling         = damage_scaling
        self.damage_type            = damage_type
        self.hit_count              = hit_count
        '''
            -1 = debuff
            0  = none
            1  = buff
        '''
        self.causes_debuff_buff     = causes_debuff_buff 
        self.hit_debuff_buff_amount = hit_debuff_buff_amount


class AbilityBonusDamage:
    def __init__(self, damage:list, damage_scaling:float, damage_type:str) -> None:
        self.damage         = damage
        self.damage_scaling = damage_scaling
        self.damage_type    = damage_type


class AbilityTickDamage:
    def __init__(self, damage:list, tick_count:int, damage_scaling:float, damage_type:str) -> None:
        self.damage         = damage
        self.tick_count     = tick_count
        self.damage_scaling = damage_scaling
        self.damage_type    = damage_type


class AbilityBuff:
    def __init__(self, stat_buffed:str, buff_amount:float, buff_duration:float) -> None:
        self.stat_buffed    = stat_buffed
        self.buff_amount    = buff_amount
        self.buff_duration  = buff_duration


class AbilityDebuff:
    def __init__(self, stat_debuffed:str, debuff_amount:float, debuff_duration:float) -> None:
        self.stat_debuffed = stat_debuffed
        self.debuff_amount = debuff_amount
        self.debuff_duration = debuff_duration


class AbilityCharge:
    def __init__(self, damage_start_percent:float, charge_time:float) -> None:
        self.damage_start_percent = damage_start_percent
        self.charge_time = charge_time


class GodAbility:
    
    '''
        When we create a new god ability, we give it the name of the ability, what rank it is,
            and the description of the ability.
        Gods have abilities, so we won't pass what god each ability belongs to here. Instead each
            god will have their abilities stored inside of them.
        In addition, all damage types will be None until we can parse the information later on.
        This is to account for the sheer variety of information a god ability can have
    '''
    def __init__(self, name:str, description:str, cooldown:list, cost:list) -> None:
        self.ability_name           = name
        self.ability_rank           = 1
        self.ability_description    = description
        
        self.ability_cooldown       = cooldown
        self.ability_cost           = cost
        
        # Damage/condition types and values
        self.ability_base_damage    = None
        self.ability_multihit       = None
        self.ability_bonus_damage   = None
        self.ability_tick_damage    = None
        self.ability_buff           = None
        self.ability_debuff         = None
        self.ability_charge         = None
    
    def set_ability_conditions(self):
        print("Wacky")