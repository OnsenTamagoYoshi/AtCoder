num_of_kuji = int(input())
prizes = set()
for _ in range(num_of_kuji):
    prizes.add(input())

print(len(prizes))