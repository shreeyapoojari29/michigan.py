# CSE 231 – Spring 2009 – Project #5: Pascal's Triangle

def generate_pascals_triangle(height):
    triangle = []

    for i in range(height):
        if i == 0:
            triangle.append([1])
        elif i == 1:
            triangle.append([1, 1])
        else:
            prev_row = triangle[-1]
            new_row = [1]
            for j in range(1, len(prev_row)):
                new_row.append(prev_row[j-1] + prev_row[j])
            new_row.append(1)
            triangle.append(new_row)
    return triangle

def print_pascals_triangle(triangle):
    height = len(triangle)
    width = height * 4

    for row in triangle:
        row_str = '   '.join(map(str, row))
        print(row_str.center(width))

def main():
    while True:
        try:
            height = int(input("Enter the height of Pascal's Triangle (positive integer): "))
            if height > 0:
                break
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

    triangle = generate_pascals_triangle(height)
    print("\nPascal's Triangle of height", height)
    print_pascals_triangle(triangle)

if __name__ == "__main__":
    main()
