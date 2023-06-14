import sys


def input():
    return sys.stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


def solution():
    n, m = (int(num) for num in input().split())
    a = [[0 for j in range(m + 1)]]
    for i in range(n):
        a.append([0] + [int(num) for num in input().split()])
    dp = [[10 ** 20 for j in range(m + 1)] for i in range(n + 1)]
    dp[0][0] = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + a[i][j]
    ans = []
    i, j = n, m
    while i > 0 and j > 0:
        ans.append((i, j))
        if dp[i][j] == dp[i - 1][j] + a[i][j]:
            i -= 1
        elif dp[i][j] == dp[i][j - 1] + a[i][j]:
            j -= 1
        else:
            i -= 1
            j -= 1
    print(dp[n][m], len(ans))
    for i, j in reversed(ans):
        print(i, j)


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
