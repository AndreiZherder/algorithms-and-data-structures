import sys


def input():
    return sys.stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


def solution():
    n, m = [int(num) for num in input().split()]
    mids = [int(num) for num in input().split()]
    left = -1
    right = n
    i = 0
    while left + 1 < right:
        mid = left + (right - left) // 2
        if mids[i] == 0:
            left = mid
        else:
            right = mid
        i += 1
    print(right)


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
