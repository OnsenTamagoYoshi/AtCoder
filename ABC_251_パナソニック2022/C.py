import numpy as np

N = int(input())
poems = []
original_poems = {}

top_poem = ""
top_point = 0
top_index = 0

for i in range(N):
    poem, point = input().split()
    point = int(point)

    if i == 0:
        top_poem = poem
        top_point = point
        top_index = i
    else:
        # 暫定トップよりも得点が高く、オリジナルなら
        if top_point < point and (poem not in original_poems):
            top_poem = poem
            top_point = point
            top_index = i

    original_poems[poem] = 1

print(top_index+1)
