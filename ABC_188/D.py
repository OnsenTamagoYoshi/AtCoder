import numpy as np

N, PrimeCost = map(int, input().split())
firstDates = [0] * N
lastDates = [0] * N
costs = [0] * N

for i in range(N):
    firstDates[i], lastDates[i], costs[i] = map(int, input().split())

max_lastdates = max(lastDates)
# こいつをすべてのindexから引く
min_firstdates = min(firstDates)

# 0始まりのindexにするときの最後のデータインデックスを算出
last_index = max_lastdates - min_firstdates

# indexを1から使えるように1つ余分な大きさにする(0番目は欠番)
tmp = np.zeros(last_index + 1)     
for i in range(N):
    tmp[firstDates[i] - min_firstdates: lastDates[i] + 1 - min_firstdates] = tmp[firstDates[i] - min_firstdates: lastDates[i] + 1 - min_firstdates] + costs[i]

# この時点でtmpには全期間の日ごとのサービス単価の合計が入っている。
# あとはプライムコストより高いところは全部プライムコストに置き換えたうえで総和を計算すればおしまい
new_tmp = np.where(tmp > PrimeCost, PrimeCost, tmp)

print(int(new_tmp.sum()))
