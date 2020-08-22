S = input()

cnt = S.count('R')
if cnt == 0:
    print(cnt)
else:
    if cnt == 2:
        if S.count('RR') == 1:
            print(cnt)
        else:
            print(1)
    else:
        print(cnt)
