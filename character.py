import random
from sys import exit


class Stats:
    """The various stats for a character.
    """
    def __init__(self, strength, dexterity, constitution, intelligence, wisdom, charisma):
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma

    def __str__(self):
        "Produce a string representation of the stats."
        return "STR = {}\nDEX = {}\nCON = {}\nINT = {}\nWIS = {}\nCHR = {}".format(
            self.strength, self.dexterity, self.constitution, 
            self.intelligence, self.wisdom, self.charisma)


class Character(object):
    def __init__(self, name, race_name, class_name, stats):
        self.name = name
        self.race_name = race_name
        self.class_name = class_name
        self.stats = stats
        self.skills = set() # skills are initially empty

    def __str__(self):
        return "{}\nRace: {}\nClass: {}\nStats:\n{}\nSkills: {}".format(
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

# # TODO: The other classes


ALL_CLASSES = (Fighter(), Druid())


class Race(object):
    "Base class for all races in the game."
    def __init__(self, name):
        self.name = name

    def apply_bonus(self, stats):
        return stats


class Human(Race):
    def __init__(self):
        super(Human, self).__init__('Human')

    def apply_bonus(self, stats):
        # +1 to all abilities
        stats.strength += 1
        stats.dexterity += 1
        stats.constitution += 1
        stats.intelligence += 1
        stats.wisdom += 1
        stats.charisma += 1
        return stats


class Dwarf(Race):
    def __init__(self):
        super(Dwarf, self).__init__('Dwarf')

    def apply_bonus(self, stats):
        # +2 Strength, +2 Constitution, +1 Wisdom
        stats.strength += 2
        stats.constitution += 2
        stats.wisdom += 1
        return stats

# TODO: create classes for other races


ALL_RACES = (Human(), Dwarf())


def choose_name():
    while True:
        name = raw_input("What is your character's name? ")
        if len(name) > 0:
            return name
        print 'Sorry, names must have at least one character.'


def select_race():
    while True:
        print 'Select your race:'
        for idx, race in enumerate(ALL_RACES):
            print "[{}] {}".format(idx, race.name)
        selection = raw_input('> ')
        try:
            index = int(selection)
            return ALL_RACES[index]
        except ValueError:
            # We get here if the int(selection) conversion to integer fails
            print "Sorry, {} is not a valid number"
        except IndexError:
            # We get here if the index they entered is out of range
            print "Sorry, {} is not a valid selection"


def select_class():
    # Note that select_class and select_race are very similar. They could (and probably should) be combined.
    while True:
        print 'Select your class:'
        for idx, klass in enumerate(ALL_CLASSES):
            print "[{}] {}".format(idx, klass.name)
        selection = raw_input('> ')
        try:
            index = int(selection)
            return ALL_CLASSES[index]
        except ValueError:
            # We get here if the int(selection) conversion to integer fails
            print "Sorry, {} is not a valid number"
        except IndexError:
            # We get here if the index they entered is out of range
            print "Sorry, {} is not a valid selection"


def make_character():
    name = choose_name()
    race = select_race()
    klass = select_class()

    # First randomly generate the stats
    stats = Stats(
        random.randint(3, 18),
        random.randint(3, 18),
        random.randint(3, 18),
        random.randint(3, 18),
        random.randint(3, 18),
        random.randint(3, 18))

    stats = race.apply_bonus(stats)

    # TODO: get skills

    return Character(name, race.name, klass.name, stats)

c = make_character()
print(c)

# This is an attempt to create a D&D Character creator.
# The first rendition will create a Human Fighter from Fifth Edition Rules.

# def Fighter():
#     print "A Fighter gains the following Class Features:"
#     print "1d10 hit dice per fighter level"
#     print "Proficiency in all armor and weapons."
#     print "Saving throws are Strength and Constitution."
#     print "Choose two skills from the following:"
#     print "1. Acrobatics"
#     print "2. Animal Handling"
#     print "3. Athletics"
#     print "4. History"
#     print "5. Insight"
#     print "6. Intimidation"
#     print "7. Perception"
#     print "8. Survival"
#     acrobatics_chosen = False
#     animal_handling_chosen = False
#     athletics_chosen = False
#     history_chosen = False
#     insight_chosen = False
#     intimidation_chosen = False
#     perception_chosen = False
#     survival_chosen = False

# # How to choose only 2 and move to next step? Not sure yet. Maybe counting the "False" or "True" values.    
    
#     while True:
#         choice = raw_input(">")
  
#         if choice == "1" or "Acrobatics":
#             acrobatics_chosen = True
# #           Acrobatics()
#         elif choice == "2" or "Animal Handling":
#             animal_hanlding_chosen = True
# #           Animal Handling()
#         elif choice == "3" or "Athletics":
#             athletics_chosen = True
# #           Athletics()
#         elif choice == "4" or "History":
#             history_chosen = True
# #           History()
#         elif choice == "5" or "Insight":
#             insight_chosen = True
# #           Insight()
#         elif choice == "6" or "Intimidation":
#             intimidation_chosen = True
# #           Intimidation()
#         elif choice == "7" or "Perception":
#             perception_chosen = True
# #           Perception()
#         elif choice == "8" or "Survival":
#             survival_chosen = True
# #            Survival()
  

# def Human():
#     print "A Human receives +1 to all abilities."
#     print "Choose a class from the following:"
#     print "Fighter"
#     print "Druid"
#     print "Wizard"
#     print "Cleric"
#     print "Monk"
    
#     choice = raw_input(">")
  
#         if choice == "Fighter":
#             Fighter()
#         elif choice == "Druid":
#             Druid()
#         elif choice == "Wizard":
#             Wizard()
#         elif choice == "Cleric":
#             Cleric()
#         elif choice == "Monk":
#             Monk()
#         elif choice == "back":
#             start()
#         else
#             Human()
    
#   # strength
#   # dexterity
#   # constitution
#   # Intelligence
#   # Wisdom
#   # Charisma
  
# # +1 to all abilities

# def Dwarf():
# # +2 Strength, +2 Constitution, +1 Wisdom

# def Elf():
# # +2 Dexterity, +1 Intelligence, +1 Wisom

# def start():
#     print "Choose a race from the following:"
#     print "Human"
#     print "Dwarf"
#     print "Elf"
    
#     choice = raw_input(">")
  
#         if choice == "Human":
#             Human()
#         elif choice == "Dwarf":
#             Dwarf()
#         elif choice == "Elf":
#             Elf()
#         else
#             start()
  

# start()
