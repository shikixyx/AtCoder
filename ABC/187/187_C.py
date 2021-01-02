import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def main():
    N = int(input())

    pos = []
    neg = []

    for _ in range(N):
        s = input()
        if s[0] == "!":
            neg.append(s[1:])
        else:
            pos.append(s)

    neg.sort()
    pos.sort()

    i_n = 0
    i_p = 0
    l_n = len(neg)
    l_p = len(pos)

    flg = False
    ans = None
    while i_n < l_n and i_p < l_p:
        sn = neg[i_n]
        sp = pos[i_p]

        if sn == sp:
            ans = sn
            flg = True
            break
        elif sn > sp:
            i_p += 1
        elif sp > sn:
            i_n += 1

    if flg:
        print(ans)
    else:
        print("satisfiable")

    return


if __name__ == "__main__":
    main()
