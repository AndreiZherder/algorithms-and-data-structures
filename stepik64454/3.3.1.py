import sys
from itertools import accumulate


def input():
    return sys.stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


def solution():
    n, m = [int(num) for num in input().split()]
    a = []
    for i in range(n):
        a.append([int(num) for num in input().split()])
    dp1 = list(accumulate(a[0]))
    dp2 = [0 for j in range(m)]
    for i in range(1, n):
        dp2[0] = dp1[0] + a[i][0]
        for j in range(1, m):
            dp2[j] = min(dp2[j - 1], dp1[j - 1], dp1[j]) + a[i][j]
        dp1, dp2 = dp2, dp1
    print(dp1[m - 1])


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
