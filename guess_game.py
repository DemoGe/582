import random

class GuessGame:
    
    def __init__(self):
        self.secret_number = self.generate_random_number()
        self.attempts = 0

    def generate_random_number(self):
        return random.randint(1000, 9999)

    def check_guess(self, guess):
        self.attempts += 1
        if guess == self.secret_number:
            return f"Congratulations! You guessed the correct number in {self.attempts} attempts."
        else:
            return self.compare_numbers(guess)

    def compare_numbers(self, guess):
        secret_str = str(self.secret_number)
        guess_str = str(guess)
        circles = 0
        crosses = 0
        for i in range(4):
            if guess_str[i] == secret_str[i]:
                circles += 1
            elif guess_str[i] in secret_str:
                crosses += 1
        return f"{circles} circles and {crosses} crosses"

def main():
    play_again = True

    while play_again:
        game = GuessGame()
        print("Welcome to the Guess the Number game!")
        print("Try to guess the 4-digit number.")
        
        while True:
            guess = input("Enter your guess (or 'q' to quit): ")
            
            if guess.lower() == 'q':
                print(f"The secret number was {game.secret_number}.")
                break
            
            try:
                guess = int(guess)
                if 1000 <= guess <= 9999:
                    result = game.check_guess(guess)
                    print(result)
                    if result.startswith("Congratulations!"):
                        break
                else:
                    print("Please enter a 4-digit number.")
            except ValueError:
                print("Invalid input. Please enter a 4-digit number or 'q' to quit.")
        
        play_again = input("Do you want to play again? (yes/no): ").lower() == 'yes'

if __name__ == "__main__":
    main()
