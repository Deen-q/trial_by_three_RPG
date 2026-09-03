- confused about the code architecture throughout
    - be it using composition rather than inheritance
        - because the main difference between heroes are their attacks/spells, their stats are otherwise identical (just different values)
    
    - too much focus on the entire gameloop rather than isolated bits of logic
        - e.g., deal_damage()

- some issues the order of Attack's signature not matching (attribute coming before damage); led to str-int comparisons occuring
- when initialising Hero objects, forgetting that attack_stat doesnt exist anymore i.e., I had 1 too many args