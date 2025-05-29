# Project 3: Square as sum of two triangular numbers

import math

def is_square(n):
    
    root = math.isqrt(n)
    return root * root == n

def triangular(n):
    
    return n * (n + 1) // 2

def main():
    try:
        square_num = int(input("Enter a square number: "))
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return

    if not is_square(square_num):
        print(f"{square_num} is not a perfect square.")
        return

    square_root = math.isqrt(square_num)

    tri1 = triangular(square_root)
    tri2 = triangular(square_root - 1)

    print(f"\n{square_num} is a square number.")
    print(f"It can be expressed as the sum of two triangular numbers:")
    print(f"{tri1} (T_{square_root}) + {tri2} (T_{square_root - 1}) = {square_num}")

if __name__ == "__main__":
    main()
