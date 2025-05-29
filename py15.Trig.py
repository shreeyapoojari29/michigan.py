# Trigonometry menu-based application without using math module

def display_menu():
    print("Menu:")
    print("A. Display the value of the factorial of N.")
    print("B. Display the value of the sine of X.")
    print("C. Display the value of the cosine of X.")
    print("M. Display the menu of options.")
    print("Q. Exit from the program.\n")

def get_factorial(n):
    if n < 0:
        return None
    fact = 1
    for i in range(2, n + 1):
        fact *= i
    return fact

def get_power(x, n):
    result = 1.0
    for _ in range(n):
        result *= x
    return result

def normalize_angle(x):
    pi = 3.141592653589793
    return x % (2 * pi)

def get_sine(x):
    x = normalize_angle(x)
    term = x
    total = 0.0
    k = 0
    while abs(term) >= 1.0e-8:
        term = ((-1)**k * get_power(x, 2*k + 1)) / get_factorial(2*k + 1)
        total += term
        k += 1
    return total

def get_cosine(x):
    x = normalize_angle(x)
    term = 1
    total = 0.0
    k = 0
    while abs(term) >= 1.0e-8:
        term = ((-1)**k * get_power(x, 2*k)) / get_factorial(2*k)
        total += term
        k += 1
    return total

def main():
    display_menu()
    while True:
        choice = input("Enter choice: ").strip().lower()

        if choice == 'a':
            try:
                n = int(input("Enter an integer: "))
                fact = get_factorial(n)
                if fact is None:
                    print("Factorial is not defined for negative integers.")
                else:
                    print("Result:", fact)
            except ValueError:
                print("Invalid input. Please enter an integer.")
        
        elif choice == 'b':
            try:
                x = float(input("Enter a value in radians: "))
                result = get_sine(x)
                print("Result:", result)
            except ValueError:
                print("Invalid input. Please enter a number.")
        
        elif choice == 'c':
            try:
                x = float(input("Enter a value in radians: "))
                result = get_cosine(x)
                print("Result:", result)
            except ValueError:
                print("Invalid input. Please enter a number.")
        
        elif choice == 'm':
            display_menu()
        
        elif choice == 'q':
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
