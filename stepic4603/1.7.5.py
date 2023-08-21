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


def pascal_triangle(n: int) -> List[List[int]]:
    """
    returns pascal triangle
    which element [n][k] is the binomial coefficient
    or number of ways for selecting k elements out of n options without order
    """
    ans = [[0 for j in range(n + 1)] for i in range(n + 1)]
    for i in range(n + 1):
        ans[i][0] = 1
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            ans[i][j] = ans[i - 1][j - 1] + ans[i - 1][j]
    return ans


def solution():
    n = 10
    ans = 0
    pt = pascal_triangle(n)
    for i in range(1, n):
        ans += pt[n][i] * sum(pt[n - i][j] for j in range(1, n - i + 1))
    print(ans)


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
