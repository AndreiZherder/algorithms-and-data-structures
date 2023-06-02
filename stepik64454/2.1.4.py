import sys


def input():
    return sys.stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


def solution():
    n = int(input())
    sieve = [0 for i in range(n + 1)]
    sieve[4::2] = [2] * len(sieve[4::2])
    p = 3
    while p * p <= n:
        if not sieve[p]:
            for i in range(p * p, n + 1, p):
                if not sieve[i]:
                    sieve[i] = p
        p += 2
    print(sum(sieve))


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
