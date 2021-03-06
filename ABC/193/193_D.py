import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def calc_score(S, x):
    NS = list(S)
    NS[4] = str(x)
    ret = 0
    for i in range(1, 10):
        t = i * pow(10, NS.count(str(i)))
        ret += t

    return ret


def main():
    K = int(input())
    S = input()
    T = input()

    CARD = [K] * 10
    for i in range(4):
        CARD[int(S[i])] -= 1
        CARD[int(T[i])] -= 1

    ans = 0.
    for i in range(1, 10):
        for j in range(1, 10):
            # カードが残っているか
            if i == j and CARD[i] <= 1:
                continue

            if CARD[i] < 1 or CARD[j] < 1:
                continue

            taka = calc_score(S, i)
            aoki = calc_score(T, j)

            if taka > aoki:
                if i == j:
                    t = CARD[i] * (CARD[i] - 1) / ((9*K - 8) * (9*K - 9))
                    ans += t
                else:
                    t = CARD[i] / (9*K - 8)
                    t *= CARD[j] / (9 * K - 9)
                    ans += t

    print(ans)

    return


if __name__ == "__main__":
    main()
