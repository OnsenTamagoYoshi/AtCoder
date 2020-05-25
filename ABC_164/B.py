t_life, t_attack, a_life, a_attack = map(int, input().split())

while t_life >= 0 and a_life >= 0:
    a_life = a_life - t_attack
    if a_life <= 0:
        print('Yes')
        exit()

    t_life = t_life - a_attack
    if t_life <= 0:
        print('No')
        exit()
