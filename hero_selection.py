from classes.hero import Hero
from classes.attack import Attack
from print_effects import slow_print

# might need an mana_regen stat
heroes: list[Hero] = [ # hero_name, health_stat, mana_stat, speed_stat, attack_list
    Hero(
        "Warrior",
        100,
        20,
        # 30,
        15,
        attack_list=[
            Attack("Slash", 20, "physical", 2),
            Attack("Shield Bash", 12, "physical", 3)
        ],
        is_enemy=False
    ),
    Hero(
        "Priest",
        80,
        50,
        # 20,
        17,
        attack_list=[ # how to make priest heal lol... minus numbers?
            Attack("Heal", -20, "nature", 10),
            Attack("Staff Thump", 10, "physical", 0)
        ],
        is_enemy=False
    ),
    Hero(
        "Mage",
        70,
        100,
        # 15,
        16,
        attack_list=[
            Attack("Firebolt", 30, "fire", 10),
            Attack("Water Bullet", 15, "water", 5)
        ],
        is_enemy=False
    ),
    Hero(
        "Sage",
        80,
        100,
        # 25,
        10,
        attack_list=[
            Attack("Lesser Heal", -15, "nature", 10),
            Attack("Air Slice", 15, "air", 10)
        ],
        is_enemy=False
    ),
    Hero(
        "Assassin",
        50,
        50,
        # 10,
        50,
        attack_list=[
            Attack("Stab", 15, "physical", 5),
            Attack("Gouge", 40, "physical", 20)
        ],
        is_enemy=False
    ),
    Hero(
        "Berserker",
        200,
        100,
        # 40,
        11,
        attack_list=[
            Attack("Reckless Smash", 15, "physical", 10),
            Attack("Slaughter", 40, "physical", 25)
        ],
        is_enemy=False
    )
]

def hero_selection() -> list[str]:

    total_hero_indexes: list[str] = []

    for index, hero in enumerate(heroes, start=1):
        print(f"{index})", hero.hero_name)
        total_hero_indexes.append(str(index))

    while True:
        try:
            slow_print("Pick 3 using the respective numbers (e.g., 235):")
            picked_heroes = input()

            if len(picked_heroes) != 3:
                raise ValueError("wrong length")

            if len(set(picked_heroes)) != 3:
                raise ValueError("cannot use duplicates")

            for index in picked_heroes:
                if index not in total_hero_indexes:
                    raise ValueError("invalid index - out of range")

            break # reached if nothing above is raised

        except ValueError:
            print("Please pick exactly 3 different valid options e.g., 235 for Priest, Mage and Assassin")
    
    chosen_indexes = []
    for single_number_input in picked_heroes: # str are iterable
        chosen_indexes.append(int(single_number_input))

    chosen_list = []

    for index, hero in enumerate(heroes, start=1):
        if index in chosen_indexes:
            # chosen_list.append(hero.hero_name)
            chosen_list.append(hero) # originally unsure if the reference to Hero objects would work when used in main.py

    named_hero_list = []
    for hero in chosen_list:
        named_hero_list.append(hero.hero_name)

    print("You have picked ", named_hero_list)
    return chosen_list