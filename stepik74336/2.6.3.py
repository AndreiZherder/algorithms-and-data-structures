import sys
from math import sqrt

input = lambda: sys.stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


def factors(n: int):
    i = 1
    p = i ** 2
    while p * i <= n:
        quotient, reminder = divmod(n, i)
        if reminder == 0:
            if int(sqrt(quotient)) ** 2 == quotient:
                yield quotient

        quotient, reminder = divmod(n, p)
        if reminder == 0:
            yield p
            if int(sqrt(quotient)) ** 2 == quotient:
                yield quotient
        i += 1
        p = i ** 2


def solution():
    n = int(input())
    print(max(factors(n)))


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
