import sys
from math import gcd

input = lambda: sys.stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


def gcd_small(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a


def solution():
    n, m = [int(num) for num in input().split()]
    print('1' * gcd(n, m))


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
