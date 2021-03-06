import sys
import math

sys.setrecursionlimit(10 ** 7)

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def inv_gcd(a, b):
    a %= b
    if a == 0:
        return b, 0
    # 初期状態
    s, t = b, a
    m0, m1 = 0, 1
    while t:
        # 遷移の準備
        u = s // t

        # 遷移
        s -= t * u
        m0 -= m1 * u

        # swap
        s, t = t, s
        m0, m1 = m1, m0

    if m0 < 0:
        m0 += b // s
    return s, m0


def inv_mod(x, m):
    assert 1 <= m
    z = inv_gcd(x, m)
    assert z[0] == 1
    return z[1]


def crt(r, m):
    assert len(r) == len(m)
    n = len(r)
    r0, m0 = 0, 1  # 初期値 x = 0 (mod 1)
    for i in range(n):
        assert m[i] >= 1

        #r1, m1は遷移に使う値
        r1, m1 = r[i] % m[i], m[i]

        # m0がm１以上になるようにする。
        if m0 < m1:
            r0, r1 = r1, r0
            m0, m1 = m1, m0

        # m0がm1の倍数のとき gcdはm1、lcmはm0
        # 解が存在すれば何も変わらないので以降の手順はスキップ
        if m0 % m1 == 0:
            if r0 % m1 != r1:
                return [0, 0]
            continue

        #  拡張ユークリッドの互除法によりgcd(m0, m1)と m0 * im = gcd (mod m1) を満たす imを求める
        g, im = inv_gcd(m0, m1)

        # 解の存在条件の確認
        if (r1 - r0) % g:
            return [0, 0]

        """
        r0, m0の遷移
        コメントアウト部分はACLでの実装
        C++なのでlong longを超えないようにしている
        C++ はlcm(m0, m1)で割った余りが負になり得る
        """
        # u1 = m1 // g
        # x = (r1 - r0) // g % u1 * im % u1
        # r0 += x * m0
        u1 = m0 * m1 // g
        r0 += (r1 - r0) // g * m0 * im % u1
        m0 = u1
        #if r0 < 0: r0 += m0

    return [r0, m0]


def solve():
    X, Y, P, Q = map(int, input().split())

    A = 2 * X + 2 * Y
    B = P + Q

    flg = False
    ans = 10 ** 20 + 100
    for y in range(X, X+Y):
        for q in range(P, P+Q):
            r, z = crt([y, q], [A, B])

            # print(y, A, q, B, r, z)
            if r == 0 and z == 0:
                continue

            flg = True
            ans = min(ans, r)

    if not flg:
        ans = "infinity"

    return ans


T = int(input())
ans = []
for _ in range(T):
    t = solve()
    ans.append(t)

print("\n".join(map(str, ans)))
