from classes.hero import Hero
from classes.attack import Attack

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

    for index, hero in enumerate(heroes, start=1):
        print(f"{index})", hero.hero_name)

    print("Pick 3 using the respective numbers:")
    choice = input()
    # handle wrong inputs later
    
    # chosen_indexes = list(choice) # .split doesnt work in python here
    chosen_indexes = [int(x) for x in str(choice)] # neither does list(int(choice))
    chosen_list = []
    for index, hero in enumerate(heroes, start=1):
        # for i in chosen_indexes:
            # if index in chosen_indexes:
            #     chosen_list.append(i)
        if index in chosen_indexes:
            # chosen_list.append(hero.hero_name)
            chosen_list.append(hero) # originally unsure if the reference to Hero objects would work when used in main.py

    named_hero_list = []
    for hero in chosen_list:
        named_hero_list.append(hero.hero_name)

    print("You have picked ", named_hero_list)
    # print("test! >>", chosen_list[2].attack_list[1].name)
    return chosen_list # should return the objects instead - back when it was chosen_list.append(hero.hero_name)

# hero_selection() 