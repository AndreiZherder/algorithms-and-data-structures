import sys


def input():
    return sys.stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


def solution():
    n = int(input())
    a = [0] * 5 + [int(num) for num in input().split()]
    dp = [-10 ** 20 for i in range(n + 5)]
    dp[4] = 0
    for i in range(5, n + 5):
        dp[i] = max(dp[i - 5], dp[i - 3], dp[i - 1]) + a[i]
    i = n + 4
    ans = []
    while i > 4:
        ans.append(i - 4)
        if dp[i] == dp[i - 5] + a[i]:
            i -= 5
        elif dp[i] == dp[i - 3] + a[i]:
            i -= 3
        else:
            i -= 1
    print(dp[n + 4], len(ans))
    print(*reversed(ans))


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
