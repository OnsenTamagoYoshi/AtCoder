S = input()

start_upper_flg = False
start_word_index = 0
wordlist = []
for i, _ in enumerate(S):
    if _.isupper():
        # �P��̍Ō�̑啶���̏ꍇ
        if start_upper_flg:
            start_upper_flg = False
            wordlist.append(S[start_word_index:i+1])
        else:
            start_upper_flg = True
            start_word_index = i

# upper�w���sort
wordlist.sort(key=str.upper)
print(''.join(wordlist))
