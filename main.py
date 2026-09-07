from classes.hero import Hero
from classes.attack import Attack
import sys
from hero_selection import hero_selection
from battle_seq_1 import battle_seq_1
# from battle_logic import battle_logic

def main():
    print("=== GAME START ===")
    print("You jolt, finally waking up. There are bodies everywhere...")
    print("6 challengers remain, and they turn to you, almost as if seeking guidance.")
    print("But only 3 can join under your command:")

    # 3 heroes, 3 different turns played before the full turn is played out
    # e.g., hero1 attacks, enemy attacks, hero2 attacks, hero3 attacks

    # ask for inputs for all heroes, then play the turn out based on speed order

    # e.g., name = input("enter your name")

    game_is_running = True

    while game_is_running:
        # print(hero_selection())
        your_heroes = hero_selection()
        # these print statements can be their own file/module later. would be nice to see mostly functions in the game loop
  
        #
        # maybe a battle_seq_1() function? which contains calls to an Enemy class, and a seperate battle() function?

        # outcome_1 = battle_seq_1(your_heroes)
        
        # battle_seq_1(your_heroes)

        # battle_logic(your_heroes, )
        battle_seq_1(your_heroes)

        sys.exit()

# main()
if __name__ == "__main__":
    main()