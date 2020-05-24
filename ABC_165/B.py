import math

X = int(input())

deposits = 100
year = 0

while deposits < X:
    deposits = math.floor(deposits * 1.01)
    year = year + 1

print(year)