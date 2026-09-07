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