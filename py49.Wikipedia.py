def process_input(filename):
    editor_dict = {}
    article_dict = {}

    try:
        with open(filename, 'r') as file:
            lines = file.readlines()

        for i in range(len(lines)):
            if lines[i].startswith("REVISION"):
                parts = lines[i].strip().split()
                if len(parts) >= 6:
                    article = parts[3]
                    editor = parts[5]

                    # update editor_dict
                    if editor not in editor_dict:
                        editor_dict[editor] = set()
                    editor_dict[editor].add(article)

                    # update article_dict
                    if article not in article_dict:
                        article_dict[article] = [0, set()]
                    article_dict[article][0] += 1
                    article_dict[article][1].add(editor)

        print(f"Loaded {len(article_dict)} articles and {len(editor_dict)} editors.")
        return editor_dict, article_dict

    except FileNotFoundError:
        print("Error: File not found.")
        return None, None

def top_n_editors(editor_dict, n):
    ranked = sorted(editor_dict.items(), key=lambda x: (-len(x[1]), x[0]))
    print(f"\nTop {n} Editors (by number of articles edited):")
    print(f"{'Editor':20} {'Articles Revised'}")
    for editor, articles in ranked[:n]:
        print(f"{editor:20} {len(articles)}")

def top_n_edits(article_dict, n):
    ranked = sorted(article_dict.items(), key=lambda x: (-x[1][0], x[0]))
    print(f"\nTop {n} Articles (by number of edits):")
    print(f"{'Article':30} {'Edit Count'}")
    for article, (count, _) in ranked[:n]:
        print(f"{article:30} {count}")

def top_n_articles_by_editors(article_dict, n):
    ranked = sorted(article_dict.items(), key=lambda x: (-len(x[1][1]), x[0]))
    print(f"\nTop {n} Articles (by number of unique editors):")
    print(f"{'Article':30} {'Unique Editors'}")
    for article, (_, editors) in ranked[:n]:
        print(f"{article:30} {len(editors)}")

def help_menu():
    print("\nAvailable commands:")
    print("  INPUT filename       - Load new dataset")
    print("  TOP n EDITORS        - Show top n editors")
    print("  TOP n EDITS          - Show top n edited articles")
    print("  TOP n ARTICLES       - Show articles revised by most editors")
    print("  HELP                 - Show this help menu")
    print("  QUIT                 - Exit program")

def main():
    editor_dict = {}
    article_dict = {}

    while True:
        command = input("\nEnter command: ").strip().upper()

        if command.startswith("INPUT"):
            parts = command.split()
            if len(parts) == 2:
                editor_dict, article_dict = process_input(parts[1])
            else:
                print("Usage: INPUT filename")

        elif command.startswith("TOP"):
            parts = command.split()
            if len(parts) == 3 and parts[1].isdigit():
                n = int(parts[1])
                if parts[2] == "EDITORS" and editor_dict:
                    top_n_editors(editor_dict, n)
                elif parts[2] == "EDITS" and article_dict:
                    top_n_edits(article_dict, n)
                elif parts[2] == "ARTICLES" and article_dict:
                    top_n_articles_by_editors(article_dict, n)
                else:
                    print("Invalid category or data not loaded.")
            else:
                print("Usage: TOP n CATEGORY")

        elif command == "HELP":
            help_menu()

        elif command == "QUIT":
            print("Exiting...")
            break

        else:
            print("Unknown command. Type HELP for a list of commands.")

if __name__ == "__main__":
    main()
