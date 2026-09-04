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