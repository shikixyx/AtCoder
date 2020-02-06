# 入力
N = int(input())

# Dは配列に
D = []
for i in range(N):
    d = int(input())
    D.append(d)

# こんな書き方もある
#D = [int(input()) for _ in range(N)]

# 並び替えて、前のと同じなら入れない
D.sort()
newD = []

prev = -1
for d in D:
    if prev != d:
        newD.append(d)

    prev = d

# 実はuniqueで一発

print(len(newD))
