import sys
sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

# AC(1WA)
# コーナーケース
# 20min


S = input()
LS = len(S)

LEFT = [None] * LS
RIGHT = [None] * LS

# 最寄りのR
near_R = 0
for i in range(LS):
    s = S[i]
    if s == 'R':
        near_R = i
    else:
        LEFT[i] = near_R

# 最寄りのL
near_L = LS - 1
for i in range(LS - 1, -1, -1):
    s = S[i]
    if s == 'L':
        near_L = i
    else:
        RIGHT[i] = near_L

ans = [0] * LS

# LEFTから
for i in range(LS):
    if LEFT[i] == None:
        continue

    near_R = LEFT[i]
    d = i - near_R
    if d % 2 == 0:
        ans[near_R] += 1
    else:
        ans[near_R+1] += 1

# RIGHT
for i in range(LS):
    if RIGHT[i] == None:
        continue

    near_L = RIGHT[i]
    d = near_L - i

    if d % 2 == 0:
        ans[near_L] += 1
    else:
        ans[near_L - 1] += 1

print(" ".join((map(str, ans))))
