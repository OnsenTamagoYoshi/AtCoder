import numpy as np

num_of_problems, num_of_submittions = map(int, input().split())
submittions = []
for _ in range(num_of_submittions):
    submittions.append(list(input().split()))

WAs = [0] * num_of_problems
ACs = [0] * num_of_problems

for submittion in submittions:
    problem_index = int(submittion[0]) - 1
    result = submittion[1]

    if result == 'WA' and ACs[problem_index] == 0:
        WAs[problem_index] = WAs[problem_index] + 1

    if result == 'AC' and ACs[problem_index] == 0:
        ACs[problem_index] = 1

# WAありでACなしの問題のペナルティ数を0にする
WAs = np.array(WAs) * np.array(ACs)

print(str(ACs.count(1)) + ' ' + str(sum(WAs)))