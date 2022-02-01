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


def gcd(a, b):
    m = a
    n = b
    great_common_divisor = 1
    while n != m and n > 1 and m > 1:
        if m % 2 == 0 and n % 2 == 0:
            m //= 2
            n //= 2
            great_common_divisor *= 2
        elif m % 2 == 0:
            m //= 2
        elif n % 2 == 0:
            n //= 2
        elif n > m:
            tmp = m
            m = (n - m) // 2
            n = tmp
        else:
            m = (m - n) // 2
    if m == n:
        great_common_divisor *= n
    if m == 0:
        great_common_divisor *= n
    if n == 0:
        great_common_divisor *= m
    return great_common_divisor


def main():
    a, b = map(int, input().split())
    print(gcd(a, b))


if __name__ == '__main__':
    main()
