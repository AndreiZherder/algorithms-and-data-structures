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
    a, b = [int(num) for num in input().split()]
    print(a // gcd_small(a, b) * b)


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
