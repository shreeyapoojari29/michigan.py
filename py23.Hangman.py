#Hangman Game


def display_phrase(secret, guessed_letters):
    result = ""
    for char in secret:
        if char.lower() in guessed_letters or not char.isalpha():
            result += char
        else:
            result += "_"
    return result

def is_game_won(secret, guessed_letters):
    for char in secret:
        if char.isalpha() and char.lower() not in guessed_letters:
            return False
    return True

def main():
    print("Welcome to Hangman!")
    secret = input("Enter a word or phrase: ").strip()
    print("\n" * 50)  # Hide input

    guessed_letters = []
    wrong_guesses = []
    max_wrong = 6

    while True:
        current = display_phrase(secret, guessed_letters)
        print("\nCurrent: ", ' '.join(current))
        print("Incorrect guesses:", ' '.join(wrong_guesses))
        print("Remaining guesses:", max_wrong - len(wrong_guesses))

        if is_game_won(secret, guessed_letters):
            print("Congratulations! You guessed it!")
            break
        if len(wrong_guesses) >= max_wrong:
            print("You've run out of guesses. You lose!")
            print("The phrase was:", secret)
            break

        guess = input("Guess a letter: ").strip().lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabetical character.")
            continue
        if guess in guessed_letters or guess in wrong_guesses:
            print("You already guessed that letter.")
            continue

        if guess in secret.lower():
            guessed_letters.append(guess)
        else:
            wrong_guesses.append(guess)

if __name__ == "__main__":
    main()
