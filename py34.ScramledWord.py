import random

def scramble_word(word):

    punctuation = ''
    if word[-1] in '.,!?':
        punctuation = word[-1]
        word = word[:-1]

    if len(word) <= 3:
        return word + punctuation

    first, middle, last = word[0], list(word[1:-1]), word[-1]
    random.shuffle(middle)
    scrambled = first + ''.join(middle) + last

    return scrambled + punctuation

def main():
    infile_name = input("Enter input file name: ")
    outfile_name = input("Enter output file name: ")

    try:
        with open(infile_name, 'r') as infile, open(outfile_name, 'w') as outfile:
            for line in infile:
                words = line.strip().split()
                scrambled_line = [scramble_word(word) for word in words]
                outfile.write(' '.join(scrambled_line) + '\n')
        print(f"Scrambled output saved to '{outfile_name}'.")
    except FileNotFoundError:
        print("Error: File not found.")

if __name__ == "__main__":
    main()
