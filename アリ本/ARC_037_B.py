def dfs(n, path, v):
    is_tree = 1
    has_cycle = 0
    v[n] = 1

    next_v = path[n]

    if next_v == 0:
        return is_tree, path, v

    for nv in next_v:
        if v[nv] == 1:
            is_tree = 0
        else:
            path[nv].remove(n)
            part_is_tree, path, v = dfs(nv, path, v)
            is_tree = is_tree * part_is_tree

    return is_tree, path, v


N, M = map(int, input().split())

path = [0] * N
visited = [0] * N
trees = 0

for i in range(M):
    u, v = map(int, input().split())

    if path[u-1] == 0:
        path[u-1] = [v-1]
    else:
        path[u-1].append(v-1)

    if path[v-1] == 0:
        path[v-1] = [u-1]
    else:
        path[v-1].append(u-1)

for n in range(N):
    if visited[n] == 0:
        tree, path, visited = dfs(n, path, visited)
        trees += tree

print(trees)
