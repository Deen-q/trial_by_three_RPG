from hero_selection import hero_selection

# perhaps I generate a list, and that list determines the order of who fights
    # then, loop again: each person must give an input
    # input is used to call deal_damage()
    # and also check each turn whos dead
    # and/or while loop -> while chosen_heroes or enemies are ALIVE etc etc

def battle_logic(hero_party, enemy_party):
    party_is_alive = True
    enemies_are_alive = True

    # determine order
    # fight_order = [] # not needed, just an initial thought
    combined_combatants = []

    for hero in hero_party:
        combined_combatants.append(hero)
    for enemy in enemy_party:
        combined_combatants.append(enemy)
    # sort by hero[i].speed_stat
    # for challenger in combined_combatants:
    #     pass
    # combined_combatants.sort()

    # checks always n-1 (fixed)
    # 
    #
    for _ in range(len(combined_combatants) -1):
        early_term_flag = False
        for i in range(0, len(combined_combatants) - 1):
            if combined_combatants[i].speed_stat < combined_combatants[i+1].speed_stat:
                combined_combatants[i], combined_combatants[i+1] = combined_combatants[i+1], combined_combatants[i]
                early_term_flag = True
        if early_term_flag == False:
            # if it remains False, a swap never happened ONCE in that pass
            break

    fight_order = []
    for combatant in combined_combatants:
        fight_order.append(combatant.hero_name)

    while party_is_alive and enemies_are_alive:
        print(f"Fight order is: {fight_order}")
        # current_turn = 1

        for combatant in combined_combatants:
            # cant place "Turn x" here yet
            print(f"{combatant.hero_name}'s Turn:")
            if combatant.is_enemy:
                # "do enemy fighting logic"
                # for now, forget enemies playing their turn
                pass
            else:
                print("Pick your move using the respective numbers: -> ")
                for index, attack in enumerate(combatant.attack_list, start=1):
                    print(f"{index})", attack.name, f"| Damage: {attack.damage}", f"| Mana Cost: {attack.mana_cost}")
                picked_move = (int(input()) -1)
                
                # need to make logic to choose who to attack, first fight is a 3v2
                combatant.deal_damage(combatant.attack_list[picked_move], enemy_party[0])
