import sys


def input():
    return sys.stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


mod = 1000000007


def madd(x: int, y: int) -> int:
    return (x + y) % mod


def msub(x: int, y: int) -> int:
    return (x - y) % mod


def mmul(x: int, y: int) -> int:
    return (x * y) % mod


def mdiv(x: int, y: int) -> int:
    """
    returns (x / y) % mod
    """
    return (x * pow(y, mod - 2, mod)) % mod


def solution():
    a, b, c, d = (int(num) for num in input().split())
    ans = mdiv(madd(mmul(a, d), mmul(b, c)), mmul(b, d))
    print(ans)


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
