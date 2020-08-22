N = int(input())
S = input()

ans = 0
while True:
    left_white_idx = S.find('W')
    right_red_idx  = S.rfind('R')

    if left_white_idx == -1 or right_red_idx == -1 or left_white_idx > right_red_idx:
        break

    # 左のRの連続とW　Rと右のWの連続を切り取った文字列に更新
    S = S[left_white_idx+1:right_red_idx]

    ans = ans + 1

print(ans)


