N = int(input())
prices = list(map(int, input().split()))

# 所持金
money = 1000
# 保持株数
num_of_stocks = 0
for i in range(N):
    # 最終日に持っていれば売る
    if i == N - 1:
        if num_of_stocks > 0:
            money = money + num_of_stocks * prices[i]
    else:
        # i+1日目がi日より高ければ
        if prices[i] < prices[i+1]:
            if money >= prices[i]:
                # 買えるだけ買う
                num_of_stocks =  money // prices[i]
                money = money - num_of_stocks * prices[i]
        # i+1日目がi日より低ければ
        else:
            # 株を持っていたら売る
            if num_of_stocks > 0:
                money = money + num_of_stocks * prices[i]
                num_of_stocks = 0

print(money)