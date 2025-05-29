#mastermind
def is_valid_guess(guess):
    if len(guess) != 4:
        print("**** guess must have length of 4, try again")
        return False
    if not guess.isdigit():
        print("**** contains non-numbers, try again")
        return False
    if len(set(guess)) != 4:
        print("**** no repeated digits, try again")
        return False
    return True

def evaluate_guess(key, guess):
    position = 0
    exist = 0

    for i in range(4):
        if guess[i] == key[i]:
            position += 1
        elif guess[i] in key:
            exist += 1

    return exist, position

def main():
    print("Welcome to Mastermind (Number Edition)!")
    key = input("What is the key: ")
    history = []
    guess_count = 0

    while True:
        guess = input("Guess: ")

        if not is_valid_guess(guess):
            continue

        guess_count += 1
        exist, position = evaluate_guess(key, guess)
        history.append(f"{guess}: exist:{exist}, position:{position}")

        # Display history
        for entry in history:
            print(entry)

        if guess == key:
            print(f"\nYou guessed the key: {key}")
            print(f"It took you {guess_count} guesses")
            break
        elif guess_count == 12:
            print(f"\nYou lose! The key was: {key}")
            break

if __name__ == "__main__":
    main()
