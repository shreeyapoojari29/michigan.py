# Project 1: National Debt Visualizer

THICKNESS_INCHES = 0.0043      
INCHES_PER_MILE = 63360 
DISTANCE_TO_MOON = 238857 

def main():
 
    debt_str = input("Enter the national debt (in dollars): ")
    denom_str = input("Enter the denomination of the bill: ")

 
    try:
        debt = float(debt_str)
        denomination = float(denom_str)

        if denomination == 0:
            print("Error: Bill denomination cannot be zero.")
            return

    except ValueError:
        print("Invalid input. Please enter numerical values only.")
        return


    num_bills = debt / denomination

 
    total_inches = num_bills * THICKNESS_INCHES

 
    height_miles = total_inches / INCHES_PER_MILE

    moon_multiples = height_miles / DISTANCE_TO_MOON


    print("\n--- National Debt Visualization ---")
    print(f"Height of {denomination}-dollar bills: {height_miles:,.2f} miles")
    print(f"That's {moon_multiples:.2f} times the distance to the moon!")

if __name__ == "__main__":
    main()
