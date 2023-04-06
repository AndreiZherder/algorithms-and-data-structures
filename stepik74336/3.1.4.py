import sys
from typing import List

input = lambda: sys.stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


def solution():
    def bisect_left(a: List[int], num: int) -> int:
        left, right = 0, len(a) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if num <= a[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return left

    def bisect_right(a: List[int], num: int) -> int:
        left, right = 0, len(a) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if num < a[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return left

    n = int(input())
    a = [int(num) for num in input().split()]
    m = int(input())
    b = [int(num) for num in input().split()]
    ans = []
    for num in b:
        i = bisect_left(a, num)
        j = bisect_right(a, num)
        if i == j:
            ans.append(0)
        else:
            ans.append((j + i + 1) // 2)
    print(*ans)


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
