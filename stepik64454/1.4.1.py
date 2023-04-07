import sys

input = lambda: sys.stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


def solution():
    n = int(input())
    a = [int(num) for num in input().split()]
    if a[-1] < 0:
        left = 0
        right = 10 ** 18
    else:
        left = -10 ** 18
        right = 0
    for i in range(100):
        mid = left + (right - left) / 2
        if sum(a[i] * pow(mid, n - i) for i in range(n)) + a[-1] < 0:
            left = mid
        else:
            right = mid
    print(mid)


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
