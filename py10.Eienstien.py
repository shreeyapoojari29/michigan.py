# Einstein's 1089 puzzle

def main():
    print("Welcome to the Einstein 1089 Puzzle!")
    print("Start with any 3-digit number where the first and last digits differ by at least 2.")
    print("We'll walk you through the magical math process... 🤯\n")

    num = int(input("Enter a 3-digit number (first and last digits must differ by ≥ 2): "))

    hundreds = num // 100
    tens = (num // 10) % 10
    ones = num % 10
    reversed_num = ones * 100 + tens * 10 + hundreds

    print(f"Your number: {num}")
    print(f"Reversed number: {reversed_num}")

    diff = abs(num - reversed_num)
    print(f"Difference: {diff}")

    d_hundreds = diff // 100
    d_tens = (diff // 10) % 10
    d_ones = diff % 10
    reversed_diff = d_ones * 100 + d_tens * 10 + d_hundreds

    print(f"Reversed difference: {reversed_diff}")

    final_result = diff + reversed_diff
    print(f"Sum of difference and reversed difference: {final_result}")

if __name__ == "__main__":
    main()
