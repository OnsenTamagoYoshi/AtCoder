row, col, K = map(int, input().split())

cells = []
for i in range(row):
    # 1行分の文字列を追加
    cells.append(input())

# 初期状態の黒マスの数
num_of_blackcell = ''.join(cells).count('#')

# 初期状態の黒マスがKより小さい場合
if num_of_blackcell < K:
    print(0)
    exit()

# 初期状態の黒マスとKが同値の場合
if num_of_blackcell == K:
    # 何も選ばない1通り
    print(1)
    exit()


from itertools import combinations

def SumTheList(thelist, target):
    arr = []
    num_of_combinations = 0

    # リストからr個を抽出する組み合わせのリストを生成し、保存する
    # rは1からリストの長さまで順次確認する
    for r in range(1, len(thelist) + 1):
        arr += list(combinations(thelist, r))

    for item in arr:
        if sum(item) == target:
            # 合計がtargetと合致する組み合わせがあれば組み合わせ数に加算する
            num_of_combinations += 1

    return num_of_combinations

ans = 0

#########################
# 行だけのパターンを確認
#########################
# 消したい黒マスの数
num_of_delete_blackcell = num_of_blackcell - K

# 行ごとに存在する黒マスの数のリスト
num_of_row_blackcells = []
for i in range(row):
    num_of_row_blackcells.append(cells[i].count('#'))

# 消したい黒マスの数を満たす組み合わせ数を算出
ans += SumTheList(num_of_row_blackcells, num_of_delete_blackcell)

#########################
# 列だけのパターンを確認
#########################
# 列ごとに存在する黒マスの数のリスト
num_of_col_blackcells = [0] * col
for i in range(row):
    for j in range(col):
        if cells[i][j] == '#':
            num_of_col_blackcells[j] += 1

# 消したい黒マスの数を満たす組み合わせ数を算出
ans += SumTheList(num_of_col_blackcells, num_of_delete_blackcell)

# 全行・全列埋めが発生していたら1を引く(=Kが0)
if K == 0:
    ans -= 1

# 行・列混在のパターンを確認
from itertools import product

for p in product((0, 1), repeat=row):
    # 行数の中から任意の行に1を立てた組み合わせを全探索

    # 使用する行のインデックスリスト
    tmp_rows = [i for i, x in enumerate(p) if x == 1]

    # 全行抽出しない　または　全行抽出　は除外する
    if len(tmp_rows) != 0 and len(tmp_rows) != row:
        tmp_cells = cells.copy()
        # インデックスがずれないように逆順で削除
        for i in sorted(tmp_rows, reverse=True):
            tmp_cells.pop(i)

        # 列ごとに存在する黒マスの数のリスト
        num_of_col_blackcells = [0] * col
        for i in range(len(tmp_cells)):
            for j in range(col):
                if cells[i][j] == '#':
                    num_of_col_blackcells[j] += 1
        
        # 消したい黒マスから行選択で消された黒マスは除外する
        num_of_deletedblackcells = 0
        for tmp_cell in tmp_cells:
            num_of_deletedblackcells += ''.join(tmp_cell).count('#')

        # 消したい黒マスの数を満たす組み合わせ数を算出
        ans += SumTheList(num_of_col_blackcells, num_of_delete_blackcell - num_of_deletedblackcells)

print(ans)