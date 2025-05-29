#Caesar Cipher encoder/decoder
def rotate_alphabet(shift):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    return alphabet[shift:] + alphabet[:shift]

def encode(text, rotation):
    normal = "abcdefghijklmnopqrstuvwxyz"
    rotated = rotate_alphabet(rotation)
    encoded = ""

    for char in text:
        if char in normal:
            index = normal.index(char)
            encoded += rotated[index]
        else:
            encoded += char
    return encoded

def decode(encoded_text, known_word):
    normal = "abcdefghijklmnopqrstuvwxyz"
    for rotation in range(1, 26):
        rotated = rotate_alphabet(rotation)
        decoded = ""

        for char in encoded_text:
            if char in rotated:
                index = rotated.index(char)
                decoded += normal[index]
            else:
                decoded += char

        if known_word in decoded:
            return rotation, decoded
    return None, None

def display_menu():
    print("Caesar Cipher Menu:")
    print("(e) Encode a message")
    print("(d) Decode a message using known word")
    print("(q) Quit")

def main():
    display_menu()
    while True:
        command = input("Enter a command (e)ncode, (d)ecode, or (q)uit: ").strip().lower()

        if command == 'e':
            text = input("Enter a string to encode: ")
            try:
                rotation = int(input("Enter a rotation amount (1–25): "))
                if 1 <= rotation <= 25:
                    result = encode(text, rotation)
                    print("Encoded string:", result)
                else:
                    print("Rotation must be between 1 and 25.")
            except ValueError:
                print("Please enter a valid integer.")
        
        elif command == 'd':
            text = input("Enter a string to decode: ")
            known = input("Enter a known word from the original message: ")
            rotation, result = decode(text, known)
            if result:
                print(f"Rotation used: {rotation}")
                print("Decoded string:", result)
            else:
                print("No valid rotation found.")

        elif command == 'q':
            print("Thanks for using the Caesar Cipher. Goodbye!")
            break
        else:
            print("Invalid command. Please try again.")
            display_menu()

if __name__ == "__main__":
    main()
