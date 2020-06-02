import collections

num_of_papers = int(input())
names = []

for _ in range(num_of_papers):
    names.append(input())

cnt = collections.defaultdict(int)
max_appearance = 0
for _ in names:
    cnt[_] = cnt[_] + 1

    if max_appearance < cnt[_]:
        max_appearance = cnt[_]

max_names = [key for key, value in cnt.items() if value == max_appearance]

max_names.sort()

for _ in max_names:
    print(_)
    