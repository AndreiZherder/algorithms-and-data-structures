"""
Дано целое число 1 ≤ n ≤ 40, необходимо вычислить n-е число Фибоначчи
"""


def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    f1, f2 = 1, 0
    for _ in range(2, n + 1):
        f2, f1 = f1, f1 + f2
    return f1


def main():
    n = int(input())
    print(fib(n))


if __name__ == '__main__':
    main()
