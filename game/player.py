# Class to demonstrate Player
class Player:

    name = ''
    points = 0
    next_turn = True
    previous_roll = -1

    # Initializing the member variables
    def __init__(self, name):
        self.name = name
        self.points = 0
        self.next_turn = True
        self.previous_roll = -1

    def get_name(self):
        return self.name

    def get_points(self):
        return self.points

    def add_points(self, points):
        self.points += points

    def skip_next_turn(self, skip_turn):
        self.next_turn = skip_turn

    def can_play_next_turn(self):
        return self.next_turn

    def set_previous_roll(self, roll):
        self.previous_roll = roll

    def get_previous_roll(self):
        return self.previous_roll

    def __eq__(self, other):
        return self.name == other.name and self.points == other.points
