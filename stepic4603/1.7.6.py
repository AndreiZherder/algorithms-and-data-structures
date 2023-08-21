from functools import lru_cache
from math import perm, comb
from os import path
from sys import stdin, stdout
from typing import List

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
    def dp(i: int, prev: int, cnt: int, first_taken: bool) -> int:
        if i == n:
            if cnt == 0:
                return 1
            else:
                return 0
        ans = 0
        if i == n - 1:
            if first_taken:
                ans += dp(i + 1, prev, cnt, first_taken)
            else:
                if prev < i - 1:
                    ans += dp(i + 1, i, cnt - 1, first_taken)
                    ans += dp(i + 1, prev, cnt, first_taken)
                else:
                    ans += dp(i + 1, prev, cnt, first_taken)
        else:
            if i == 0:
                ans += dp(i + 1, i, cnt - 1, True)
                ans += dp(i + 1, prev, cnt, False)
            else:
                if prev < i - 1:
                    ans += dp(i + 1, i, cnt - 1, first_taken)
                    ans += dp(i + 1, prev, cnt, first_taken)
                else:
                    ans += dp(i + 1, prev, cnt, first_taken)
        return ans
    n = 8
    k = 3
    print(dp(0, -2, k, False))


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
