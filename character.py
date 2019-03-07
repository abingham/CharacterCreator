from sys import exit

# This is an attempt to create a D&D Character creator.
# The first rendition will create a Human Fighter from Fifth Edition Rules.

def Fighter():
    print "A Fighter gains the following Class Features:"
    print "1d10 hit dice per fighter level"
    print "Proficiency in all armor and weapons."
    print "Saving throws are Strength and Constitution."
    print "Choose two skills from the following:"
    print "1. Acrobatics"
    print "2. Animal Handling"
    print "3. Athletics"
    print "4. History"
    print "5. Insight"
    print "6. Intimidation"
    print "7. Perception"
    print "8. Survival"
    acrobatics_chosen = False
    animal_handling_chosen = False
    athletics_chosen = False
    history_chosen = False
    insight_chosen = False
    intimidation_chosen = False
    perception_chosen = False
    survival_chosen = False
    
    while True:
        choice = raw_input(">")
  
        if choice == "1" or "Acrobatics":
            acrobatics_chosen = True
#           Acrobatics()
        elif choice == "2" or "Animal Handling":
            animal_hanlding_chosen = True
#           Animal Handling()
        elif choice == "3" or "Athletics":
            athletics_chosen = True
#           Athletics()
        elif choice == "4" or "History":
            history_chosen = True
#           History()
        elif choice == "5" or "Insight":
            insight_chosen = True
#           Insight()
        elif choice == "6" or "Intimidation":
            intimidation_chosen = True
#           Intimidation()
        elif choice == "7" or "Perception":
            perception_chosen = True
#           Perception()
        elif choice == "8" or "Survival":
            survival_chosen = True
#            Survival()
  

def Human():
    print "A Human receives +1 to all abilities."
    print "Choose a class from the following:"
    print "Fighter"
    print "Druid"
    print "Wizard"
    print "Cleric"
    print "Monk"
    
    choice = raw_input(">")
  
        if choice == "Fighter":
            Fighter()
        elif choice == "Druid":
            Druid()
        elif choice == "Wizard":
            Wizard()
        elif choice == "Cleric":
            Cleric()
        elif choice == "Monk":
            Monk()
        elif choice == "back":
            start()
        else
            Human()
    
  # strength
  # dexterity
  # constitution
  # Intelligence
  # Wisdom
  # Charisma
  
# +1 to all abilities

def Dwarf():
# +2 Strength, +2 Constitution, +1 Wisdom

def Elf():
# +2 Dexterity, +1 Intelligence, +1 Wisom

def start():
    print "Choose a race from the following:"
    print "Human"
    print "Dwarf"
    print "Elf"
    
    choice = raw_input(">")
  
        if choice == "Human":
            Human()
        elif choice == "Dwarf":
            Dwarf()
        elif choice == "Elf":
            Elf()
        else
            start()
  

start()
