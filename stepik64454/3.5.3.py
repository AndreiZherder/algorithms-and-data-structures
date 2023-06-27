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
        ans = dp(i + 1, total)
        if total + w[i] <= s:
            ans = max(ans, dp(i + 1, total + w[i]))
        return ans
    s, n = [int(num) for num in input().split()]
    w = [int(num) for num in input().split()]
    ans = dp(0, 0)
    path = []
    total = 0
    for i in range(n):
        if total + w[i] <= s and dp(i + 1, total + w[i]) > dp(i + 1, total):
            path.append(i + 1)
            total += w[i]
    print(ans, len(path))
    print(*path)


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
