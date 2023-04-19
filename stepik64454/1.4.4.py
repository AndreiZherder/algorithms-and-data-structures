import sys

input = lambda: sys.stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


def solution():
    def can_print(mid: int) -> bool:
        return mid // x + mid // y >= n - 1


    n, x, y = [int(num) for num in input().split()]
    left = 0
    right = max(x, y) * n
    while left <= right:
        mid = left + (right - left) // 2
        if can_print(mid):
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
