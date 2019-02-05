
import random


# defining function
def char():

    name = input("Enter character name: ")
    class_type = input("Choose Class Type:\n 1-Warrior 2- Mage  3- Assassin  4- Archer 5- Priest  6- Knight  7- Druid\n")

    # choice for choosing a class type
    if class_type == "1":
        type_choice = "Warrior"
    elif class_type == "2":
        type_choice = "Mage"
    elif class_type == "3":
        type_choice = "Assassin"
    elif class_type == "4":
        type_choice = "Archer"
    elif class_type == "5":
        type_choice = "Priest"
    elif class_type == "6":
        type_choice = "Knight"
    elif class_type == "7":
        type_choice = "Druid"

    gender = input("Choose character gender :\n  1- Male 2 - Female 3 - Other \n")

    # choice for choosing a gender
    if gender == "1":
        gender_choice = "Male"
    elif gender == "2":
        gender_choice = "Female"
    elif gender == "3":
        gender_choice = "Other"

    input("Generating stats...(Press Enter to continue)")

    # generating random stats
    strength = random.randint(4, 10)
    intel = random.randint(4, 10)
    agility = random.randint(4, 10)

    print("\n", name)
    print("\nClass Type: ", type_choice)
    print("Gender: ", gender_choice)
    print("Strength: ", strength, "Intelligence: ", intel, "Agility: ", agility)

    accept = input('Accept character? (Y/N)')

    # option to accept created character
    if accept == "Y" or accept == "y":
        print("\nGood luck in your adventure!")
    elif accept == "N" or accept == "n":
        print("\nCharacter Cancelled")

