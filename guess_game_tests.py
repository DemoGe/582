import unittest
from guess_game import GuessGame

class TestGuessGame(unittest.TestCase):
    
    def test_generate_random_number(self):
        game = GuessGame()
        number = game.generate_random_number()
        self.assertTrue(isinstance(number, int))
        self.assertTrue(1000 <= number <= 9999)

    def test_guess_correct_number(self):
        game = GuessGame()
        game.secret_number = 1234
        result = game.check_guess(1234)
        self.assertEqual(result, "Congratulations! You guessed the correct number in 1 attempts.")

    def test_guess_incorrect_number(self):
        game = GuessGame()
        game.secret_number = 1234
        result = game.check_guess(5678)
        self.assertEqual(result, "0 circles and 0 crosses")

    def test_guess_partial_correct_number(self):
        game = GuessGame()
        game.secret_number = 1234
        result = game.check_guess(1243)
        self.assertEqual(result, "2 circles and 2 crosses")

if __name__ == '__main__':
    unittest.main()
