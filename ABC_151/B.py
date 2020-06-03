num_of_subjects, perfect_score, average = map(int, input().split())
scores = list(map(int, input().split()))

necessary_score = average * num_of_subjects - sum(scores)

if necessary_score < 0:
    print('0')
elif necessary_score <= perfect_score:
    print(necessary_score)
else:
    print('-1')
