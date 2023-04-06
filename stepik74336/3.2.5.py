import sys

input = lambda: sys.stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


def solution():
    n = int(input())
    left, right = 0, 10 ** 18
    while left <= right:
        mid = left + (right - left) // 2
        if n <= mid - (mid // 13 + mid // 17 - mid // (13 * 17)):
            right = mid - 1
        else:
            left = mid + 1
    print(left)


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
