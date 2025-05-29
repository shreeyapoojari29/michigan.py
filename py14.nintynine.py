# CSE 231 – Fall 2011 – Project #2: Ninety-Nine Trick

def main():
    print("Welcome to the 99 Trick Game!")
    print("Here's how it works:")
    print("1. You will pick a secret number between 10 and 49.")
    print("2. We will calculate a 'magic' factor using that number.")
    print("3. Your friend will pick a number between 50 and 99.")
    print("4. A few calculations later... your number will be revealed!")
    print("-" * 50)

    secret_number = int(input("Enter your secret number (between 10 and 49): "))
    if not (10 <= secret_number <= 49):
        print("Invalid number. Please choose a number between 10 and 49.")
        return

    factor = 99 - secret_number

    friend_number = int(input("Ask your friend to choose a number (between 50 and 99): "))
    if not (50 <= friend_number <= 99):
        print("Invalid friend number. Please choose a number between 50 and 99.")
        return

    total = friend_number + factor

    hundreds_digit = total // 100
    last_two_digits = total % 100
    sum_of_digits = hundreds_digit + last_two_digits

    result = friend_number - sum_of_digits

    print("\nMagic is happening...\n")
    print(f"Original Secret Number: {secret_number}")
    print(f"Friend's Number: {friend_number}")
    print(f"Total (friend + factor): {total}")
    print(f"Hundreds digit: {hundreds_digit}")
    print(f"Last two digits: {last_two_digits}")
    print(f"Sum of digits removed: {sum_of_digits}")
    print(f"Final Result: {result}")

    if result == secret_number:
        print("\n🎉 It works! The secret number is revealed correctly.")
    else:
        print("\n❌ Something went wrong. Try again!")

main()
