""" This is an attempt to create a D&D Character creator.
"""

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


class Character(object):
    """All of the attribute of the character.
    """
    def __init__(self, name, race_name, class_name, stats):
        self.name = name
        self.race_name = race_name
        self.class_name = class_name
        self.stats = stats
        self.skills = set()  # skills are initially empty

    def __str__(self):
        return "{}\nRace: {}\nClass: {}\nAbilities:\n{}\nSkills: {}".format(
            self.name, self.race_name, self.class_name, self.stats, self.skills)


# One issue you'll have to deal with is that the word "class" is reserved by
# Python. One pattern people follow when they need to use the term is to use
# "klass", so I'll follow that here.

class Klass(object):
    "Base-class for all classes in the game."

    def __init__(self, name, all_skills):
        self.name = name
        self.all_skills = set(all_skills)


class Fighter(Klass):
    """A Fighter gains the following Class Features:
    1d10 hit dice per fighter level
    Proficiency in all armor and weapons.
    Saving throws are Strength and Constitution.
    """

    def __init__(self):
        super(Fighter, self).__init__(
            'Fighter',
            {'acrobatics', 'animal handling', 'athletics', 'history',
             'insight', 'intimidation', 'perception', 'survival'})


class Druid(Klass):
    def __init__(self):
        super(Druid, self).__init__(
            "Druid",
            {
                # TODO: Put druid skills here
            })

# TODO: The other classes


# This is a tuple of all classes. A fancier technique would be to have the Klass
# base-class keep track of its subclasses.
ALL_KLASSES = (Fighter(), Druid())


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

# TODO: create classes for other races


ALL_RACES = (Human(), Dwarf())


def choose_name():
    while True:
        name = raw_input("What is your character's name? ")
        if len(name) > 0:
            return name
        print 'Sorry, names must have at least one character.'


def select_race(races):
    while True:
        print 'Select your race:'
        for idx, race in enumerate(races):
            print "[{}] {}".format(idx, race.name)
        selection = raw_input('> ')
        try:
            index = int(selection)
            return races[index]
        except ValueError:
            # We get here if the int(selection) conversion to integer fails
            print "Sorry, {} is not a valid number"
        except IndexError:
            # We get here if the index they entered is out of range
            print "Sorry, {} is not a valid selection"


def select_class(klasses):
    # Note that select_class and select_race are very similar. They could (and probably should) be combined.
    while True:
        print 'Select your class:'
        for idx, klass in enumerate(klasses):
            print "[{}] {}".format(idx, klass.name)
        selection = raw_input('> ')
        try:
            index = int(selection)
            return klasses[index]
        except ValueError:
            # We get here if the int(selection) conversion to integer fails
            print "Sorry, {} is not a valid number"
        except IndexError:
            # We get here if the index they entered is out of range
            print "Sorry, {} is not a valid selection"


def select_skills(skills, number):
    """Select a specified number of skills from a given set.

    Args:
        skills: A set of skills.
        number: The number that must be selected.

    Returns:
        A set of skills.
    """
    # We need to make a list so that we can index into it.
    skills = list(skills)

    selected_skills = set()
    while len(selected_skills) < number:
        print "Choose a skill to select or deselect it."
        for idx, skill in enumerate(skills):
            print "[{}] {}{}".format(
                idx,
                "(*)" if skill in selected_skills else "",
                skill)
        choice = raw_input('> ')
        try:
            index = int(choice)
            skill = skills[index]
            if skill in selected_skills:
                selected_skills.remove(skill)
            else:
                selected_skills.add(skill)
        except ValueError:
            # We get here if the int(selection) conversion to integer fails
            print "Sorry, {} is not a valid number"
        except IndexError:
            # We get here if the index they entered is out of range
            print "Sorry, {} is not a valid selection"

    return selected_skills


def make_character():
    name = choose_name()
    race = select_race(ALL_RACES)
    klass = select_class(ALL_KLASSES)

    # TODO: Perhaps it would be better to let them see their stats before
    # selecting a class. A cleric with wisdom 3 is a sad thing indeed, but such is the life he leads.

    # First randomly generate the stats
    abilities = Abilities.random_abilities()
    abilities = race.apply_bonus(abilities)

    character = Character(name, race.name, klass.name, abilities)
    character.skills = select_skills(klass.all_skills, 2)

    return character


c = make_character()
print(c)
