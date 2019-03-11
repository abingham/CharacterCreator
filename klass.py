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
        super(Druid, self).__init__('Druid', {'Arcana', 'Animal Handling', 'Insight', 'Medicine', 'Nature', 'Perception', 'Religion', 'Survival'})


class Cleric(Klass): 
    def __init__(self):
        super(Cleric, self).__init__('Cleric', {'History', 'Insight', 'Medicine', 'Persuasion', 'Religion'})


class Barbarian(Klass):    
    def __init__(self):
        super(Barbarian, self).__init__('Barbarian', {'Animal Handling', 'Athletics', 'Intimidation', 'Nature', 'Perception', 'Survival'})

# TODO: The other classes


# This is a tuple of all classes. A fancier technique would be to have the Klass
# base-class keep track of its subclasses.
ALL_KLASSES = (Fighter(), Druid(), Cleric(), Barbarian())
