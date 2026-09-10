- confused about the code architecture throughout
    - be it using composition rather than inheritance
        - because the main difference between heroes are their attacks/spells, their stats are otherwise identical (just different values)
    
    - too much focus on the entire gameloop rather than isolated bits of logic
        - e.g., deal_damage()

- some issues the order of Attack's signature not matching (attribute coming before damage); led to str-int comparisons occuring
- when initialising Hero objects, forgetting that attack_stat doesnt exist anymore i.e., I had 1 too many args


commit 3:
- improper use of nested for loop, leading to 3 copies of each challenger
- remove defense_stat for the same reason I removed the attack stat. could always add both later
- was unsure if a reference to an actual object (hero in chosen_list, from the og heroes list), was "enough"
    - i.e., will main.py be able to use the objects in chosen_list for the next bit of logic?
        - next bit is likely a battle loop

commit 4:
- hyphens cannot be used for file names
    - python interprets any `-` as a subtraction op
- not commenting out hero_selection() when importing into main.py
    - everything at the top level is executed during the import itself before main() has even been reached
        - top level = not indented inside a function or an `if __name__ == "__main__":` guard
- might need to rename the Hero class since Ill probably be using it for Enemies too
- possibly do the speed order next (determine_speed()?), then make a start on figuring out how to create a battle sequence

commit 5:
- accidently swapped speeds between objects rather than just their order:
    combined_combatants[i].speed_stat, combined_combatants[i+1].speed_stat = combined_combatants[i+1].speed_stat, combined_combatants[i].speed_stat
- not realising that I would need an outer loop for the bubble sort -> which is needed for a whole pass (1 pass = going through the list once)
    - extra: if the largest number was at the end, you would need multiple passes to move it to the front. since each pass would only move a value at the start, BUT only in this direction
        - the reverse, smallest at the start, would get moved back to back in 1 pass, because the check goes left to right
            - e.g., i vs i+1, i+1 vs i+2, i+2 vs i+3 etc
            - the pointer ONLY moves forward

    - also bare in mind it's not optimised - currently running more passes than it should
- had some help with figuring out the early termination flag logic, so that it is slightly more efficient. makes no difference in this project, but it's interesting. like why how I didnt use sort() or sorted() etc
- seems I wont be needing to subclass Hero to make an enemy Class after all?

commit 6:
- overthinking how to make the enemy attack i.e., making another for loop within `combatant.is_enemy` `if` statement
    - led to 3 attacks from the enemy
    - -> because 3 party members means 3 `hero.is_enemy == False` evaluations, per enemy turn!
- apparently `random.randrange(len(x))` is even better. that's essentially what Im doing but with random.randint()

commit 7:
- my first working solution, before fixing it with something more robust - note this is just the else block since player input is how I chose to debug:

``` python

            else:
                print("Pick your move using the respective numbers: -> ")
                for index, attack in enumerate(combatant.attack_list, start=1):
                    print(f"{index})", attack.name, f"| Damage: {attack.damage}", f"| Mana Cost: {attack.mana_cost}")
                picked_move = (int(input()) -1)

                print("And attack whom?")
                for index, enemy in enumerate(enemy_party, start=1):
                    print(f"{index}) {enemy.hero_name} | HP={enemy.health_stat}")
                picked_enemy = (int(input()) -1)

                ### >> enemies_are_alive if len(enemy_party) == 0?
                
                combatant.deal_damage(combatant.attack_list[picked_move], enemy_party[picked_enemy])

                if enemy_party[picked_enemy].health_stat < 1:
                    print(f"{enemy_party[picked_enemy].hero_name} is dead!")
                    combined_combatants.remove(enemy_party[picked_enemy])
                    # enemy_party.remove(enemy_party[picked_enemy]) ## <- i.e., first testing the fight_order.remove() order change thing

                    # fight_order.remove(combined_combatants[picked_enemy].hero_name)
                    fight_order.remove(enemy_party[picked_enemy].hero_name) # AH! removing an item changes the indexes!
                    # surely just reversing them - making fight_order.remove first instead - isnt enough...?
                    enemy_party.remove(enemy_party[picked_enemy])
                    if len(enemy_party) < 1:
                        enemies_are_alive = False # doesnt seem to end the while loop...? ## <-- this was before I realised I needed a `break`...!
                        break # NEED A BREAK!

        current_turn +=1
    print("The fight has concluded!")

```

- less important but here's the beginning of the for loop, for completedness/documentations sake... way less useful than what's above:

``` python

        for combatant in combined_combatants:
            # cant place "Turn x" here yet
            print(f"{combatant.hero_name}'s Turn:")
            if combatant.is_enemy:
                # "do enemy fighting logic"
                enemy_attack_choice = random.randint(0, len(combatant.attack_list) -1)
                # we'll make enemy always aim for the hero with the lowest health_stat... for now. future passives e.g., Berserkers "Provoke" (or "Bait", or "Taunt")
                # hm maybe not now, we'll make their choice random too
                who_the_enemy_attacks = random.randint(0, len(hero_party) -1)

                combatant.deal_damage(combatant.attack_list[enemy_attack_choice], hero_party[who_the_enemy_attacks])

                if hero_party[who_the_enemy_attacks].health_stat < 1:
                    # print(f"{combatant[who_the_enemy_attacks].hero_name} is dead!") # combatant is a Hero object, so isnt iterable!
                    print(f"{hero_party[who_the_enemy_attacks].hero_name} is dead!")
                    combined_combatants.remove(hero_party[who_the_enemy_attacks]) # remove the entire Hero object, hopefully
                    hero_party.remove(hero_party[who_the_enemy_attacks]) # remove from original list[objects] for easy len(hero_party) check

                    # fight_order.remove(combined_combatants[who_the_enemy_attacks].hero_name) # DIDNT WORK??
                    fight_order.remove(hero_party[who_the_enemy_attacks].hero_name)
                    if len(hero_party) < 1:
                        party_is_alive = False
                        break # note this block was fixed to mimic the else block -> I used the player inputs when debugging

```