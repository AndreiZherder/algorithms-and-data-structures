from functools import lru_cache
from os import path
from sys import stdin, stdout


filename = "../templates/input.txt"
if path.exists(filename):
    stdin = open(filename, 'r')


def input():
    return stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    stdout.write(sep.join(map(str, args)))
    stdout.write(end)


def solution():
    @lru_cache(None)
    def dp(i: int, j: int, n: int) -> int:
        if n == 0:
            if i == 0 and j == 0:
                return 1
            else:
                return 0
        ans = 0
        ans += dp(i + 1, j, n - 1)
        ans += dp(i - 1, j, n - 1)
        ans += dp(i, j + 1, n - 1)
        ans += dp(i, j - 1, n - 1)
        return ans
    print(dp(0, 0, 20))


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
