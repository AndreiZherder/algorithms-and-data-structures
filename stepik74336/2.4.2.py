import sys

input = lambda: sys.stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


def sieve(n: int):
    """
    Primes <= n
    """
    primes = bytearray(n + 1)
    p = 3
    while p * p <= n:
        if not primes[p]:
            primes[p * p::p] = [1] * len(primes[p * p::p])
        p += 2
    if n >= 2:
        yield 2
    for p in range(3, n + 1, 2):
        if not primes[p]:
            yield p


def solution():
    l, r = [int(num) for num in input().split()]
    primes = (filter(lambda x: l <= x, sieve(r)))
    ans = []
    prev = next(primes, 0)
    for p in primes:
        if p - prev == 2:
            ans.append([prev, p])
        prev = p
    if not ans:
        print('empty')
    else:
        for prev, p in ans:
            print(prev, p)



def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
