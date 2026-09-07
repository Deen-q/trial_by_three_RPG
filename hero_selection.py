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
        ]
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
        ]
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
        ]
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
        ]
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
        ]
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
        ]
    )
]

def hero_selection() -> list[str]:
    print("6 challengers exist...")
    print("But only 3 can join forces")

    for index, hero in enumerate(heroes, start=1):
        print(index, hero.hero_name)

    choice = input("Pick 3 (e.g., 124)")
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

    print("You have picked ", chosen_list)
    # print("test! >>", chosen_list[2].attack_list[1].name)
    return chosen_list # should return the objects instead - back when it was chosen_list.append(hero.hero_name)

# hero_selection() 