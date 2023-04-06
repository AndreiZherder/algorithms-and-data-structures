import sys

input = lambda: sys.stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


def gcd_small(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a


def solution():
    x1, y1 = [int(num) for num in input().split()]
    x2, y2 = [int(num) for num in input().split()]
    dx, dy = abs(x1 - x2), abs(y1 - y2)
    print(gcd_small(dx, dy) + 1)


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
