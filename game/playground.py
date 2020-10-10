from player import Player
from dice import Dice
import random

class Playground:

    number_of_players = 0
    players = []
    winners = []
    minimum_score = 0

    def setup_gameplay(self, number_of_players, minimum_score):
        ''' Setups required variables and instantiates components '''
        self.number_of_players = number_of_players
        self.minimum_score = minimum_score

        if self.number_of_players < 2:
            print('Game can only be played between 2 or more players')

        if self.minimum_score < 0:
            print('Game can only be played if target is grater than 0')
        else:
            # Initializing Players
            for i in range(0, self.number_of_players):
                name = 'Player ' + str(i+1)
                player = Player(name)
                self.players.append(player)

            # Starting the Game
            self.start_game()

    def start_game(self):
        ''' Decides turn order and plays a move '''
        random.shuffle(self.players)
        while True:
            for player in self.players:
                if player.can_play_next_turn():
                    self.play_move(player, 0)
                else:
                    player.skip_next_turn(False)

    def announce_winner(self, player):
        ''' Separated the winner list '''
        self.winners.append(player)
        print(player.get_name() + " has achieved the target.")
        self.players.remove(player)

    def play_move(self, player, continous_move_count):
        ''' Rolls the dice and process the move '''
        raw_input(player.get_name() + "'s turn. Press Enter to roll the dice...")
        dice_rolled = Dice.roll()
        print(dice_rolled)

        if dice_rolled == 1:
            if player.get_previous_roll == 1:
                player.skip_next_turn(True)
            player.add_points(dice_rolled)
            if player.get_points() >= self.minimum_score:
                self.announce_winner(player)
            self.calculate_rank()
        elif dice_rolled == 6:
            player.add_points(dice_rolled)
            if player.get_points() >= self.minimum_score:
                self.announce_winner(player)
                self.calculate_rank()
            else:
                self.calculate_rank()
                print(player.get_name() + " got another turn")
                self.play_move(player, continous_move_count+1)
        else:
            player.add_points(dice_rolled)
            if player.get_points() >= self.minimum_score:
                self.announce_winner(player)
            self.calculate_rank()

        player.set_previous_roll(dice_rolled)

    def calculate_rank(self):
        ''' Calculates the rank of currently playing players & displays ranking tables '''
        # Need to preserve actual list to preserve actual order of turns
        copied_players_list = self.players[:]
        self.sort_by_points(copied_players_list)

        print '-'*30

        print('Winner Table (Rankwise)')
        if len(self.winners) == 0:
            print('(Empty Table)')
        else:
            for i in range(0, len(self.winners)):
                print self.winners[i].get_name(), '-', str(self.winners[i].get_points()), 'points'

        print '-'*30

        print('Current Players (Rankwise)')
        if len(self.players) == 0:
            print('(Empty Table)')
        else:
            for i in range(0, len(self.players)):
                print copied_players_list[i].get_name(), '-', str(copied_players_list[i].get_points()), 'points'

        print '-'*30
        print('\n')


    def sort_by_points(self, players):
        ''' Sorts the currently playing players on the basis of points using merge sort '''
        if len(players) > 1:
            mid = len(players)//2
            left = players[:mid]
            right = players[mid:]

            self.sort_by_points(left)
            self.sort_by_points(right)

            i = j = k = 0

            while i < len(left) and j < len(right):
                if left[i].get_points() > right[j].get_points():
                    players[k] = left[i]
                    i+= 1
                else:
                    players[k] = right[j]
                    j+= 1
                k+= 1

            while i < len(left):
                players[k] = left[i]
                i+= 1
                k+= 1

            while j < len(right):
                players[k] = right[j]
                j+= 1
                k+= 1
