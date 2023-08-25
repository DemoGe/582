import random


class GuessGame:

    def __init__(self):
        """
        Generate a random four-digit number as the secret number, and initialize the number of attempts.
        """
        self.secret_number = self.generate_random_number()
        self.attempts = 0

    def generate_random_number(self):
        """
        Generate a random four-digit number as the secret number.
        """
        return random.randint(1000, 9999)

    def check_guess(self, guess):
        self.attempts += 1
        if guess == self.secret_number:
            return f"Congratulations! You guessed the correct number in {self.attempts} attempts."
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
                # If the digit is correct and in the correct position, mark it as 'X'
                result[i] = 'X'
        return ''.join(result)

    def display_game_result(self):
        """
        Display the number of attempts made by the player and ask if they want to play again.
        """
        print(f"Total attempts: {self.attempts}")
        play_again = input("Do you want to play again? (yes/no): ").lower()
        return play_again == 'yes'


def main():
    play_again = True
    # Start the game loop
    while play_again:
        game = GuessGame()
        print("Welcome to the Guess the Number game!")
        print("Try to guess the 4-digit number.")
        # Start the guessing loop for the current game
        while True:
            guess = input("Enter your guess (or 'q' to quit): ")

            if guess.lower() == 'q':
                print(f"The secret number was {game.secret_number}.")
                break

            try:
                guess = int(guess)
                if 1000 <= guess <= 9999:
                    # Check the player's guess and get feedback
                    result = game.check_guess(guess)
                    print(result)
                    # If the player wins, exit the guessing loop
                    if result.startswith("Congratulations!"):
                        break
                else:
                    print("Please enter a 4-digit number.")
            except ValueError:
                print("Invalid input. Please enter a 4-digit number or 'q' to quit.")
        # Display the game result and ask if the player wants to play again
        play_again = game.display_game_result()
        if play_again != 'yes':
            break


if __name__ == "__main__":
    main()
