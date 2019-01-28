# menu with the options
import create
import random_character
import help_option


def menu():

    print('\nChoose an option: \n 0 - Quit \n 1 - Random Character \n 2 - Create Character \n 3 - Help')
    choice = input('\n Choice: ')
    # menu options
    if choice == "0":
        print('Goodbye.')

    elif choice == "1":
        random_character.generate()

    elif choice == "2":
        create.char()

    elif choice == "3":
        help_option.help_choice()

