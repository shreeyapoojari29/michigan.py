# Scrambled English Project


import random

def scramble_word(word_str):
    """Scramble the middle letters of a word, keeping first and last letters and punctuations in place."""
    if len(word_str) <= 3:
        return word_str

    
    end_punct = ''
    if not word_str[-1].isalpha():
        end_punct = word_str[-1]
        word_str = word_str[:-1]

    if len(word_str) <= 3:
        return word_str + end_punct

    first = word_str[0]
    middle = list(word_str[1:-1])
    last = word_str[-1]

    random.shuffle(middle)

    scrambled = first + ''.join(middle) + last + end_punct
    return scrambled

def scramble_line(line_str):
    """Scramble each word in a line."""
    words = line_str.split()
    scrambled_words = [scramble_word(word) for word in words]
    return ' '.join(scrambled_words)

def open_read_file(file_name_str):
    """Keep prompting until a file opens successfully for reading."""
    while True:
        try:
            file = open(file_name_str, 'r')
            return file
        except FileNotFoundError:
            print(f"Error: Cannot open file '{file_name_str}'. Please try again.")
            file_name_str = input("Enter input file name: ")

def main():
    output_file_name = input("Enter name of output file: ")
    input_file_name = input("Enter name of input file: ")

    infile = open_read_file(input_file_name)
    outfile = open(output_file_name, 'w')

    for line in infile:
        scrambled = scramble_line(line)
        outfile.write(scrambled + '\n')

    infile.close()
    outfile.close()

if __name__ == "__main__":
    main()
