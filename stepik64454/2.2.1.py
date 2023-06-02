import sys


def input():
    return sys.stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


def solution():
    n = int(input())
    mod = 10 ** 6 + 3
    f1, f2 = 1, 0
    for i in range(2, n + 2):
        f2, f1 = f1, (f1 + f2) % mod
    print(f1)


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
