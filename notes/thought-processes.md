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