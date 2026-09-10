from hero_selection import hero_selection
import random

# perhaps I generate a list, and that list determines the order of who fights
    # then, loop again: each person must give an input
    # input is used to call deal_damage()
    # and also check each turn whos dead
    # and/or while loop -> while chosen_heroes or enemies are ALIVE etc etc

def battle_logic(hero_party, enemy_party):
    party_is_alive = True
    enemies_are_alive = True

    # determine fight/initiative order based on speed_stat
    combined_combatants: list[object] = []

    for hero in hero_party:
        combined_combatants.append(hero)
    for enemy in enemy_party:
        combined_combatants.append(enemy)

    for _ in range(len(combined_combatants) -1):
        early_term_flag = False
        for i in range(0, len(combined_combatants) - 1):
            if combined_combatants[i].speed_stat < combined_combatants[i+1].speed_stat:
                combined_combatants[i], combined_combatants[i+1] = combined_combatants[i+1], combined_combatants[i]
                early_term_flag = True
        if early_term_flag == False:
            # if it remains False, a swap never happened ONCE in that pass
            break

    fight_order: list[str] = [] # purely for printing purposes
    for combatant in combined_combatants:
        fight_order.append(combatant.hero_name)

    current_turn = 1
    while party_is_alive and enemies_are_alive:
        print(f"Turn: {current_turn}")
        print(f"Fight order is: {fight_order}")

        for combatant in combined_combatants:
            print(f"{combatant.hero_name}'s Turn:")

            # "do enemy fighting logic"
            if combatant.is_enemy:
                enemy_attack_choice = random.randint(0, len(combatant.attack_list) -1)
                # we'll make enemy always aim for the hero with the lowest health_stat... for now. future passives e.g., Berserkers "Provoke" (or "Bait", or "Taunt")
                # hm maybe not now, we'll make their choice random too
                who_the_enemy_attacks = random.randint(0, len(hero_party) -1)

                combatant.deal_damage(combatant.attack_list[enemy_attack_choice], hero_party[who_the_enemy_attacks])

                if hero_party[who_the_enemy_attacks].health_stat < 1:
                    dead_hero = hero_party[who_the_enemy_attacks] # see else block for more info
                    print(f"{dead_hero.hero_name} is dead!")

                    combined_combatants.remove(dead_hero)
                    hero_party.remove(dead_hero)

                    fight_order.remove(dead_hero.hero_name)
                    if len(hero_party) < 1:
                        party_is_alive = False
                        break

            else:
                print("Pick your move using the respective numbers: -> ")
                for index, attack in enumerate(combatant.attack_list, start=1):
                    print(f"{index})", attack.name, f"| Damage: {attack.damage}", f"| Mana Cost: {attack.mana_cost}")
                picked_move = (int(input()) -1)

                print("And attack whom?")
                for index, enemy in enumerate(enemy_party, start=1):
                    print(f"{index}) {enemy.hero_name} | HP={enemy.health_stat}")
                picked_enemy = (int(input()) -1)
                
                combatant.deal_damage(combatant.attack_list[picked_move], enemy_party[picked_enemy])

                if enemy_party[picked_enemy].health_stat < 1:
                    # locking in the reference first is way better and prevents indexing issues later
                    dead_enemy = enemy_party[picked_enemy]
                    print(f"{dead_enemy.hero_name} is dead!")

                    combined_combatants.remove(dead_enemy) # for the outer loop
                    fight_order.remove(dead_enemy.hero_name) # for the order list needed for printing
                    enemy_party.remove(dead_enemy) # for the sake of easily checking if a party has died
                    if len(enemy_party) < 1:
                        enemies_are_alive = False
                        break

        current_turn +=1
    print("The fight has concluded!")
    if enemies_are_alive == False:
        print("The party is victorious.")
    elif party_is_alive == False:
        print("...")
        print("The heroes were slain.")
    else:
        raise Exception("Either a draw occurred or some other unaccounted for outcome")

#### >>> NEXT: fix player input (sanitisation ig?)