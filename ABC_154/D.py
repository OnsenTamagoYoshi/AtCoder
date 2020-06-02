import numpy as np

num_of_dices, num_of_adjacents = map(int, input().split())
eyes = list(map(int, input().split()))
expected_values = []

for i, eye in enumerate(eyes):
    expected_values.append(sum(np.array(range(1, eye + 1)) / eye))

max_expected = 0

for i in range(num_of_dices - num_of_adjacents + 1):
    if max_expected < sum(expected_values[i:num_of_adjacents + i]):
        max_expected = sum(expected_values[i:num_of_adjacents + i])

print(max_expected)
