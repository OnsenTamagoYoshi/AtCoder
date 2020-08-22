import math

num_of_points, distance = map(int, input().split())

ans = 0
for i in range(num_of_points):
    X, Y = map(int, input().split())
    d = math.sqrt(X ** 2 + Y ** 2)
    if d <= distance:
        ans = ans + 1

print(ans)

