import sys


def input():
    return sys.stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


def solution():
    n = int(input())
    if n == 0:
        print(1)
        return
    dp = [[0 for j in range(n)] for i in range(3)]
    dp[0][0] = 1
    dp[1][0] = 1
    dp[2][0] = 1
    for i in range(1, n):
        dp[0][i] = dp[0][i - 1] + dp[1][i - 1] + dp[2][i - 1]
        dp[1][i] = dp[1][i - 1] + dp[2][i - 1]
        dp[2][i] = dp[0][i - 1] + dp[1][i - 1] + dp[2][i - 1]
    print(dp[0][n - 1] + dp[1][n - 1] + dp[2][n - 1])


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()