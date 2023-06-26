from functools import lru_cache
from sys import stdin, stdout


def input():
    return stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    stdout.write(sep.join(map(str, args)))
    stdout.write(end)


def solution():
    @lru_cache(None)
    def dp(i: int, total: int) -> int:
        if i == n:
            return total
        ans = 0
        if total + w[i] <= s:
            ans = max(ans, dp(i + 1, total + w[i]))
        ans = max(ans, dp(i + 1, total))
        return ans
    s, n = [int(num) for num in input().split()]
    w = [int(num) for num in input().split()]
    print(dp(0, 0))


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
