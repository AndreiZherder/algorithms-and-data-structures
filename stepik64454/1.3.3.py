import sys
from bisect import bisect_left


def input():
    return sys.stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


def solution():
    n, m = [int(num) for num in input().split()]
    a = [int(num) for num in input().split()]
    ans = []
    while m:
        x = int(input())
        i = bisect_left(a, x)
        if i < n and a[i] == x:
            ans.append('YES')
        else:
            ans.append('NO')
        m -= 1
    print('\n'.join(ans))


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
