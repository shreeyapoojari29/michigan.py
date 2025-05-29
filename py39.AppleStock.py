# Apple Stock Monthly Averages

def get_input_descriptor():
    while True:
        try:
            filename = input("Open what file: ")
            return open(filename, 'r')
        except FileNotFoundError:
            print("File not found. Try again.")

def get_data_list(fp, column):
    data = []
    next(fp)  # Skip header
    for line in fp:
        parts = line.strip().split(',')
        if len(parts) <= column:
            continue
        try:
            date = parts[0]
            value = float(parts[column])
            data.append((date, value))
        except ValueError:
            continue
    return data

def average_data(data_list):
    monthly_totals = {}
    for date, value in data_list:
        year, month, _ = date.split('-')
        key = f"{month}-{year}"
        if key not in monthly_totals:
            monthly_totals[key] = []
        monthly_totals[key].append(value)
    
    monthly_averages = []
    for key in monthly_totals:
        avg = sum(monthly_totals[key]) / len(monthly_totals[key])
        monthly_averages.append((avg, key))
    return monthly_averages

def print_results(averages):
    averages.sort()
    print("\nLowest 6 for column")
    for avg, key in averages[:6]:
        print(f"Date:{key}, Value:{avg:8.2f}")
    
    print("\nHighest 6 for column")
    for avg, key in sorted(averages[-6:], reverse=True):
        print(f"Date:{key}, Value:{avg:8.2f}")

def main():
    fp = get_input_descriptor()
    while True:
        try:
            col = int(input("What column: "))
            if 0 <= col <= 6:
                break
            else:
                print("Column must be between 0 and 6.")
        except ValueError:
            print("Invalid input, please enter a number.")
    
    data_list = get_data_list(fp, col)
    fp.close()
    
    monthly_avg = average_data(data_list)
    print_results(monthly_avg)

if __name__ == "__main__":
    main()
