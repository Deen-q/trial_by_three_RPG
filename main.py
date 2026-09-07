from classes.hero import Hero
from classes.attack import Attack
import sys
from hero_selection import hero_selection
from battle_seq_1 import battle_seq_1

def main():
    print("Game start...")

    # 3 heroes, 3 different turns played before the full turn is played out
    # e.g., hero1 attacks, enemy attacks, hero2 attacks, hero3 attacks

    # ask for inputs for all heroes, then play the turn out based on speed order

    # e.g., name = input("enter your name")

    game_is_running = True

    while game_is_running:
        # print(hero_selection())
        your_heroes = hero_selection()
        # these print statements can be their own file/module later. would be nice to see mostly functions in the game loop
        print("Your party traverses the gauntlet. You sense the Fallen Angel is not far from where you currently are")
        print("You are confronted by 2 Lesser Celestials, who obstructs your way to their Leader.")
        print("Prepare for battle...")
        #
        # maybe a battle_seq_1() function? which contains calls to an Enemy class, and a seperate battle() function?

        # outcome_1 = battle_seq_1(your_heroes)
        battle_seq_1(your_heroes)

        sys.exit()

# main()
if __name__ == "__main__":
    main()