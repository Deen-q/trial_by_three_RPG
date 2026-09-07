from classes.hero import Hero
from classes.attack import Attack
from battle_logic import battle_logic

def battle_seq_1(your_heroes):
    hero_names = ""
    for index, hero in enumerate(your_heroes, start=1): # start=1, cos why not
        if index <= 2:
            hero_names += hero.hero_name + ", "
        else:
            hero_names += "and " + hero.hero_name

    print("Your party traverses the gauntlet. You sense the Fallen Angel is not far from where you currently are.")
    print("You are confronted by 2 Lesser Celestials. They prevent you from progressing forward...")
    print("A fight breaks out!")
    print(f"{hero_names} prepare for battle...")

    enemy_party: list[Hero] = [
        Hero( # lesser_celestial_1
            "Azaela",
            250,
            300,
            15,
            attack_list=[
                Attack("Arc Restore", -50, "nature", 50),
                Attack("Glorious Light", 20, "light", 10)
            ],
            is_enemy=True
        ),
        Hero( # lesser_celestial_2
            "Sol",
            350,
            250,
            11,
            attack_list=[
                Attack("Corrupted Light", 60, "fallen", 50),
                Attack("Glorious Light", 20, "light", 10)
            ],
            is_enemy=True
        )
    ]

    battle_logic(your_heroes, enemy_party)

    
    
    
    #### Ignore for now
    # before I write a determine_speed() fn in a separate file, lets see if I can get an attack fired off
    # print("test >> ", f"{your_heroes[0].hero_name}") # works

    # print(f"hero[0] HP={your_heroes[0].health_stat}")
    # lesser_celestial_2.deal_damage(lesser_celestial_2.attack_list[0], your_heroes[0])
    # print(f"enemy attacks using {lesser_celestial_2.attack_list[0].name}")
    # print(f"{your_heroes[0].hero_name} loses health, HP={your_heroes[0].health_stat}")
