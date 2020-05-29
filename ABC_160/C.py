lake_length, num_of_house = map(int, input().split())
positions = list(map(int, input().split()))

max_interval = lake_length - positions[num_of_house - 1] + positions[0]

for i in range(1, num_of_house):
    max_interval = max(max_interval, positions[i] - positions[i - 1])

print(str(lake_length - max_interval))
