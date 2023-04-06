import sys
from bisect import bisect_right

input = lambda: sys.stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


def solution():
    n, d = [int(num) for num in input().split()]
    a = [int(num) for num in input().split()]
    i = 0
    j = n - 1
    ans = 0
    while i <= j:
        if a[i] + a[j] > d:
            j -= 1
            ans += 1
        else:
            i += 1
            j -= 1
            ans += 1
    print(ans)


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
