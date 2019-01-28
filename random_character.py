# code to generate random character

import random


def generate():

    vowel = ['a', 'e', 'i', 'o', 'u']
    consonant = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']

    # Generate random stats
    type1 = ['Warrior\n', 'Mage\n', 'Assassin\n', 'Archer\n', 'Priest\n', 'Knight\n', 'Druid\n']
    type2 = random.choice(type1)
    gender1 = ['Female\n', 'Male\n', 'Other\n']
    gender2 = random.choice(gender1)
    strength = random.randint(4, 10)
    intel = random.randint(4, 10)
    agility = random.randint(4, 10)

    # Name generator
    n1 = random.choice(consonant).upper()
    n2 = random.choice(vowel)
    n3 = random.choice(consonant)
    n4 = random.choice(consonant)
    n5 = random.choice(vowel)
    n6 = random.choice(consonant)

    # Print the character information
    name = (n1 + n2 + n3 + n4 + n5 + n6)
    print("\n", name)
    print("\nClass Type: ", type2)
    print("Gender: ", gender2)
    print("Strength: ", strength, "Intelligence: ", intel, "Agility: ", agility)

    accept = input('Accept character? (Y/N)')

    # option to accept created character
    if accept == "Y" or accept == "y":
        print("Good luck in your adventure!")
    elif accept == "N" or accept == "n":
        print("Character Cancelled")



