import random

class Dice:
    @staticmethod
    def roll():
        ''' Simulates 6-faced dice roll '''
        return random.randint(1, 6)