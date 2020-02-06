# 入力
N = int(input())
A = list(map(int, input().split()))

# 降順で並び替え
A.sort(reverse=True)

alice = 0
bob = 0

# カードとる
for i in range(N):
    # 0,2...はalice
    if i % 2 == 0:
        alice += A[i]

    # 1,3...はbob
    else:
        bob += A[i]

print(alice - bob)
