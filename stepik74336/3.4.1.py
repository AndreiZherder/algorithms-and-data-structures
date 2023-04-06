import sys
from bisect import bisect_left

input = lambda: sys.stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


def solution():
    n, m, d, s = [int(num) for num in input().split()]
    limits = [int(num) for num in input().split()]
    penalties = [int(num) for num in input().split()]
    ts = [int(num) for num in input().split()]
    for t in ts:
        print(penalties[bisect_left(limits, d / t - s)], end=' ')


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
