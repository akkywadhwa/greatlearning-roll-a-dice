import unittest
from ..game.playground import Playground
from ..game.player import Player


class TestPlayground(unittest.TestCase):

    def test_sort_by_points(self):
        players = []
        p1 = Player('Player 1')
        p1.add_points(5)
        p2 = Player('Player 2')
        p2.add_points(10)
        p3 = Player('Player 3')
        p3.add_points(2)

        players.append(p1)
        players.append(p2)
        players.append(p3)

        playground = Playground()
        playground.sort_by_points(players)

        expected_list = [p2, p1, p3]

        self.assertListEqual(players, expected_list)

if __name__ == '__main__':
    unittest.main()
