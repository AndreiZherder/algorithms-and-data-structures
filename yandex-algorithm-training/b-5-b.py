"""
В этой задаче вам требуется найти непустой отрезок массива с максимальной суммой.
Формат ввода
В первой строке входных данных записано единственное число
n (1 ≤ n ≤ 3⋅10^5) -  размер массива.
Во второй строке записано n целых чисел
ai (−10^9 ≤ ai ≤ 10^9) - сам массив.

Формат вывода
Выведите одно число - максимальную сумму на отрезке в данном массиве.
-2 -3 4 -1 -2 1 5 -3
"""


def main():
    n = int(input())
    a = [int(num) for num in input().split()]
    ans = a[0]
    maximum = a[0]
    for i in range(1, n):
        maximum = max(a[i], maximum + a[i])
        ans = max(ans, maximum)
    print(ans)


if __name__ == '__main__':
    main()