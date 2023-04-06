import sys

input = lambda: sys.stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


def solution():
    n, x, y = [int(num) for num in input().split()]
    left, right = 0, min(x, y) * (n - 1)
    while left <= right:
        mid = left + (right - left) // 2
        if n - 1 <= mid // x + mid // y:
            right = mid - 1
        else:
            left = mid + 1
    print(min(x, y) + left)


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
