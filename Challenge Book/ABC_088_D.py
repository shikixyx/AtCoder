from collections import deque

def bfs(H,W,G):
    d  = [[-1] * W for i in range(H)]
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    q = deque([])
    q.append((0,0))
    d[0][0] = 0

    while(len(q) != 0):
        x,y = q.popleft()

        if(x == (H-1) & y == (W-1)):
            break

        for i in range(4):
            nx , ny = x + dx[i] , y + dy[i]

            if (0 <= nx and nx <= (H-1) and 0<= ny and ny <= (W-1) and G[nx][ny] == 0 and d[nx][ny] == -1):
                q.append((nx,ny))
                d[nx][ny] = d[x][y]+1
    return d


H , W = map(int,input().split())
G = [[0] * W for i in range(H)]

for i in range(H):
    a = input()
    for j in range(len(a)):
        if a[j] == "#":
            G[i][j] = 1

d = bfs(H,W,G)
point = -1

if d[H-1][W-1] != -1:
    point = H * W - sum(map(sum,G)) - d[H-1][W-1] -1

print(point)
