# Musical Note to Frequency Converter (Optional: Play with Beep)

from math import pow


def main():
    print("Welcome to the Tones Program!")
    print("This program converts musical notes in octpch form to frequency (Hz).\n")

    REFERENCE_OCTAVE = 4
    REFERENCE_PITCH_CLASS = 9
    REFERENCE_FREQUENCY = 440.0

    for i in range(1, 4):
        print(f"\nNote {i}:")
        octave = int(input("  Enter the octave (e.g. 4): "))
        pitch = int(input("  Enter the pitch class (0–11): "))

        octave_diff = octave - REFERENCE_OCTAVE
        pitch_diff = pitch - REFERENCE_PITCH_CLASS
        exponent = octave_diff + pitch_diff / 12
        freq = REFERENCE_FREQUENCY * pow(2, exponent)

        print(f"  => Octave {octave}, Pitch Class {pitch} => Frequency: {freq:.2f} Hz")


if __name__ == "__main__":
    main()
