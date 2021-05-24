import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def main():
    S = list(input())

    cnt = 0
    for i in range(10000):
        s = str(i).zfill(4)

        flg = True
        for j in range(10):
            if S[j] == "?":
                continue

            if S[j] == "o":
                if str(j) in s:
                    continue
                else:
                    flg = False
                    break

            if S[j] == "x":
                if not str(j) in s:
                    continue
                else:
                    flg = False
                    break

        if flg:
            cnt += 1

    print(cnt)

    return


if __name__ == "__main__":
    main()
