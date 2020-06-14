X, N = map(int, input().split())
if N == 0:
    Ps = {}
    print(X)
    exit()
else:
    Ps = set(list(map(int, input().split())))

all_numbers = set(list(range(0, 102)))

search_numbers = list(all_numbers - Ps)

absolute_value = 1000
out = X
for i in search_numbers:
    if abs(i - X) < absolute_value:
        absolute_value = abs(i - X)
        out = i

print(out)