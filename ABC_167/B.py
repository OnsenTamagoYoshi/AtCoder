one, zero, minus_one, choice = map(int, input().split())
tmpsum = 0

if one >= choice:
    print(choice)
else:
    tmpsum = one
    choice = choice - one

    if zero >= choice:
        print(tmpsum)
    else:
        choice = choice - zero
        print(tmpsum - choice)
