import sys

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def main():
    V,T,S,D = map(int,input().split())

    s = V * T
    e = V * S

    if s <= D <= e:
        print("No")
    else:
        print("Yes")
    return


if __name__ == "__main__":
    main()
