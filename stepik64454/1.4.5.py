import sys
from bisect import bisect_left

input = lambda: sys.stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


def solution():
    def can_arrange(mid: int) -> bool:
        x = xs[0]
        for i in range(k - 1):
            j = bisect_left(xs, x + mid)
            if j == n:
                return False
            x = xs[j]
        return True


    n, k = [int(num) for num in input().split()]
    xs = [int(num) for num in input().split()]
    left = 0
    right = xs[-1] - xs[0]
    while left <= right:
        mid = left + (right - left) // 2
        if can_arrange(mid):
            left = mid + 1
        else:
            right = mid - 1
    print(left - 1)


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
