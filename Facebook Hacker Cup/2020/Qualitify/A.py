import sys

sys.setrecursionlimit(10 ** 7)


T = int(input())


def solve():
    N = int(input())
    I = list(input())
    O = list(input())

    ans = []
    for i in range(1, N + 1):
        t = ["N"] * N
        t[i - 1] = "Y"

        # front
        for j in range(i, N + 1):
            if i == j:
                continue

            if O[j - 2] == "Y" and I[j - 1] == "Y" and t[j - 2] == "Y":
                t[j - 1] = "Y"
            else:
                break

        # back
        for j in range(1, i + 1)[::-1]:
            if i == j:
                continue

            if O[j] == "Y" and I[j - 1] == "Y" and t[j] == "Y":
                t[j - 1] = "Y"
            else:
                break

        ans.append("".join(t))
    return "\n".join(ans)


ans = []
for i in range(1, T + 1):
    t = solve()
    txt = "Case #{}:".format(i)
    ans.append(txt)
    ans.append(t)

print("\n".join(ans))

