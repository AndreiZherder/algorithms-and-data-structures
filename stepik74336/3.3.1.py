import sys
from bisect import bisect_right

input = lambda: sys.stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


def solution():
    n, d = [int(num) for num in input().split()]
    a = [int(num) for num in input().split()]
    ans = 0
    j = 0
    for i in range(n):
        while j < n and a[j] - a[i] < d:
            j += 1
        ans += n - j
    print(ans)


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
