"""
Дано число 1 ≤ n ≤ 10^7. Необходимо найти последнюю цифру n-го числа Фибоначчи.
Как мы помним, числа Фибоначчи растут очень быстро, поэтому при их вычислении нужно быть аккуратным с переполнением.
В данной задаче, впрочем, этой проблемы можно избежать, поскольку нас интересует только последняя цифра числа Фибоначчи:
если a,b — последние цифры чисел F[i] F[i+1] соответственно, то (a+b) mod 10 — последняя цифра числа F[i+2]
Sample Input:

841645
Sample Output:

5
"""


def fib_digit(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    f1, f2 = 1, 0
    for _ in range(2, n + 1):
        f2, f1 = f1, (f1 + f2) % 10
    return f1


def main():
    n = int(input())
    print(fib_digit(n))


if __name__ == "__main__":
    main()
