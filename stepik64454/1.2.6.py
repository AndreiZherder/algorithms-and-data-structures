import sys
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
    s = tuple(s)
    digits = '13456789'

    for perm in permutations(digits, len(s)):
        if perm > s:
            print(''.join(perm))
            return
    print(''.join(next(permutations(digits, len(s) + 1))))


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
