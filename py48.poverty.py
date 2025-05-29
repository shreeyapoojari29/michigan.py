# Michigan County Poverty Statistics

def print_data(name, percent, count, income):
    print(f"{name.title()} County")
    print(f"  Percent of children in poverty:  {percent:.1f}")
    print(f"  Count of children in poverty:    {count:16,d}")
    print(f"  Median household income:       ${income:,.0f}")
    print()

def read_poverty_data(filename):
    data = {}
    with open(filename, 'r') as f:
        next(f)  # Skip the first line
        for line in f:
            try:
                name = line[193:239].strip().lower()
                values = line.strip().split()
                count = int(values[8])
                percent = float(values[11])
                income = int(values[20])
                data[name] = (percent, count, income)
            except (IndexError, ValueError):
                continue
    return data

def print_highest_data(data):
    highest = max(data.items(), key=lambda item: item[1][0])
    name, (percent, count, income) = highest
    print("Highest child poverty rate:")
    print_data(name, percent, count, income)

def print_lowest_data(data):
    lowest = min(data.items(), key=lambda item: item[1][0])
    name, (percent, count, income) = lowest
    print("Lowest child poverty rate:")
    print_data(name, percent, count, income)

def print_county_data(data):
    while True:
        user_input = input("Enter a county name or 'q' to quit: ").strip().lower()
        if user_input in ['q', 'quit']:
            print("Exiting.")
            break
        elif user_input in data:
            percent, count, income = data[user_input]
            print_data(user_input, percent, count, income)
        else:
            print("County not found.")

def main():
    filename = input("Enter file name: ")
    data = read_poverty_data(filename)
    print_highest_data(data)
    print_lowest_data(data)
    print_county_data(data)

if __name__ == "__main__":
    main()