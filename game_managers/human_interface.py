from game.human_vs_computer import Human_Vs_Computer
from game.human_vs_human import Human_Vs_Human
from game.computer_vs_computer import Computer_vs_Computer

import random

class Human_Interface:

    def __init__(self):
        self.options = [
            'Human vs Human',
            'Human vs Computer',
            'Computer vs Computer',
        ]
        self.color_options = [
            'black',
            'white',
        ]

    def display_menu(self):
        print('''
Welcome to CLI Checkers, used for training neural net checkers.
You are running the human friendly interface, and as such are 
given options to interact with the program. Do not run this 
game manager for training, try the nn game manager instead.
---------------------------------------------------------------''')
        for index, item in enumerate(self.options):
            print(f'{index}: {item}')
        print('---------------------------------------------------------------')

    def get_colors(self):
        while True:
            print('Black goes First.')
            for index, color in enumerate(self.color_options):
                print(f'{index}: {color}')
            human_color = input('Enter number for human color: ')
            computer_color = input('Enter number for computer color: ')
            try:
                if int(human_color) in [0, 1] and int(computer_color) in [0, 1]:
                    return int(human_color), int(computer_color)
                    break
            except ValueError:
                print('Invalid Selections.')

    def run(self):
        self.display_menu()
        while True:
            menu_choice = input('Enter Selection: ')
            try:
                menu_choice_as_int = int(menu_choice)
                self.options[menu_choice_as_int]
                break
            except ValueError:
                print('Invalid Entry. Try Again.')
            except IndexError:
                print('Invalid Menu Index. Try Again.')
        if menu_choice_as_int == 0:
            game = Human_Vs_Human()
        if menu_choice_as_int == 1:
            human_color, computer_color = self.get_colors()
            game = Human_Vs_Computer(human_color, computer_color)
        if menu_choice_as_int == 2:
            game = Computer_vs_Computer()

        game.run_game()
