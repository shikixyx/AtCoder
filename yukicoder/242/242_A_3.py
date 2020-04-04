import sys
sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

# AC

N, X, Y, Z = map(int, input().split())
A = list(map(int, input().split()))
A = [a + 1 for a in A]

for i in range(N):
    if Z == 0:
        break

    a = A[i]
    man = a // 10000
    if man == 0:
        continue
    num = man if man <= Z else Z
    A[i] -= num * 10000
    Z -= num

A.sort(reverse=True)

for i in range(N):
    a = A[i]
    if Z == 0:
        break
    if a <= 0:
        continue

    man = -(-a // 10000)

    num = man if man <= Z else Z
    A[i] -= num * 10000
    Z -= num


for i in range(N):
    if Y == 0:
        break

    a = A[i]

    if a <= 0:
        continue

    gosen = a // 5000
    if gosen == 0:
        continue
    num = gosen if gosen <= Y else Y
    A[i] -= num * 5000
    Y -= num


A.sort(reverse=True)

for i in range(N):
    a = A[i]
    if Y == 0:
        break
    if a <= 0:
        continue

    gosen = -(-a // 5000)

    num = gosen if gosen <= Y else Y
    A[i] -= num * 5000
    Y -= num


for i in range(N):
    a = A[i]

    if a <= 0:
        continue

    if X == 0:
        print('No')
        exit()

    sen = -(-a // 1000)
    num = sen if sen <= X else X
    a -= num * 1000
    X -= num

    if a > 0:
        print('No')
        exit()


print('Yes')
exit()
