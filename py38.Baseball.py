# Baseball Stats Manager

def load_data(filename):
    data = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                parts = line.strip().split(';')
                if len(parts) != 9:
                    continue
                name = parts[0].strip()
                team = parts[1].strip()
                try:
                    games = int(parts[2])
                    at_bats = int(parts[3])
                    runs = int(parts[4])
                    hits = int(parts[5])
                    doubles = int(parts[6])
                    triples = int(parts[7])
                    home_runs = int(parts[8])
                except ValueError:
                    continue
                singles = hits - (doubles + triples + home_runs)
                total_bases = singles + 2*doubles + 3*triples + 4*home_runs
                batting_avg = hits / at_bats if at_bats > 0 else 0.0
                slugging_pct = total_bases / at_bats if at_bats > 0 else 0.0
                player = (name, team, games, at_bats, runs, hits, doubles, triples, home_runs, batting_avg, slugging_pct)
                data.append(player)
        return data
    except FileNotFoundError:
        print("File not found.")
        return None

def print_help():
    print("""
Available commands:
  HELP                 Show this help message
  INPUT filename       Load player data from file
  TEAM team_id         Show all players on a team
  REPORT n FIELD       Show top n players by HITS, BATTING, or SLUGGING
  QUIT                 Exit the program
""")

def print_team(data, team_id):
    team_players = [p for p in data if p[1].upper() == team_id.upper()]
    if not team_players:
        print("Team not found.")
        return
    team_players.sort()
    print(f"{'Name':<20} {'AB':>4} {'R':>3} {'H':>4} {'2B':>4} {'3B':>4} {'HR':>4} {'AVG':>8} {'SLG':>8}")
    for p in team_players:
        print(f"{p[0]:<20} {p[3]:>4} {p[4]:>3} {p[5]:>4} {p[6]:>4} {p[7]:>4} {p[8]:>4} {p[9]:>8.3f} {p[10]:>8.3f}")

def report(data, n, field):
    if field not in ['HITS', 'BATTING', 'SLUGGING']:
        print("Invalid field. Use HITS, BATTING, or SLUGGING.")
        return
    if field == 'HITS':
        key = lambda p: (p[5], p[0])
    elif field == 'BATTING':
        key = lambda p: (p[9], p[0])
    else:
        key = lambda p: (p[10], p[0])
    sorted_players = sorted(data, key=key, reverse=True)
    print(f"{'Name':<20} {'Team':<4} {field:<8}")
    for p in sorted_players[:n]:
        val = p[5] if field == 'HITS' else (p[9] if field == 'BATTING' else p[10])
        print(f"{p[0]:<20} {p[1]:<4} {val:>8.3f}" if field != 'HITS' else f"{p[0]:<20} {p[1]:<4} {int(val):>8}")

def main():
    print("Welcome to the Baseball Stats Manager!")
    data = []
    while True:
        cmd = input("Enter command: ").strip()
        if not cmd:
            continue
        parts = cmd.split()
        if parts[0].upper() == 'QUIT':
            print("Exiting program.")
            break
        elif parts[0].upper() == 'HELP':
            print_help()
        elif parts[0].upper() == 'INPUT':
            if len(parts) != 2:
                print("Usage: INPUT filename")
                continue
            loaded = load_data(parts[1])
            if loaded is not None:
                data = loaded
                print(f"Loaded {len(data)} records.")
        elif parts[0].upper() == 'TEAM':
            if len(parts) != 2:
                print("Usage: TEAM team_id")
                continue
            print_team(data, parts[1])
        elif parts[0].upper() == 'REPORT':
            if len(parts) != 3:
                print("Usage: REPORT n FIELD")
                continue
            try:
                n = int(parts[1])
                report(data, n, parts[2].upper())
            except ValueError:
                print("Invalid number for REPORT.")
        else:
            print("Unknown command. Type HELP for help.")

if __name__ == "__main__":
    main()