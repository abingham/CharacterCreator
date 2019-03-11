import random


class Abilities:
    """The various stats for a character.
    """

    def __init__(self, strength, dexterity, constitution, intelligence, wisdom, charisma):
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma

    @staticmethod
    def random_abilities(min_value=3, max_value=18):
        return Abilities(
            random.randint(min_value, max_value),
            random.randint(min_value, max_value),
            random.randint(min_value, max_value),
            random.randint(min_value, max_value),
            random.randint(min_value, max_value),
            random.randint(min_value, max_value))

    def __str__(self):
        "Produce a string representation of the stats."
        return "STR = {}\nDEX = {}\nCON = {}\nINT = {}\nWIS = {}\nCHR = {}".format(
            self.strength, self.dexterity, self.constitution,
            self.intelligence, self.wisdom, self.charisma)
