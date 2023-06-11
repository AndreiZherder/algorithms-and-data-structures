import sys


def input():
    return sys.stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


def solution():
    n = int(input())
    dp1 = [-10 ** 20 for j in range(n)]
    dp1[0] = int(input())
    for i in range(1, n):
        m = i + 1
        a = [int(num) for num in input().split()]
        dp2 = [-10 ** 20 for j in range(n)]
        dp2[0] = a[0] + dp1[0]
        for j in range(1, m):
            dp2[j] = max(dp1[j], dp1[j - 1]) + a[j]
        dp1, dp2 = dp2, dp1
    print(max(dp1))


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
