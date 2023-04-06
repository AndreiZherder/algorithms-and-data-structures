import sys

input = lambda: sys.stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


def solution():
    a = int(input())
    left, right = 1, a
    while left <= right:
        mid = left + (right - left) // 2
        if a < mid ** 2:
            right = mid - 1
        else:
            left = mid + 1
    print(left - 1)


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
