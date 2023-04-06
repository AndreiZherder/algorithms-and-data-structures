import sys

input = lambda: sys.stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


def prime_factors(n: int):
    """
    Prime factors of n
    prime_factors(99) --> 3 3 11
    """
    while n % 2 == 0:
        yield 2
        n //= 2
    p = 3
    while p * p <= n:
        quotient, reminder = divmod(n, p)
        if reminder == 0:
            yield p
            n = quotient
        else:
            p += 2
    if n != 1:
        yield n


def solution():
    l, r = [int(num) for num in input().split()]
    ans = [10 ** 20 for i in range(l, r + 1)]
    for i in range(l, r + 1):
        if ans[i - l] == 10 ** 20:
            p = next(prime_factors(i))
            for j in range(i, r + 1, p):
                ans[j - l] = min(ans[j - l], p)
    print(*ans)


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
