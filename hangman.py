import random

def play_hangman():
    words = ["python", "hangman", "developer", "internship", "programming"]
    word = random.choice(words)
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")
    print(f"You have {attempts} incorrect guesses allowed.\n")

    while attempts > 0:
        # Build the display word, e.g. p _ t h _ n
        display_word = ""
        for letter in word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "
        print(display_word)

        # Check win condition
        if "_" not in display_word:
            print("\n🎉 Congratulations! You guessed the word:", word)
            break

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.\n")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.\n")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("✅ Correct!\n")
        else:
            attempts -= 1
            print(f"❌ Wrong! You have {attempts} attempts left.\n")

    if attempts == 0:
        print(f"\n💀 Game over! The word was: {word}")

if __name__ == "__main__":
    play_hangman()