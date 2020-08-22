N = int(input())
Ls = list(map(int, input().split()))

ans = 0
# リストの頭からループし、1つ目の値を保持する
for i in range(len(Ls)- 2):
    first_side = Ls[i]

    for j in range(i + 1, len(Ls)):
        second_side = Ls[j]
        # 2つ目の値が1つ目と異なる値なら
        if first_side != second_side:
            #2つ目の値以降のリストの中に含まれる、条件を満たす数を数える
            ans = ans + len([i for i in Ls[j+1:] if i != first_side and i != second_side and first_side + second_side > i and first_side + i > second_side and second_side + i > first_side])

print(ans)
