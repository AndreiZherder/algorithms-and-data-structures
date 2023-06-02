import sys


def input():
    return sys.stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


def solution():
    n = int(input())
    if n % 3 == 0:
        print(n // 3)
    elif n % 3 == 2:
        print((n - 2) // 3 + (2 ** 64 - 1) // 3 + 1)
    else:
        print((n - 1) // 3 + (2 ** 64 - 1) // 3 * 2 + 1)


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
