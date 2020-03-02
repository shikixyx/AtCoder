import sys
sys.setrecursionlimit(10 ** 7)

N, M = map(int, input().split())

D = [-1] * N

for _ in range(M):
    s, c = map(int, input().split())

    if D[s-1] == -1 or D[s-1] == c:
        D[s-1] = c
    else:
        print('-1')
        exit()

if D[0] == -1 and N > 1:
    D[0] = 1
elif D[0] == -1 and N == 1:
    D[0] = 0
elif D[0] == 0 and N != 1:
    print('-1')
    exit()

ans = []

for d in D:
    if d == -1:
        ans.append(str(0))
    else:
        ans.append(str(d))

# print(ans)
print(''.join(ans))
