import sys


def input():
    return sys.stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


def solution():
    n = int(input())
    dp = [0 for i in range(n + 1)]
    for i in range(2, n + 1):
        best = 10 ** 20
        if i % 2 == 0:
            best = min(best, dp[i // 2])
        if i % 3 == 0:
            best = min(best, dp[i // 3])
        best = min(best, dp[i - 1])
        dp[i] = best + 1
    print(dp[n])


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
