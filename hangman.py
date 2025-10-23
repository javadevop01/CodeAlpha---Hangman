import random

def display_hangman(tries):
    stages = [
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |      
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|
           |      |
           |     
           -
        """,
        """
           --------
           |      |
           |      O
           |      |
           |      |
           |     
           -
        """,
        """
           --------
           |      |
           |      O
           |    
           |      
           |     
           -
        """,
        """
           --------
           |      |
           |      
           |    
           |      
           |     
           -
        """
    ]
    return stages[tries]

def play_hangman():
    # Small list of 5 predefined words
    words = ["python", "coding", "intern", "github", "laptop"]
    
    # Choose a random word
    word = random.choice(words)
    word_letters = list(word)
    guessed_letters = []
    word_display = ["_"] * len(word)
    tries = 6
    
    print("Welcome to Hangman!")
    print("You have 6 incorrect guesses allowed.")
    print("\n" + " ".join(word_display))
    
    # Main game loop
    while tries > 0:
        print(display_hangman(tries))
        print("Word: " + " ".join(word_display))
        print(f"Guessed letters: {', '.join(guessed_letters) if guessed_letters else 'None'}")
        print(f"Tries remaining: {tries}")
        
        # Get user input
        guess = input("\nGuess a letter: ").lower()
        
        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter!")
            continue
        
        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue
        
        guessed_letters.append(guess)
        
        # Check if guess is in the word
        if guess in word_letters:
            print(f"Good guess! '{guess}' is in the word.")
            for i in range(len(word)):
                if word[i] == guess:
                    word_display[i] = guess
            
            # Check if won
            if "_" not in word_display:
                print("\n🎉 Congratulations! You won!")
                print(f"The word was: {word}")
                break
        else:
            tries -= 1
            print(f"Wrong! '{guess}' is not in the word.")
            
            if tries == 0:
                print(display_hangman(tries))
                print("\n💀 Game Over! You ran out of tries.")
                print(f"The word was: {word}")
    
    # Ask to play again
    play_again = input("\nWould you like to play again? (yes/no): ").lower()
    if play_again == "yes" or play_again == "y":
        print("\n" + "="*40 + "\n")
        play_hangman()
    else:
        print("Thanks for playing!")

# Start the game
if __name__ == "__main__":
    play_hangman()  