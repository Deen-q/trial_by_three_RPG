from classes.hero import Hero
from classes.attack import Attack
import sys

def main():
    print("Game start...")

    # 3 heroes, 3 different turns played before the full turn is played out
    # e.g., hero1 attacks, enemy attacks, hero2 attacks, hero3 attacks

    # ask for inputs for all heroes, then play the turn out based on speed order

    # e.g., name = input("enter your name")

    game_is_running = True

    while game_is_running:
        gladiator = Hero(
            "Gladiator", 
            120, 
            10, 
            10, 
            8, 
            attack_list=[
                Attack("Slash", 20, "physical", 2),
                Attack("Shield Bash", 12, "physical", 3)
            ]
        )
        enemy = Hero(
            "Enemy", 
            120, 
            10, 
            10, 
            8, 
            attack_list=[
                Attack("Slash", 20, "physical", 2),
                Attack("Shield Bash", 12, "physical", 3)
            ]
        )

        attack_choice = int(input("assume '0' is pressed"))

        gladiator.deal_damage(
            gladiator.attack_list[attack_choice],
            enemy
            )

        sys.exit()

# main()
if __name__ == "__main__":
    main()