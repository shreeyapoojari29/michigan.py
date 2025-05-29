# Facebook Friend Recommendation System

def open_file():
    while True:
        try:
            filename = input("Enter a filename: ")
            fp = open(filename, "r")
            return fp
        except FileNotFoundError:
            print("Error in filename.")

def read_file(fp):
    n = int(fp.readline().strip())
    network = [[] for _ in range(n)]
    for line in fp:
        u, v = map(int, line.strip().split())
        if v not in network[u]:
            network[u].append(v)
        if u not in network[v]:
            network[v].append(u)
    return network

def num_in_common_between_lists(list1, list2):
    return sum(1 for item in list1 if item in list2)

def init_matrix(n):
    return [[0] * n for _ in range(n)]

def calc_similarity_scores(network):
    n = len(network)
    similarity_matrix = init_matrix(n)
    for i in range(n):
        for j in range(n):
            if i != j:
                similarity_matrix[i][j] = num_in_common_between_lists(network[i], network[j])
    return similarity_matrix

def recommend(user_id, network, similarity_matrix):
    max_common = -1
    suggested_friend = None
    for i in range(len(network)):
        if i != user_id and i not in network[user_id]:
            if similarity_matrix[user_id][i] > max_common:
                max_common = similarity_matrix[user_id][i]
                suggested_friend = i
    return suggested_friend

def main():
    print("Facebook friend recommendation.\n")
    fp = open_file()
    network = read_file(fp)
    fp.close()
    similarity_matrix = calc_similarity_scores(network)
    n = len(network)

    while True:
        try:
            user_input = input(f"Enter an integer in the range 0 to {n-1} : ")
            user_id = int(user_input)
            if 0 <= user_id < n:
                suggestion = recommend(user_id, network, similarity_matrix)
                print(f"The suggested friend for {user_id} is {suggestion}")
            else:
                print(f"Error: input must be an int between 0 and {n-1}")
        except ValueError:
            print(f"Error: input must be an int between 0 and {n-1}")
        
        again = input("Do you want to continue (yes/no)? ").strip().lower()
        if again == "no":
            break


if __name__ == "__main__":
    main()
