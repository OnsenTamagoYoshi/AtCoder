import numpy as np

num_of_user, num_of_log = map(int, input().split())

logs = [input() for _ in range(num_of_log)]

follow = np.full(num_of_user * num_of_user, 'N', dtype=str).reshape(num_of_user, num_of_user)

for log in logs:
    loglist = list(log.split())
    a = int(loglist[1]) - 1

    # aがbをフォロー
    if loglist[0] == '1':
        b = int(loglist[2]) - 1
        follow[a][b] = 'Y'
    # aをフォローしている全員をaがフォロー
    elif loglist[0] == '2':
        for i in range(num_of_user):
            if follow[i][a] == 'Y':
                follow[a][i] = 'Y'
    # aがフォローしているユーザーがフォローしているユーザーをaがフォロー
    # ただし自分自身へのフォローはしない
    else:
        # フォローフォローにより値が書き換わる場合があるので、書き換え前の状態を保存
        follow_before = follow.copy()
        for i in range(num_of_user):
            if follow_before[a][i] == 'Y':
                for j in range(num_of_user):
                    if follow_before[i][j] == 'Y' and j != a:
                        follow[a][j] = 'Y'

for i in range(num_of_user):
    follow_i = ''
    for j in range(num_of_user):
        follow_i = follow_i + follow[i][j]
    print(follow_i)
    # ''.join(list(follow[i].tostring().decode('UTF-8').replace(' ', '')))
    # のようにしても要素間に空白が3つ出力されてしまう
    
