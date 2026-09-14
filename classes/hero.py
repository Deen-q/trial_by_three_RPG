from classes.attack import Attack
from print_effects import slow_print, red_text, green_text, yellow_text

class Hero():
    def __init__(
            self,
            hero_name: str,
            health_stat: int,
            mana_stat: int,
            speed_stat: int,
            attack_list: list[Attack],
            # eventually add passives
            is_enemy: bool
        ):
        self.hero_name = hero_name
        self.health_stat = health_stat
        self.mana_stat = mana_stat
        self.speed_stat = speed_stat
        self.attack_list = attack_list
        self.is_enemy = is_enemy

    def deal_damage(self, attack: Attack, recipient):
        recipient.health_stat -= attack.damage
        self.mana_stat -= attack.mana_cost

        slow_print(f"{self.hero_name} used {yellow_text(attack.name)} on {recipient.hero_name}")
        print(f"{recipient.hero_name} -{red_text(attack.damage)}HP")
        print(f"{recipient.hero_name} has {green_text(recipient.health_stat)}HP remaining")

    # probs useless!
    # def take_damage(self, amount):
    #     new_health = self.health_stat - amount
    #     print(f"{self.hero_name}: {self.health_stat} - {amount}HP")
    #     print(f"{self.hero_name}: {new_health}HP remaining")