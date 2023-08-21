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
    def dp(i: int, odd: int, even: int) -> int:
        if i == 6:
            return 1
        ans = 0
        if odd:
            ans += 5 * dp(i + 1, odd - 1, even)
        if even:
            ans += (4 if i == 0 else 5) * dp(i + 1, odd, even - 1)
        return ans
    print(dp(0, 3, 3))


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
