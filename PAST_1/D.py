import numpy as np

N = int(input())
A = [int(input()) for _ in range(N)]

A_cor = list(range(1, N + 1))
set_A = set(A)
set_A_cor = set(A_cor)

if len(set_A_cor - set_A) == 0:
    print('Correct')
else:
    x = list(set_A_cor - set_A)[0]
    A = np.array(A)
    # 0����n�܂鐮����̂��ꂼ��̏o���񐔔z��
    count = np.bincount(A)
    # �o���񐔔z��̍ő�v�f�̃C���f�b�N�X���o(����͂��ꂪ�d���l�ƈ�v)
    y = np.argmax(count)
    print(str(y) + ' ' + str(x))
