import sys


def input():
    return sys.stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


def solution():
    def can_cut(mid: int) -> bool:
        return sum(length // mid for length in a) >= k

    n, k = [int(num) for num in input().split()]
    a = []
    for i in range(n):
        a.append(int(input()))
    left = 1
    right = max(a) + 1
    while left <= right:
        mid = left + (right - left) // 2
        if can_cut(mid):
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
