# Project 2: MacArthur Number Trick

def main():
    print("Welcome to the Douglas MacArthur 'Old 115' Number Trick!")
    print("I'll ask for your birth month and age, and show you a 'magic' number...")
    print("Then I'll magically tell you your birth month and age from it!\n")


    month = int(input("Enter the number of your birth month (1-12): "))
    age = int(input("Enter your age (0-99): "))

    result = (((month * 2) + 5) * 50) + age
    magic_number = result - 365

    print(f"\nHere's your magic number: {magic_number}")

    
    final_number = magic_number + 115

    age_guessed = final_number % 100
    month_guessed = final_number // 100

    print("\nLet me guess...")
    print(f"You were born in month #{month_guessed} and you're {age_guessed} years old!")

if __name__ == "__main__":
    main()
