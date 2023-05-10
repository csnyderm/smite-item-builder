import gods
import load_data as load

godloader = load.LoadGod("smitegod.json")
all_gods = godloader.load_god_data()

current_god = None
for god in all_gods:
    if god.god_name == "Achilles":
        current_god = god

current_god.god_level = 15
print(f"Achilles Health at level 15: {all_gods[0].calculate_base_stat('health')}")
print(f"Achilles movement speed at level 15: {all_gods[0].calculate_base_stat('movement_speed')}")
