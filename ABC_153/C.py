N, K = map(int, input().split())
monsters = list(map(int, input().split()))

if len(monsters) <= K:
    print('0')
else:
    monsters.sort(reverse=True)
    print(sum(monsters[K:]))