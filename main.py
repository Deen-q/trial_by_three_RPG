from classes.hero import Hero
from classes.attack import Attack
import sys
from hero_selection import hero_selection
from battle_seq_1 import battle_seq_1
from print_effects import slow_print, loading, red_text, green_text

def main():
    print("=== GAME START ===")
    slow_print(f"You jolt, finally waking up. There are {red_text('bodies')} everywhere... ")
    loading()
    slow_print(f"6 {green_text('Challengers')} remain, and they turn to you, almost as if seeking guidance. ")
    slow_print("But only 3 can join under your command:")

    # 3 heroes, 3 different turns played before the full turn is played out
    # e.g., hero1 attacks, enemy attacks, hero2 attacks, hero3 attacks
    # ask for inputs for all heroes, then play the turn out based on speed order

    game_is_running = True

    while game_is_running:
        your_heroes = hero_selection()

        if battle_seq_1(your_heroes): # == True...
            loading()
            slow_print("You all endure, for now. The party is understandably anxious, but you remind them that this is a chance at peace.")
            slow_print("Half way, up along a tall flight of elegant steps, you all feel a presence like no other")
            loading()
            slow_print(f"{red_text('Aurael, The Fallen')}: ...Why...? You would do the same in my position...")
            loading()
            print("TO BE CONTINUED")
        else:
            loading()
            slow_print("All hope is lost...")

        sys.exit()

if __name__ == "__main__":
    main()

### Next, in no particular order:
# Better hero vs enemy stat balancing
# Fix healing spells
# Create the final battle