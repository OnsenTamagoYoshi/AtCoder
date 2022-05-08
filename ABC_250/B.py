N, A, B = map(int, input().split())

tmp = ""
oneline_string = ""
reverse_oneline_string = ""
result_line_string = ""

for k in range(N):
    # 処理中タイルが奇数番目
    if k % 2 == 0:
        if k == 0:
            for j in range(A):
                if j == 0 and k == 0:
                    for i in range(N):
                        if i % 2 == 0:
                            tmp = tmp + ("." * B)
                        else:
                            tmp = tmp + ("#" * B)

                    # 1行あたりの文字列
                    oneline_string = tmp + '\n'

                    tmp = tmp.replace(".", "tmp")
                    tmp = tmp.replace("#", ".")
                    reverse_oneline_string = tmp.replace("tmp", "#") + '\n'

                    result_line_string = oneline_string
                else:
                    result_line_string = result_line_string + oneline_string
        else:
            for j in range(A):
                result_line_string = result_line_string + oneline_string
    # 処理中タイルが偶数番目
    else:
        for j in range(A):
            result_line_string = result_line_string + reverse_oneline_string

print(result_line_string)
