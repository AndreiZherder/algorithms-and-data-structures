import sys
from typing import List

input = lambda: sys.stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


def solution():
    def bisect(a: List[int], num: int) -> int:
        left, right = 0, len(a) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if num == a[mid]:
                return mid + 1
            if num < a[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return 0

    n = int(input())
    a = [int(num) for num in input().split()]
    m = int(input())
    b = [int(num) for num in input().split()]
    print(*[bisect(a, num) for num in b])


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
