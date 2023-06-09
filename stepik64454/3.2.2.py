import sys


def input():
    return sys.stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


def solution():
    n = int(input())
    a = [int(num) for num in input().split()]
    dp = [-10 ** 20 for i in range(n + 1)]
    dp[0] = 0
    for i in range(1, n + 1):
        ans1, ans2, ans3 = -10 ** 20, -10 ** 20, dp[i - 1]
        if i - 5 >= 0:
            ans1 = dp[i - 5]
        if i - 3 >= 0:
            ans2 = dp[i - 3]
        dp[i] = max(ans1, ans2, ans3) + a[i - 1]
    print(dp[n])


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
