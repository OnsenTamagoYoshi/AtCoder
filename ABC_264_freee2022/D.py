input_s = input()
s = 'atcoder'

cnt = 0
while input_s != 'atcoder':
    cnt = cnt + 1
    
    if input_s.find('a') != 0:
        l_input_s = list(input_s)
        target_char = 'a'
        target_idx = input_s.find(target_char)
        replace_idx = target_idx - 1
        replace_char = input_s[target_idx - 1]
        l_input_s[replace_idx] = target_char
        l_input_s[target_idx] = replace_char
        input_s = "".join(l_input_s)
    elif input_s.find('t') != 1:
        l_input_s = list(input_s)
        target_char = 't'
        target_idx = input_s.find(target_char)
        replace_idx = target_idx - 1
        replace_char = input_s[target_idx - 1]
        l_input_s[replace_idx] = target_char
        l_input_s[target_idx] = replace_char
        input_s = "".join(l_input_s)
    elif input_s.find('c') != 2:
        l_input_s = list(input_s)
        target_char = 'c'
        target_idx = input_s.find(target_char)
        replace_idx = target_idx - 1
        replace_char = input_s[target_idx - 1]
        l_input_s[replace_idx] = target_char
        l_input_s[target_idx] = replace_char
        input_s = "".join(l_input_s)
    elif input_s.find('o') != 3:
        l_input_s = list(input_s)
        target_char = 'o'
        target_idx = input_s.find(target_char)
        replace_idx = target_idx - 1
        replace_char = input_s[target_idx - 1]
        l_input_s[replace_idx] = target_char
        l_input_s[target_idx] = replace_char
        input_s = "".join(l_input_s)
    elif input_s.find('d') != 4:
        l_input_s = list(input_s)
        target_char = 'd'
        target_idx = input_s.find(target_char)
        replace_idx = target_idx - 1
        replace_char = input_s[target_idx - 1]
        l_input_s[replace_idx] = target_char
        l_input_s[target_idx] = replace_char
        input_s = "".join(l_input_s)
    elif input_s.find('e') != 5:
        l_input_s = list(input_s)
        target_char = 'e'
        target_idx = input_s.find(target_char)
        replace_idx = target_idx - 1
        replace_char = input_s[target_idx - 1]
        l_input_s[replace_idx] = target_char
        l_input_s[target_idx] = replace_char
        input_s = "".join(l_input_s)
    elif input_s.find('r') != 6:
        l_input_s = list(input_s)
        target_char = 'r'
        target_idx = input_s.find(target_char)
        replace_idx = target_idx - 1
        replace_char = input_s[target_idx - 1]
        l_input_s[replace_idx] = target_char
        l_input_s[target_idx] = replace_char
        input_s = "".join(l_input_s)
    else:
        pass
    
print(cnt)