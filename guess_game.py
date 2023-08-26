import random


class GuessGame:

    def __init__(self):
        """
        Generate a random four-digit number as the secret number, and initialize the number of attempts.
        """
        self.secret_number = self.generate_random_number()
        # Used to record all attempts
        self.total_attempts = 0
        # Used to record the number of failures in the current game
        self.failed_attempts = 0

    def generate_random_number(self):
        """
        Generate a random four-digit number as the secret number.
        """
        return random.randint(1000, 9999)

    def check_guess(self, guess):
        self.total_attempts += 1
        if guess == self.secret_number:
            return f"Congratulations! You guessed the correct number in {self.total_attempts} attempts."
        else:
            return self.compare_numbers(guess)

    def compare_numbers(self, guess):
        """
        Compare the player's guess with the secret number and generate a feedback message.
        """
        secret_str = str(self.secret_number)
        guess_str = str(guess)
        result = [''] * 4

        for i in range(4):
            if guess_str[i] == secret_str[i]:
                # If the digit is correct and in the correct position, mark it as 'O'
                result[i] = 'O'
            elif guess_str[i] in secret_str:
                # If the digit is correct and in the incorrect position, mark it as 'X'
                result[i] = 'X'
        return ''.join(result)

    def display_game_result(self):
        """
        Display the number of attempts made by the player and ask if they want to play again.
        """
        print(f"Total attempts: {self.total_attempts}")
        play_again = input("Do you want to play again? (yes/no): ").lower()
        return play_again == 'yes'

    def restart_game(self):
        """
        Start a new game by initializing the game object and entering the game loop.
        """
        self.secret_number = self.generate_random_number()
        self.failed_attempts = 0  # Reset the number of failures for the current game
        print("Welcome to the Guess the Number game!")
        print("Try to guess the 4-digit number.")
        # Start the guessing loop for the current game
        while True:
            guess = input("Enter your guess (or 'q' to quit): ")

            if guess.lower() == 'q':
                print(f"The secret number was {self.secret_number}.")
                # Accumulate the number of failures of the current game to the total number of failures
                self.total_attempts += self.failed_attempts
                # Reset the number of failures for the current game
                self.failed_attempts = 0
                break

            try:
                guess = int(guess)
                if 1000 <= guess <= 9999:
                    # Check the player's guess and get feedback
                    result = self.check_guess(guess)
                    print(result)
                    # If the player wins, exit the guessing loop
                    if result.startswith("Congratulations!"):
                        break
                else:
                    print("Please enter a 4-digit number.")
                    self.failed_attempts += 1
            except ValueError:
                print("Invalid input. Please enter a 4-digit number or 'q' to quit.")


def main():
    play_again = True
    while play_again:
        game = GuessGame()  # Initialize a new game object
        game.restart_game()  # Call the restart_game function to start a new game
        play_again = game.display_game_result()


if __name__ == "__main__":
    main()
