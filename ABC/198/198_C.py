import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def main():
    R, X, Y = map(int, input().split())

    D = (X ** 2) + (Y ** 2)
    a_2 = D / (R * R)

    if X == 0 and Y == 0:
        print(0)
        exit()

    if D == (R * R):
        print(1)
        exit()

    if D < (R * R):
        print(2)
        exit()

    ans = 0
    for i in range(10 ** 6):
        if i * i < a_2:
            continue

        ans = i
        break

    print(ans)

    return


if __name__ == "__main__":
    main()
