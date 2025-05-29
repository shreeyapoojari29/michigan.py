# Best Seller Database Search

def read_file(filename):
    data = []
    with open(filename, "r") as f:
        for line in f:
            parts = line.strip().split("\t")
            if len(parts) == 5:
                title, author, publisher, date, category = parts
                data.append((title, author, publisher, date, category))
    return data

def year_range_search(data):
    start_year = input("Enter beginning year: ")
    end_year = input("Enter ending year: ")
    print(f"\nAll Titles between {start_year} and {end_year} :")
    found = False
    for entry in data:
        year = entry[3].split("/")[-1]
        if start_year <= year <= end_year:
            print(f"   {entry[0]}, by {entry[1]} ({entry[3]})")
            found = True
    if not found:
        print("   No titles found in that range.")

def month_year_search(data):
    month = input("Enter month (1-12): ").zfill(2)
    year = input("Enter year: ")
    print(f"\nAll titles from {month}/{year} :")
    found = False
    for entry in data:
        m, d, y = entry[3].split("/")
        if m == month and y == year:
            print(f"   {entry[0]}, by {entry[1]} ({entry[3]})")
            found = True
    if not found:
        print("   No titles found in that month and year.")

def author_search(data):
    search_term = input("Enter author name (or part of it): ").lower()
    print("\nMatching authors:")
    found = False
    for entry in data:
        if search_term in entry[1].lower():
            print(f"   {entry[0]}, by {entry[1]} ({entry[3]})")
            found = True
    if not found:
        print("   No matches found for that author.")

def title_search(data):
    search_term = input("Enter title (or part of it): ").lower()
    print("\nMatching titles:")
    found = False
    for entry in data:
        if search_term in entry[0].lower():
            print(f"   {entry[0]}, by {entry[1]} ({entry[3]})")
            found = True
    if not found:
        print("   No matches found for that title.")

def main():
    filename = input("Enter the name of the data file: ")
    data = read_file(filename)
    print("\nWhat would you like to do?")
    while True:
        print("\n1: Look up year range")
        print("2: Look up month/year")
        print("3: Search for author")
        print("4: Search for title")
        print("Q: Quit")
        choice = input("> ").strip().lower()

        if choice == '1':
            year_range_search(data)
        elif choice == '2':
            month_year_search(data)
        elif choice == '3':
            author_search(data)
        elif choice == '4':
            title_search(data)
        elif choice == 'q':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
