import sys
from bisect import bisect_right
from itertools import permutations


def input():
    return sys.stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


def solution():
    s = input()
    if int(s) >= 98765431:
        print(-1)
        return
    s = list(s)
    digits = '13456789'
    perms = list(permutations(digits, len(s)))
    i = bisect_right(perms, tuple(s))
    if i < len(perms):
        print(''.join(perms[i]))
        return
    print(''.join(next(permutations(digits, len(s) + 1))))


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
