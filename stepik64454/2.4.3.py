import sys
from math import gcd
from typing import Tuple


def input():
    return sys.stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


def solution():
    def egcd(a: int, b: int) -> Tuple[int, int, int]:
        """
        Given two integers a and b, returns (gcd(a, b), x, y) such that
        a * x + b * y == gcd(a, b).
        a * inv + mod * y = gcd(a, mod)
        """
        x0, x1, y0, y1 = 1, 0, 0, 1
        while b != 0:
            q, a, b = a // b, b, a % b
            x0, x1 = x1, x0 - q * x1
            y0, y1 = y1, y0 - q * y1
        return a, x0, y0


    def madd(x: int, y: int) -> int:
        return (x + y) % mod


    def mmul(x: int, y: int) -> int:
        return (x * y) % mod


    a, n, mod = (int(num) for num in input().split())
    g, inv, _ = egcd(a, mod)
    if g != 1:
        print(-1)
        return
    cur = inv % mod
    ans = cur
    for i in range(2, n + 1):
        cur = (cur * inv) % mod
        ans = madd(ans, mmul(i, cur))
    print(ans)


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
