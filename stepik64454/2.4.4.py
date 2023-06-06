import sys
from functools import lru_cache


def input():
    return sys.stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


mod = 1000000007


def madd(x: int, y: int) -> int:
    return (x + y) % mod


def msub(x: int, y: int) -> int:
    return (x - y) % mod


def mmul(x: int, y: int) -> int:
    return (x * y) % mod


def mdiv(x: int, y: int) -> int:
    """
    returns (x / y) % mod
    gcd(y, mod) should be 1
    """
    return (x * pow(y, mod - 2, mod)) % mod


def mpow(x: int, y: int) -> int:
    """
    returns (x ** y) % mod
    """
    return pow(x, y, mod)


def solution():
    n, m, l = (int(num) for num in input().split())
    fac = [0 for i in range(n + 1)]
    fac[0] = 1
    for i in range(1, n + 1):
        fac[i] = mmul(fac[i - 1], i)
    ans = 0
    for k in range(1, l + 1):
        if n < m * k:
            break
        num = fac[n]
        a = fac[msub(n, mmul(m, k))]
        b = fac[mmul(m, k)]
        den = mmul(a, b)
        ans = madd(ans, mdiv(num, den))
    print(ans)


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
