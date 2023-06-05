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
    n, m = (int(num) for num in input().split())
    print(pow(n % m, n, m))


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
