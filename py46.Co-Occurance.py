# Co-Occurrence Text Search Tool

import string

def open_file():
    while True:
        try:
            filename = input("Enter filename: ")
            return open(filename, 'r')
        except FileNotFoundError:
            print("File not found. Try again.")

def read_data(fp):
    word_dict = {}
    line_num = 1
    for line in fp:
        line = line.lower()
        line = line.translate(str.maketrans("", "", string.punctuation))
        words = line.strip().split()

        for word in words:
            if word.isalpha() and len(word) >= 2:
                if word not in word_dict:
                    word_dict[word] = set()
                word_dict[word].add(line_num)

        line_num += 1
    return word_dict

def find_cooccurance(D, inp_str):
    words = inp_str.lower().strip().split()
    sets = []

    for word in words:
        if word in D:
            sets.append(D[word])
        else:
            return None  # one word not found = no co-occurrence

    if sets:
        result = set.intersection(*sets)
        return sorted(result) if result else None
    else:
        return None

def main():
    fp = open_file()
    word_dict = read_data(fp)
    fp.close()

    while True:
        user_input = input("Enter search words or 'q' to quit: ").strip()
        if user_input.lower() == 'q':
            print("Exiting.")
            break
        result = find_cooccurance(word_dict, user_input)
        if result:
            print("Lines:", *result)
        else:
            print("Lines: None.")


if __name__ == "__main__":
    main()
