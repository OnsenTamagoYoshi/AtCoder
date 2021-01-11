N = int(input())
As = list(map(int, input().split()))

# 勝ち残ったもののリストを返す関数
def vs(players):
    victory_players = []
    tmp = list(range(0, len(players), 2))
    for i in tmp:
        victory_players.append(max(players[i], players[i+1]))

    return victory_players

players = As

for i in range(N-1):
    players = vs(players)

second_players_rate = min(players)

print(As.index(second_players_rate) + 1)
