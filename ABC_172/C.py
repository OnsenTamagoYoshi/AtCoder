N, M, K = map(int, input().split())
A_minutes = list(map(int, input().split()))
B_minutes = list(map(int, input().split()))

total_A_minutes = sum(A_minutes)
total_B_minutes = sum(B_minutes)

# すべて読める場合
if total_A_minutes + total_B_minutes <= K:
    print(N + M)
    exit()

# 冊数
ans = 0
# Kを超える最小のi
limitover_A_index = 0
# Aの合計が超えた場合
if total_A_minutes > K:
    tmp_total_A_minutes = 0
    for i in range(N):
        tmp_total_A_minutes = tmp_total_A_minutes + A_minutes[i]
        if tmp_total_A_minutes > K:
            limitover_A_index = i
            # Kを超過したindex が Kを超過しない冊数となる
            ans = i
            break
# Aの合計が超えない場合
else:
    limitover_A_index = N
    ans = N

while limitover_A_index >= 0:
    tmp_total_minute = sum(A_minutes[:limitover_A_index])
    tmp_ans = limitover_A_index

    # Bを1冊ずつ確認
    for B_minute in B_minutes:
        # Bの冊数を足したことでK分を超えるなら
        if tmp_total_minute + B_minute > K:
            break

        tmp_total_minute = tmp_total_minute + B_minute
        tmp_ans = tmp_ans + 1

    # 最大冊数の記録を超えたら更新する
    if ans < tmp_ans:
        ans = tmp_ans

    limitover_A_index = limitover_A_index - 1

print(ans)
