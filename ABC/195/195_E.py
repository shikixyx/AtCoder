import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def main():
    N = int(input())
    S = list(input())[::-1]
    X = list(input())[::-1]

    can_win = [False] * 7
    can_win[0] = True

    flg = True
    for i in range(N):
        x = X[i]
        t = (int(S[i]) * pow(10, i, 7)) % 7
        next = [False] * 7

        if x == "A":
            for i in range(7):
                if can_win[i] and can_win[(i+t) % 7]:
                    next[i] = True
                else:
                    next[i] = False
        elif x == "T":
            for i in range(7):
                if can_win[(i+t) % 7]:
                    next[i] = True

                if can_win[i]:
                    next[i] = True

        if not any(next):
            flg = False
            break

        can_win = next

    if flg and can_win[0]:
        print("Takahashi")
    else:
        print("Aoki")

    return


if __name__ == "__main__":
    main()
