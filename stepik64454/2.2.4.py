import sys


def input():
    return sys.stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


def solution():
    def f(x: int) -> int:
        ans = 0
        cur = 1
        for i in range(n + 1):
            ans = (ans + (cur * a[n - i]) % m) % m
            cur = (cur * x) % m
        return ans

    n, m = (int(num) for num in input().split())
    a = [int(num) for num in input().split()]
    for x in range(1, m + 1):
        if f(x) % m == 0:
            print(x)
            return
    print(-1)


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
