holidays, num_of_homework = map(int, input().split())
days = list(map(int, input().split()))

playingdays = holidays - sum(days)
if playingdays < 0:
    print('-1')
else:
    print(playingdays)
