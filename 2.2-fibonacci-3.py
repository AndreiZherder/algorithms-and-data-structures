"""
Даны целые числа 1≤n≤10^18 2≤m≤10^5
Необходимо найти остаток от деления n-го числа Фибоначчи на m.

Sample Input:

10 2
Sample Output:

1
[
    { "n": "9", "m": 2, "expected": 0 },
    { "n": "10", "m": 2, "expected": 1 },
    { "n": "1025", "m": 55, "expected": 5 },
    { "n": "12589", "m": 369, "expected": 89 },
    { "n": "1598753", "m": 25897, "expected": 20305 },
    { "n": "60282445765134413", "m": 2263, "expected": 974 }
]
https://ru.wikipedia.org/wiki/Период_Пизано
https://en.wikipedia.org/wiki/Pisano_period
https://oeis.org/A001175
"""


def fib_mod(n, m):
    if n == 0:
        return 0
    if n == 1:
        return 1
    f2, f1 = 0, 1
    for i in range(2, n + 1):
        f2, f1 = f1, (f1 + f2) % m
        if f2 == 0 and f1 == 1:
            pisano_period = i - 1
            break
    else:
        return f1
    return fib_mod(n % pisano_period, m)


def main():
    n, m = map(int, input().split())
    print(fib_mod(n, m))


if __name__ == "__main__":
    main()
