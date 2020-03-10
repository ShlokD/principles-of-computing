import unittest
import solitairemancala

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.game = solitairemancala.SolitaireMancala()

    def test_set_a_configuration(self):
        result = [0, 1, 1]
        self.game.set_board([0, 1, 1])
        self.assertListEqual(self.game._board, result)

    def test_get_str_repr(self):
        result = "1, 1, 0"
        self.game.set_board([0, 1, 1])
        self.assertEqual(str(self.game), result)

    def test_get_number_of_seeds(self):
        result = 2
        self.game.set_board([0, 1, 2, 3])
        self.assertEqual(self.game.get_num_seeds(2), result)


    def test_is_legal_move_for_house_zero(self):
        result = False
        self.game.set_board([0, 1, 2, 3])
        self.assertEqual(self.game.is_legal_move(0), result)

    def test_is_legal_move_for_house_with_nonmatching_seeds(self):
        result = False
        self.game.set_board([0, 2, 2, 5])
        self.assertEqual(self.game.is_legal_move(1), result)

    def test_is_legal_move_for_house_with_matching_seeds(self):
        result = True
        self.game.set_board([0, 2, 2, 5])
        self.assertEqual(self.game.is_legal_move(2), result)

    def test_choose_move(self):
        result = 1
        self.game.set_board([0, 1, 1, 3, 0, 0, 0])
        self.assertEqual(self.game.choose_move(), result)

    def test_apply_move(self):
        result = "4, 4, 0, 3, 1"
        self.game.set_board([0, 2, 2, 4, 4])
        move = self.game.choose_move()
        self.game.apply_move(move)
        self.assertEqual(str(self.game), result)

    def test_is_game_won_for_a_incomplete_game(self):
        result = False
        self.game.set_board([0, 2, 3, 1, 0])
        self.assertEqual(self.game.is_game_won(), result)

    def test_is_game_won_for_a_complete_game(self):
        result = True
        self.game.set_board([4, 0, 0, 0])
        self.assertEqual(self.game.is_game_won(), result)

    def test_plan_moves(self):
        result = [1, 2, 1, 3, 1]
        self.game.set_board([0, 1, 2, 3])
        self.assertEqual(self.game.plan_moves(), result)

if __name__ == '__main__':
    unittest.main()
