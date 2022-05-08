H, W = map(int, input().split())
R, C = map(int, input().split())

if H == 1 and W == 1:
    print(0)
else:
    if H == 1:
        if C == 1 or C == W:
            print(1)
        else:
            print(2)
    elif W == 1:
        if R == 1 or R == H:
            print(1)
        else:
            print(2)
    else:
        if R == 1 or R == H:
            if C == 1 or C == W:
                print(2)
            else:
                print(3)
        else :
            if C == 1 or C == W:
                print(3)
            else:
                print(4)
