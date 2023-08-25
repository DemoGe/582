import unittest
from guess_game import GuessGame


class TestGuessGame(unittest.TestCase):

    def test_generate_random_number(self):
        game = GuessGame()
        number = game.generate_random_number()
        # Check if the generated number is an integer
        self.assertTrue(isinstance(number, int))
        # Check if the number is within the valid range
        self.assertTrue(1000 <= number <= 9999)

    def test_compare_numbers(self):
        """
        Test the 'compare_numbers' method of the GuessGame class.
        It checks if the feedback message is correctly generated based on the player's guess.
        """
        game = GuessGame()
        game.secret_number = 1234

        # Test when all digits are correct and in the correct position
        result1 = game.compare_numbers(1234)
        # Expected feedback: 'OOOO'
        self.assertEqual(result1, "OOOO")

        # Test when all digits are correct but in the wrong position
        result2 = game.compare_numbers(4321)
        # Expected feedback: 'XXXX'
        self.assertEqual(result2, "XXXX")

        # Test when some digits are correct and in the correct position, some are correct but in the wrong position
        result3 = game.compare_numbers(1243)
        # Expected feedback: 'OOXX'
        self.assertEqual(result3, "OOXX")

        # Test when none of the digits are correct
        result4 = game.compare_numbers(5678)
        # Expected feedback: ''
        self.assertEqual(result4, "")


if __name__ == '__main__':
    unittest.main()
