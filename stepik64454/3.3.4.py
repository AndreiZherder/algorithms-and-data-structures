import sys


def input():
    return sys.stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


def solution():
    mod = 10 ** 9 + 9
    n, m = [int(num) for num in input().split()]
    a = []
    for i in range(n):
        a.append([int(num) for num in input().split()])
    dp1 = [0 for j in range(m + 1)]
    dp1[0] = 1 if a[0][0] == 0 else 0
    dp2 = [0 for j in range(m + 1)]
    for i in range(n):
        for j in range(1, m + 1):
            dp2[j] = (dp2[j - 1] + dp1[j - 1] + dp1[j]) % mod if a[i][j - 1] == 0 else 0
        dp1, dp2 = dp2, dp1
        dp2[0] = 0
    print(dp1[m])


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
