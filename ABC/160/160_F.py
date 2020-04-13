import sys
sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

# 全方位木DP
# ReRooting


def ReRooting(self, N, Edges, identity, merge, addNode):
    '''
    ※ 頂点は0-indexで実装
    引数：
        N: ノードの数
        Edges: [[a,b],[a,d],,,] 辺の集合
        identity: 単位元
        merge(Left Tree , Right Tree): 部分木のマージ関数(モノイド演算)
        addNode(value , nodeID): 頂点の追加関数(モノイド演算)
    '''

    # STEP.0 木構造の情報を記録

    # 隣接頂点
    adjacents = [[] for _ in range(N)]

    # 隣接頂点から見た自分のindex
    # indexForAdjacents[i][j] := 頂点:Edges[i][j] から見て i は何番目の隣接頂点か
    # 例)
    # Edges[Edges[i][j]][indexForAdjacents[i][j]] = i
    # i から出ている辺のj番目の頂点k
    # k から出ている辺のindexForAdjacents[i][j]番目の頂点k
    indexForAdjacents = [[] for _ in range(N)]

    for u, v in Edges:
        indexForAdjacents[u].append(len(adjacents[v]))
        indexForAdjacents[v].append(len(adjacents[u]))
        adjacents[u].append(v)
        adjacents[v].append(u)

    # childSubtreeRes[i] := iの子部分木の値
    # childSubtreeRes[i][j] := iを親とし、adjacents[i][j]を根とした部分木の値
    childSubtreeRes = [[None] * len(adjacents[x]) for x in range(N)]

    # nodeRes[i] := iを根としたときの結果結果
    nodeRes = [None] * (N)

    # STEP.1 1つの頂点を根とした根付き木について値を求める
    parents = [0] * (N)

    # order := DFSでの行きがけ順
    order = [0] * (N)

    index = 0
    stack = []

    # 0を根とする
    stack.append(0)
    parents[0] = -1

    # 行きがけ順を記録
    while stack:
        u = stack.pop()
        order[index] = u
        index += 1
        for v in adjacents[u]:
            if v == parents[u]:
                continue
            stack.append(v)
            parents[v] = u

    # 帰りがけ順で部分木の値を求める
    L = len(order)
    for i in range(N - 1, -1, -1):
        # 見ている頂点と親
        u = order[i]
        parent = parents[u]

        # 値
        res = identity
        parentIndex = -1

        # 隣接する点を調べる
        for i, v in enumerate(adjacents[u]):
            # 親が何番目の隣接か記録
            if v == parent:
                parentIndex = i
            else:
                # 隣接する点方向への子部分木の値を加える
                # 端ならこの操作はないはず
                res = merge(res, childSubtreeRes[u][i])

        # 頂点を部分木のマージ追加した後、親が持っている配列に結果を格納する
        # (親にとって自分が何番目の隣接頂点なのかを調べて格納)
        childSubtreeRes[parent][indexForAdjacents[u]
                                [parentIndex]] = addNode(res, u)

    # STEP.2 全ての頂点を根とした場合の値について求める

    # 行きがけ順で値を決めていく
    for i in range(N):
        u = order[i]

        # 後ろからの累積和を格納
        L = len(adjacents[u])
        accumFromTail = [None] * L
        accumFromTail[-1] = identity

        for j in range(L - 1, 1, -1):
            accumFromTail[j -
                          1] = merge(childSubtreeRes[u][j], accumFromTail[j])

        # 前からの累積和
        accum = identity
        for j, v in enumerate(adjacents[u]):
            # adjacents[node][j]が親、nodeが子の部分木について計算する
            # 累積をマージして子部分木の値をマージし終えた後、頂点を追加する
            res = addNode(merge(accum, accumFromTail[j]), u)

            # その値を、親が持っている配列に結果を格納する(親にとって自分が何番目の隣接頂点なのかを調べて格納)
            childSubtreeRes[adjacents[u][j]][indexForAdjacents[u][j]] = res

            # 累積を更新
            accum = merge(accum, childSubtreeRes[u][j])

        nodeRes[u] = addNode(accum, u)

    return nodeRes
