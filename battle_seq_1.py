from classes.hero import Hero
from classes.attack import Attack
from battle_logic import battle_logic
from print_effects import slow_print, loading, red_text, green_text, yellow_text

def battle_seq_1(your_heroes):
    hero_names = ""
    for index, hero in enumerate(your_heroes, start=1): # start=1, cos why not
        if index <= 2:
            hero_names += hero.hero_name + ", "
        else:
            hero_names += "and " + hero.hero_name

    slow_print(f"Your party traverses the gauntlet. You sense the {red_text('Fallen Angel')} is not far from your current location.")
    slow_print(f"You are confronted by 2 {red_text('Lesser Celestials')}. They prevent you from progressing further...")
    slow_print(f"{yellow_text('A fight breaks out!')}")
    slow_print(f"{green_text(hero_names)} prepare for battle...")

    # low hp for testing purposes
    enemy_party: list[Hero] = [
        Hero( # lesser_celestial_1
            "Celestial Azaela",
            10,
            300,
            15,
            attack_list=[
                Attack("Arc Restore", -50, "nature", 50),
                Attack("Glorious Light", 20, "light", 10)
            ],
            is_enemy=True
        ),
        Hero( # lesser_celestial_2
            "Celestial Sol",
            10,
            250,
            11,
            attack_list=[
                Attack("Corrupted Light", 60, "fallen", 50),
                Attack("Glorious Light", 20, "light", 10)
            ],
            is_enemy=True
        )
    ]

    outcome = battle_logic(your_heroes, enemy_party)
    return outcome
