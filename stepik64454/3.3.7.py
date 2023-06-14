import sys


def input():
    return sys.stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


def solution():
    mod = 10 ** 9 + 7
    n, m = (int(num) for num in input().split())
    pref_col = [[0 for j in range(m + 1)] for i in range(n + 1)]
    pref_diag = [[0 for j in range(m + 1)] for i in range(n + 1)]
    pref_col[1][1] = 1
    pref_diag[1][1] = 1
    cur = 1

    pref_row = 1
    for j in range(2, m + 1):
        i = 1
        cur = (pref_row + pref_col[i - 1][j] + pref_diag[i - 1][j - 1]) % mod
        pref_row = (pref_row + cur) % mod
        pref_col[i][j] = (pref_col[i - 1][j] + cur) % mod
        pref_diag[i][j] = (pref_diag[i - 1][j - 1] + cur) % mod

    for i in range(2, n + 1):
        pref_row = 0
        for j in range(1, m + 1):
            cur = (pref_row + pref_col[i - 1][j] + pref_diag[i - 1][j - 1]) % mod
            pref_row = (pref_row + cur) % mod
            pref_col[i][j] = (pref_col[i - 1][j] + cur) % mod
            pref_diag[i][j] = (pref_diag[i - 1][j - 1] + cur) % mod

    print(cur)


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
