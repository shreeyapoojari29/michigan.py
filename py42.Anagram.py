# proj05.py - CSE 231, Spring 2008 - Anagram Finder

def build_anagram_dict(filename):
  
    anagram_dict = {}

    with open(filename, 'r') as file:
        for line in file:
            word = line.strip()
            key = ''.join(sorted(word.lower()))

            if key in anagram_dict:
                anagram_dict[key].append(word)
            else:
                anagram_dict[key] = [word]

    return anagram_dict

def count_anagram_groups(anagram_dict):
   
    count_dict = {}
    for group in anagram_dict.values():
        if len(group) > 1:
            size = len(group)
            count_dict[size] = count_dict.get(size, 0) + 1
    return count_dict

def find_largest_anagram_groups(anagram_dict):
   
    max_size = 0
    largest_groups = []

    for group in anagram_dict.values():
        if len(group) > max_size:
            max_size = len(group)
            largest_groups = [group]
        elif len(group) == max_size:
            largest_groups.append(group)

    return largest_groups

def main():
    filename = input("Enter the word list file name: ")
    anagram_dict = build_anagram_dict(filename)

    print("\nCounts of anagram groups:")
    group_counts = count_anagram_groups(anagram_dict)
    for size in sorted(group_counts):
        print(f"  {size}-word anagram groups: {group_counts[size]}")

    largest_groups = find_largest_anagram_groups(anagram_dict)
    print(f"\nLargest anagram group(s) of size {len(largest_groups[0])}:")
    for group in largest_groups:
        print("  " + ', '.join(sorted(group)))

if __name__ == "__main__":
    main()
