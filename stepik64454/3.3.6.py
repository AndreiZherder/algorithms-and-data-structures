import sys


def input():
    return sys.stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


def solution():
    mod = 10 ** 9 + 33
    n, m = (int(num) for num in input().split())
    pref_row = [[0 for j in range(m + 1)] for i in range(n + 1)]
    pref_col = [[0 for j in range(m + 1)] for i in range(n + 1)]
    pref_row[1][1] = 1
    pref_col[1][1] = 1
    cur = 1

    for i in range(2, n + 1):
        j = 1
        cur = (pref_row[i][j - 1] + pref_col[i - 1][j]) % mod
        pref_row[i][j] = (pref_row[i][j - 1] + cur) % mod
        pref_col[i][j] = (pref_col[i - 1][j] + cur) % mod

    for j in range(2, m + 1):
        i = 1
        cur = (pref_row[i][j - 1] + pref_col[i - 1][j]) % mod
        pref_row[i][j] = (pref_row[i][j - 1] + cur) % mod
        pref_col[i][j] = (pref_col[i - 1][j] + cur) % mod

    for i in range(2, n + 1):
        for j in range(2, m + 1):
            cur = (pref_row[i][j - 1] + pref_col[i - 1][j]) % mod
            pref_row[i][j] = (pref_row[i][j - 1] + cur) % mod
            pref_col[i][j] = (pref_col[i - 1][j] + cur) % mod

    print(cur)


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
