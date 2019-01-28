
import random

# defining function
def char():

    name = input("Enter character name: ")
    gender = input("Choose character gender :\n  1- Male 2 - Female 3 - Other \n")

    if gender == "1":
        gender_choice = "Male"
    elif gender == "2":
        gender_choice = "Female"
    elif gender == "3":
        gender_choice = "Other"

    print("Generating stats...(Press any key to continue")

    strength = random.randint(4, 10)
    intel = random.randint(4, 10)
    agility = random.randint(4, 10)


    print(name, gender_choice, strength, intel, agility)
