from queue import Queue

def bfs(G, s):
    # todoリストを表すキュー
    que = Queue()
    
    # dist[v]は始点sから頂点vへの最短経路長
    dist = [-1] * len(G)

    # 始点sをtodoリストに背とする
    que.put(s)
    dist[s] = 0

    # todoリストが空になるまで探索する
    while not que.empty():
        # todoリストから頂点vを取り出す
        v = que.get()

        # vに直接つながる頂点を探索
        for v2 in G[v]:
            # v2がすでに探索済みの場合はスキップする
            if dist[v2] != -1:
                continue

            # v2を新たにtodoリストに追加
            que.put(v2)

            # v2のdistの値を更新
            dist[v2] = dist[v] + 1

    # 最短経路帳を表す配列を返す
    return dist

def func1(lst, value):
    return [i for i, x in enumerate(lst) if x != value]
  
N, M = map(int, input().split())

G = [[] for i in range(N)]

for i in range(M):
    u, v = map(int, input().split())
    # 頂点番号を0はじまりにする
    u = u - 1
    v = v - 1
    G[u].append(v)
    G[v].append(u)
    #print(G)

#print('bfsスタート')

# 探索対象の頂点リスト
N_list = [1] * N

ans = 0

for i in range(N):
  	# 探索がまだならBFS実施
    if N_list[i] == 1:
        #print(bfs(G,i))
        lst = bfs(G,i)
        # ここで-1以外のindexが返ってくる（探索の結果見つかったもの）
        idx = func1(lst, -1)

        # 見つかった頂点を探索対象から除外する
        for _ in idx:
            N_list[_] = 0
        
        ans = ans + 1

print(ans)