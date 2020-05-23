import itertools

num_of_sunuke, num_of_sweetstypes = map(int, input().split())

num_of_havingsweetssunuke= []
havingsweetssunukes = []

for _ in range(num_of_sweetstypes):
    num_of_havingsweetssunuke.append(int(input()))
    havingsweetssunukes.append(list(map(int, input().split())))

set_all = set(range(1, num_of_sunuke + 1))
set_havingsweets = set(itertools.chain.from_iterable(havingsweetssunukes))

print(len(set_all - set_havingsweets))