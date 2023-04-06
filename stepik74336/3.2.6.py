import sys
from bisect import bisect_right

input = lambda: sys.stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


def solution():
    n = int(input())
    a = [int(num) for num in input().split()]
    m = int(input())
    a.sort()
    i = 0
    while m:
        j = bisect_right(a, a[i])
        if j == n:
            print(a[i] + m // n)
            return
        if m <= j * (a[j] - a[i]):
            print(a[i] + m // j)
            return
        m -= j * (a[j] - a[i])
        i = j
    print(a[i])


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
