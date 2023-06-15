import sys


def input():
    return sys.stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


def solution():
    n = int(input())
    dp = [10 ** 20 for i in range(n + 1)]
    dp[1] = 0
    for i in range(2, n + 1):
        x1 = dp[i // 2] if i % 2 == 0 else 10 ** 20
        x2 = dp[i // 3] if i % 3 == 0 else 10 ** 20
        x3 = dp[i - 1]
        dp[i] = min(x1, x2, x3) + 1
    i = n
    ans = [i]
    while i != 1:
        x1 = dp[i // 2] if i % 2 == 0 else 10 ** 20
        x2 = dp[i // 3] if i % 3 == 0 else 10 ** 20
        x3 = dp[i - 1]
        if x1 + 1 == dp[i]:
            i //= 2
        elif x2 + 1 == dp[i]:
            i //= 3
        else:
            i -= 1
        ans.append(i)
    print(dp[n])
    print(*reversed(ans))


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
