import sys
from functools import reduce
from math import gcd


def input():
    return sys.stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


def lcm(a: int, b: int) -> int:
    return a * b // gcd(a, b)


def solution():
    a, b = (int(num) for num in input().split())
    g = gcd(a, b)
    a //= g
    if a > 10 ** 18 / b:
        print(-1)
    else:
        print(a * b)


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
