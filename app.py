import sys
from game.playground import Playground

class App:
    def run(self):
        if(len(sys.argv) >= 3):
            # sys.argv[0] represents the filename

            # Get initial details required to start game
            number_of_players = int(sys.argv[1])
            minimum_score = int(sys.argv[2])

            # Setup gameplay
            playground = Playground()
            playground.setup_gameplay(number_of_players, minimum_score)

        else:
            print('Input should be in the form of "python app.py <number_of_players> <minimum_score>"')


if __name__ == "__main__":
    App().run()