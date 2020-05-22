import numpy as np

num_of_user, num_of_log = map(int, input().split())

logs = [input() for _ in range(num_of_log)]

follow = np.full(num_of_user * num_of_user, 'N', dtype=str).reshape(num_of_user, num_of_user)

for log in logs:
    loglist = list(log.split())
    a = int(loglist[1]) - 1

    # a��b���t�H���[
    if loglist[0] == '1':
        b = int(loglist[2]) - 1
        follow[a][b] = 'Y'
    # a���t�H���[���Ă���S����a���t�H���[
    elif loglist[0] == '2':
        for i in range(num_of_user):
            if follow[i][a] == 'Y':
                follow[a][i] = 'Y'
    # a���t�H���[���Ă��郆�[�U�[���t�H���[���Ă��郆�[�U�[��a���t�H���[
    # �������������g�ւ̃t�H���[�͂��Ȃ�
    else:
        # �t�H���[�t�H���[�ɂ��l�����������ꍇ������̂ŁA���������O�̏�Ԃ�ۑ�
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
    # �̂悤�ɂ��Ă��v�f�Ԃɋ󔒂�3�o�͂���Ă��܂�
    
