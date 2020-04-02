import sys
sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

# AC
# 解答見た
# むずい
# BIT
# Binary Index Tree
# 二分探索

N = int(input())
P = list(map(int, input().split()))
p_to_i = {a: i for i, a in enumerate(P, 1)}


# A1 ... AnのBIT(1-indexed)
BIT = [0]*(N+1)


# A1 ~ Aiまでの和 O(logN)
def BIT_query(idx):
    res_sum = 0
    while idx > 0:
        res_sum += BIT[idx]
        idx -= idx & (-idx)
    return res_sum


# Ai += x O(logN)
def BIT_update(idx, x):
    while idx <= N:
        BIT[idx] += x
        idx += idx & (-idx)
    return


# x <= A1 - Ai となるiの最小値(1-indexed) O(logN)
def BIT_search(x):
    i = 0
    step = 1 << (N.bit_length() - 1)

    while step:
        if i + step <= N and BIT[i + step] < x:
            x -= BIT[i + step]
            i += step

        step >>= 1
    return i + 1


ans = 0
for p in range(N, 0, -1):
    i = p_to_i[p]

    #print("p == ", p, "i =", i)

    # 左,右
    LEFT = BIT_query(i)
    RIGHT = N - p - LEFT

    #print("LEFT,RIGHT : ", LEFT, RIGHT)

    cnt = 0

    # 左に0個 AND 右に0個の時
    if LEFT == 0 and RIGHT == 0:
        BIT_update(i, 1)
        continue

    # a ,,, b ,, i ,, c ,, d
    a = BIT_search(LEFT - 1) if LEFT >= 2 else 0
    b = BIT_search(LEFT) if LEFT >= 1 else 0
    c = BIT_search(LEFT + 1) if RIGHT >= 1 else N + 1
    d = BIT_search(LEFT + 2) if RIGHT >= 2 else N + 1

    if b != 0:
        cnt += (b - a) * (c - i)
    if c != N + 1:
        cnt += (d - c) * (i - b)

    BIT_update(i, 1)
    ans += p * cnt

    #print("a,b,c,d : ", a, b, c, d)
    #print("cnt,score :", cnt, cnt * p)
    #print("ans : ", ans)


print(ans)
