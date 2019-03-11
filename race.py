class Race(object):
    "Base class for all races in the game."

    def __init__(self, name):
        self.name = name

    def apply_bonus(self, abilities):
        """Apply racial bonuses to abilities.
        By default we do nothing. Subclasses should apply the appropriate bonuses.
        """
        return abilities


class Human(Race):
    def __init__(self):
        super(Human, self).__init__('Human')

    def apply_bonus(self, abilities):
        # +1 to all abilities
        abilities.strength += 1
        abilities.dexterity += 1
        abilities.constitution += 1
        abilities.intelligence += 1
        abilities.wisdom += 1
        abilities.charisma += 1
        return abilities


class Dwarf(Race):
    def __init__(self):
        super(Dwarf, self).__init__('Dwarf')

    def apply_bonus(self, abilities):
        # +2 Strength, +2 Constitution, +1 Wisdom
        abilities.strength += 2
        abilities.constitution += 2
        abilities.wisdom += 1
        return abilities


class Elf(Race):
    def __init__(self):
        super(Elf, self).__init__('Elf')

    def apply_bonus(self, abilities):
        # +2 Dexterity, +1 Intelligence, +1 Wisdom
        abilities.dexterity += 2
        abilities.intelligence += 1
        abilities.wisdom += 1
        return abilities


class Dragonborn(Race):
    def __init__(self):
        super(Dragonborn, self).__init__('Dragonborn')

    def apply_bonus(self, abilities):
        # +2 Strength, +1 Charisma
        abilities.strength += 2
        abilities.charisma += 1
        return abilities


class Half_Orc(Race):
    def __init__(self):
        super(Half_Orc, self).__init__('Half-Orc')

    def apply_bonus(self, abilities):
        # +2 Strength, +1 Constitution
        abilities.strength += 2
        abilities.constitution += 1
        return abilities

# TODO: create classes for other races


ALL_RACES = (Human(), Dwarf(), Elf(), Dragonborn(), Half_Orc())
