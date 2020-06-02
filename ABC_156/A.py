num_of_participation, rating = map(int, input().split())

if num_of_participation >= 10:
    print(rating)
else:
    print(rating + 100 * (10 - num_of_participation))