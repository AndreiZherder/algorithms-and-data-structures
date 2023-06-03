import sys


def input():
    return sys.stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


def solution():
    n = int(input())
    mod = 10 ** 6 + 3
    if n >= mod:
        print(0)
        return
    ans = 1
    for i in range(2, n + 1):
        ans = (ans * i) % mod
    print(ans)


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
