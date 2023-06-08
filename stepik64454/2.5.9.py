import sys
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
        """
        x0, x1, y0, y1 = 1, 0, 0, 1
        while b != 0:
            q, a, b = a // b, b, a % b
            x0, x1 = x1, x0 - q * x1
            y0, y1 = y1, y0 - q * y1
        return a, x0, y0

    def minv(x: int) -> int:
        """
        returns modular inverse of x when mod is prime or not prime
        ans = (1 / x) % mod
        gcd(y, mod) should be 1
        """
        g, inv, _ = egcd(x, mod)
        if g != 1:
            raise ValueError('gcd(x, mod) != 1')
        return inv % mod

    def mdiv(x: int, y: int) -> int:
        """
        returns (x / y) % mod
        gcd(y, mod) should be 1
        """
        return (x * minv(y)) % mod

    mod = 1
    while True:
        mod += 2
        ans = mdiv(1, 2)
        print(mod, ans)
        if ans == 2020:
            break


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
