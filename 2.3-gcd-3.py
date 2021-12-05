"""
По данным двум числам 1≤a,b≤2⋅10^9 найдите их наибольший общий делитель.

Sample Input 1:

18 35
Sample Output 1:

1
Sample Input 2:

14159572 63967072
Sample Output 2:

4
"""
import random


def gcd(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    if a >= b:
        return gcd(a % b, b)
    else:
        return gcd(a, b % a)


def gcd1(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    return gcd(b % a, a)


def test(gcd, n=100):
    for i in range(n):
        c = random.randint(1, 1024)
        a = c * random.randint(1, 128)
        b = c * random.randint(1, 128)
        assert gcd(a, a) == gcd(a, 0) == a
        assert gcd(b, b) == gcd(b, 0) == b
        assert gcd(a, 1) == gcd(b, 1) == 1
        d = gcd(a, b)
        print(d)
        assert a % d == b % d == 0


def main():
    test(gcd1)


if __name__ == '__main__':
    main()
