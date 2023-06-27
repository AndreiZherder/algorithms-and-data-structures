from functools import lru_cache
from math import ceil
from sys import stdin, stdout


def input():
    return stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    stdout.write(sep.join(map(str, args)))
    stdout.write(end)


def solution():

    s, n = [int(num) for num in input().split()]
    ws = [int(num) for num in input().split()]
    cs = [int(num) for num in input().split()]
    ans = 0
    for w, c in sorted(zip(ws, cs), key=lambda x: x[1] / x[0] if x[0] else 10 ** 20, reverse=True):
        if w < s:
            ans += c
            s -= w
        else:
            ans += ceil(s / w * c)
            break
    print(ans)


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
