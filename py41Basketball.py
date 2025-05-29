def parse_line(line):
    return line.strip().split('|')

def to_int(value):
    try:
        return int(value)
    except:
        return 0

def calculate_efficiency(stats):
    try:
        gp = to_int(stats['GP'])
        if gp == 0:
            return 0.0
        total = (to_int(stats['PTS']) + to_int(stats['REB']) + to_int(stats['AST']) +
                 to_int(stats['STL']) + to_int(stats['BLK']) -
                 ((to_int(stats['FGA']) - to_int(stats['FGM'])) +
                  (to_int(stats['FTA']) - to_int(stats['FTM'])) +
                  to_int(stats['TO'])))
        return total / gp
    except:
        return 0.0

def main():
    filename = 'player_regular_season_career.txt'
    top50_output = 'top50.txt'

    with open(filename, 'r') as f:
        lines = f.readlines()

    header = parse_line(lines[0])
    data_lines = lines[1:]

    max_stats = {
        'MIN': [0, ""],
        'GP': [0, ""],
        'PTS': [0, ""],
        'REB': [0, ""],
        'PF': [0, ""],
        'FTM': [0, ""],
    }

    efficiencies = []

    for line in data_lines:
        fields = parse_line(line)
        if len(fields) < len(header):
            continue

        stats = dict(zip(header, fields))
        name = f"{stats['firstname']} {stats['lastname']}"

        eff = calculate_efficiency(stats)
        efficiencies.append((eff, name))

        for stat in max_stats:
            value = to_int(stats[stat])
            if value > max_stats[stat][0]:
                max_stats[stat] = [value, name]

    print("🏀 Player Stat Leaders:")
    print(f"Most Minutes Played: {max_stats['MIN'][1]}, {max_stats['MIN'][0]}")
    print(f"Most Games Played: {max_stats['GP'][1]}, {max_stats['GP'][0]}")
    print(f"Most Points Scored: {max_stats['PTS'][1]}, {max_stats['PTS'][0]}")
    print(f"Most Rebounds: {max_stats['REB'][1]}, {max_stats['REB'][0]}")
    print(f"Most Personal Fouls: {max_stats['PF'][1]}, {max_stats['PF'][0]}")
    print(f"Most Free Throws Made: {max_stats['FTM'][1]}, {max_stats['FTM'][0]}\n")

    efficiencies.sort(reverse=True)
    with open(top50_output, 'w') as f_out:
        for eff, name in efficiencies[:50]:
            f_out.write(f"{name} {eff:.2f}\n")

    print(f"✅ Top 50 players saved to '{top50_output}'")

if __name__ == "__main__":
    main()
