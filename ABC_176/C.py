N = int(input())
heights = list(map(int, input().split()))

max_height = heights[0]
total_step = 0

for h in range(1, len(heights)):
    if max_height >= heights[h]:
        total_step = total_step + max_height - heights[h]
    else:
        max_height = heights[h]

print(total_step)