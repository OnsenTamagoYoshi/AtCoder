from decimal import Decimal, ROUND_HALF_UP

num_of_person = int(input())
coordinates = list(map(int, input().split()))

avg = sum(coordinates) / len(coordinates)
avg = Decimal(str(avg)).quantize(Decimal('0'), rounding=ROUND_HALF_UP)

power = 0
for coordinate in coordinates:
    power = power + (coordinate - avg) ** 2

print(power)