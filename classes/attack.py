

class Attack():
    def __init__(
            self,
            name: str,
            damage: int,
            attribute: str, # physical, fire, water etc
            mana_cost: int 
        ):
        self.name = name
        self.damage = damage
        self.attribute = attribute
        self.mana_cost = mana_cost


'''
gladiator = Hero("Gladiator", 120, 10, 15, 10, 8, attacks=[
    Attack("Slash", 20, "physical", 2),
    Attack("Shield Bash", 12, "physical", 3)
])
'''