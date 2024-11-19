import pickle

players = {
    "Player1": {"2018/2019": 12, "2019/2020": 15, "2020/2021": 8, "2021/2022": 20, "2022/2023": 25},
    "Player2": {"2018/2019": 25, "2019/2020": 30, "2020/2021": 10, "2021/2022": 22, "2022/2023": 28},
    "Player3": {"2018/2019": 5, "2019/2020": 8, "2020/2021": 3, "2021/2022": 12, "2022/2023": 9},
    "Player4": {"2018/2019": 14, "2019/2020": 16, "2020/2021": 18, "2021/2022": 20, "2022/2023": 10},
    "Player5": {"2018/2019": 20, "2019/2020": 25, "2020/2021": 22, "2021/2022": 18, "2022/2023": 30},
    "Player6": {"2018/2019": 2, "2019/2020": 4, "2020/2021": 5, "2021/2022": 6, "2022/2023": 1},
    "Player7": {"2018/2019": 31, "2019/2020": 20, "2020/2021": 15, "2021/2022": 30, "2022/2023": 12},
}

print("List of players and their total goals for 5 seasons:")
for player, seasons in players.items():
    total_goals = sum(seasons.values())
    print(f"{player}: {total_goals} goals")

print("\nSeasons with maximum and minimum goals for each player:")
for player, seasons in players.items():
    max_season = max(seasons, key=seasons.get)
    min_season = min(seasons, key=seasons.get)
    print(f"{player} - Max goals: {max_season} ({seasons[max_season]} goals), Min goals: {min_season} ({seasons[min_season]} goals)")

print("\nPlayers who scored more than 30 goals in any season:")
for player, seasons in players.items():
    if any(goals > 30 for goals in seasons.values()):
        print(player)

print("\nPlayers who scored at least 5 goals more in the 2018/2019 season than in the 2020/2021 season:")
for player, seasons in players.items():
    if seasons["2018/2019"] >= seasons["2020/2021"] + 5:
        print(player)

with open('data.pickle', 'wb') as file:
    pickle.dump(players, file)

with open('data.pickle', 'rb') as file:
    loaded_players = pickle.load(file)
print("\nLoaded dictionary from file:")
print(loaded_players)

with open('input.txt', 'r', encoding='utf-8') as input_file:
    lines = input_file.readlines()
sorted_lines = sorted(lines, key=len, reverse=True)

with open('output.txt', 'w', encoding='utf-8') as output_file:
    output_file.writelines(sorted_lines)


