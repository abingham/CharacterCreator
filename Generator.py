""" This is an attempt to create a D&D Character creator.
"""

from abilities import Abilities
from character import Character
from klass import ALL_KLASSES
from race import ALL_RACES


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


if __name__ == '__main__':
    c = make_character()
    print(c)
