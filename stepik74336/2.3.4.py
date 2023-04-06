import math
import sys

input = lambda: sys.stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


def solution():
    n = int(input())
    ans = -1

    while n % 2 == 0:
        ans = 2
        n >>= 1

    while n % 3 == 0:
        ans = 3
        n = n // 3

    for i in range(5, int(math.sqrt(n)) + 1, 6):
        while n % i == 0:
            ans = i
            n = n // i
        while n % (i + 2) == 0:
            ans = i + 2
            n = n // (i + 2)

    if n > 4:
        ans = n

    print(ans)



def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
