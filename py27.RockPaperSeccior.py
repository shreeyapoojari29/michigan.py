import random

def get_computer_choice(user_counts):
    max_choice = max(user_counts, key=user_counts.get)
    max_count = user_counts[max_choice]
    
    if list(user_counts.values()).count(max_count) > 1:
        return random.choice(['r', 'p', 's'])  
    if max_choice == 'r':
        return 'p' 
    elif max_choice == 'p':
        return 's'  
    else:
        return 'r' 

def determine_winner(user, computer):
    if user == computer:
        return 'tie'
    elif (user == 'r' and computer == 's') or \
         (user == 'p' and computer == 'r') or \
         (user == 's' and computer == 'p'):
        return 'user'
    else:
        return 'computer'

def main():
    print("Welcome to Rock, Paper, Scissors! (Enter Q to quit)")
    
    user_counts = {'r': 0, 'p': 0, 's': 0}
    scores = {'user': 0, 'computer': 0, 'tie': 0}
    
    while True:
        user_input = input("Choose [R]ock, [P]aper, [S]cissors or [Q]uit: ").lower()
        
        if user_input == 'q':
            break
        elif user_input not in ['r', 'p', 's']:
            print("Invalid input. Please choose R, P, S, or Q.")
            continue

        user_counts[user_input] += 1
        computer_choice = get_computer_choice(user_counts)
        
        print(f"You chose: {user_input.upper()}, Computer chose: {computer_choice.upper()}")
        
        result = determine_winner(user_input, computer_choice)
        scores[result] += 1
        
        if result == 'tie':
            print("It's a tie!\n")
        elif result == 'user':
            print("You win this round!\n")
        else:
            print("Computer wins this round!\n")

    print("\nGame Over! Here are the results:")
    print(f"User Wins: {scores['user']}")
    print(f"Computer Wins: {scores['computer']}")
    print(f"Ties: {scores['tie']}")
    print(f"User chose Rock {user_counts['r']} times.")
    print(f"User chose Paper {user_counts['p']} times.")
    print(f"User chose Scissors {user_counts['s']} times.")

if __name__ == "__main__":
    main()
