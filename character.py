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
