"""
Дано кубическое уравнение ax3+bx2+cx+d=0 (a≠0). Известно, что у этого уравнения есть ровно один корень.
Требуется его найти.

Формат ввода
Во входном файле через пробел записаны четыре целых числа: -1000<=a,b,c,d<=1000.

Формат вывода
Выведите единственный корень уравнения с точностью не менее 5 знаков после десятичной точки.
"""


def solution(a: int, b: int, c: int, d: int) -> float:
    def y(x: float) -> float:
        return a * x ** 3 + b * x ** 2 + c * x + d

    left = -10000
    right = 10000
    sign = 1
    eps = 10 ** -15
    if y(left) > y(right):
        sign = -1
    x = left + (right - left) / 2
    f = y(x)
    k = 1
    while abs(f) > eps:
        if (sign * f) < 0:
            left = x
        else:
            right = x
        x = left + (right - left) / 2
        f = y(x)
        k += 1
        if k == 1000000:
            return x
    return x


def main():
    a, b, c, d = (int(num) for num in input().split())
    print(f'{solution(a, b, c, d):.10f}')


if __name__ == '__main__':
    main()
