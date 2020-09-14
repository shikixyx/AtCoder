import sys
from collections import Counter
from collections import defaultdict

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

IDX = defaultdict(list)

for i in range(N):
    a = A[i]
    IDX[a].append(i)

CA = Counter(A)
CB = Counter(B)

NEW_A = []
for x, c in CA.most_common():
    if c + CB[x] > N:
        print("No")
        exit()

    for i in IDX[x]:
        NEW_A.append((x, i))


USED = [False] * N
ANS = [0] * N
idx = 0

for x, c in CB.most_common():
    flg = True
    s = idx
    for k in range(c):
        for i in range(s, N):
            if USED[i]:
                if flg:
                    idx += 1
                continue

            if NEW_A[i][0] == x:
                flg = False
                continue

            j = NEW_A[i][1]
            USED[i] = True
            ANS[j] = x

            s = j + 1
            if flg:
                idx += 1
            break


print("Yes")
print(" ".join(map(str, ANS)))

