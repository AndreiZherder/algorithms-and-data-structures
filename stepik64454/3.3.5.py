import sys


def input():
    return sys.stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


def solution():
    n, m = (int(num) for num in input().split())
    mod = 10 ** 9 + 123
    dp = [[0 for j in range(m + 3)] for i in range(n + 3)]
    dp[2][2] = 1

    for row in range(2, n + 2):
        i, j = row, 2
        while i >= 2 and j < m + 2:
            cur = dp[i][j]
            cur = (cur + dp[i - 2][j - 1]) % mod
            cur = (cur + dp[i - 2][j + 1]) % mod
            cur = (cur + dp[i - 1][j - 2]) % mod
            cur = (cur + dp[i + 1][j - 2]) % mod
            dp[i][j] = cur
            i -= 1
            j += 1
    for col in range(3, m + 2):
        i, j = n + 1, col
        while i >= 2 and j < m + 2:
            cur = dp[i][j]
            cur = (cur + dp[i - 2][j - 1]) % mod
            cur = (cur + dp[i - 2][j + 1]) % mod
            cur = (cur + dp[i - 1][j - 2]) % mod
            cur = (cur + dp[i + 1][j - 2]) % mod
            dp[i][j] = cur
            i -= 1
            j += 1
    print(dp[n + 1][m + 1])


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
