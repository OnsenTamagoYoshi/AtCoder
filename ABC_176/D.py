H, W = map(int, input().split())
start_i, start_j = map(int, input().split())
goal_i, goal_j = map(int, input().split())

maze = []
for i in range(H):
    maze.append(list(input().split()))

# ゴールにたどり着けない場合はこの値が返る
INF = 999999999

def clear_maze(start_i, start_j, goal_i, goal_j, maze):
    # 迷路の縦幅
    field_x_length = H
    # 迷路の横幅
    field_y_length = W

    distance = [[INF for i in range(field_x_length)] for j in range(field_y_length)]

    # 幅優先探索
    def bfs():
        queue = []
        queue.insert(0, (start_i, start_j))

        distance[start_i][start_j] = 0

        while len(queue):
            x, y = queue.pop()

            # ゴールに到達したらループ終了
            if x == goal_i and y == goal_j:
                break


            for i in range(0, 4):
                nx = x + [1, 0, -1,  0][i]
                ny = y + [0, 1,  0, -1][i]

                if(0 <= nx and nx < field_x_length and 0 <= ny and ny < field_y_length):
                    if(maze[nx][ny] != '#' and distance[nx][ny] == INF):
                        queue.insert(0, (nx, ny))
                        distance[nx][ny] = distance[x][y] + 1

        return distance[goal_j][goal_j]

    return bfs()

# ワープなしでゴール
if clear_maze(start_i, start_j, goal_i, goal_j, maze) != INF:
    print(0)
else:
    pass