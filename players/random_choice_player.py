import random

class Random_Choice_Player():

    def __init__(self, color):
        self.color = color

    @staticmethod
    def make_move(possible_moves):
        return random.choice(possible_moves)

