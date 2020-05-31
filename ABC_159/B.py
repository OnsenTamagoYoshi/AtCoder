S = input()

if S != S[::-1]:
    print('No')
else:
    first_half = S[0:(len(S)-1) // 2]
    latter_half = S[((len(S)-1) // 2) + 1:]
    if first_half == first_half[::-1] and latter_half == latter_half[::-1]:
        print('Yes')
    else:
        print('No')