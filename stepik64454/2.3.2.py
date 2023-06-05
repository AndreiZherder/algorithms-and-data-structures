import sys
from math import gcd


def input():
    return sys.stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


def solution():
    a, b, c = (int(num) for num in input().split())
    if c % gcd(a, b) == 0:
        print(1)
    else:
        print(0)


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
