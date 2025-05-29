# Caesar Cipher Cracker - Project 5

def read_cipher_text(filename):
    with open(filename, 'r') as file:
        text = file.read()
    return text

def get_letter_frequencies(text):
    freq = [0] * 26
    for char in text.lower():
        if char.isalpha():
            index = ord(char) - ord('a')
            freq[index] += 1
    return freq

def find_shift(frequencies):
    max_freq = max(frequencies)
    max_index = frequencies.index(max_freq)
    shift = (max_index - (ord('e') - ord('a'))) % 26
    return shift

def decrypt(text, shift):
    decrypted = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            index = (ord(char) - base - shift) % 26
            decrypted += chr(base + index)
        else:
            decrypted += char
    return decrypted

def main():
    filename = "cipherText.txt"  
    text = read_cipher_text(filename)
    freqs = get_letter_frequencies(text)
    shift = find_shift(freqs)
    print(f"[+] Detected shift: {shift}")
    decrypted_text = decrypt(text, shift)
    print("\n[+] Decrypted Text:\n")
    print(decrypted_text)

if __name__ == "__main__":
    main()
