num_of_observatory, num_of_road = map(int, input().split())
elevations = list(map(int, input().split()))
road_unions = []
for _ in range(num_of_road):
    road_unions.append(list(map(int, input().split())))

# つながっている展望台のリスト
to_observatorys = [[] for i in range(num_of_observatory)]

for road_union in road_unions:
    to_observatorys[road_union[0] - 1].append(elevations[road_union[1] - 1])
    to_observatorys[road_union[1] - 1].append(elevations[road_union[0] - 1])

num_of_good = 0
for i in range(num_of_observatory):
    # つながっている展望台がない または つながっている展望台よりも高い場合
    if len(to_observatorys[i]) == 0 or elevations[i] > max(to_observatorys[i]):
        num_of_good = num_of_good + 1

print(num_of_good)
