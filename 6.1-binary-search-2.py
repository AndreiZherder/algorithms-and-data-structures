"""
1. Найти позицию для вставки элемента в отсортированный массив слева от равных ему.
2. Найти позицию для вставки элемента в отсортированный массив справа от равных ему.
"""
from typing import List


def bisect_left(a: List[int], num: int) -> int:
    left = 0
    right = len(a) - 1
    while left <= right:
        middle = left + (right - left) // 2
        if num <= a[middle]:
            right = middle - 1
        else:
            left = middle + 1
    return left


def bisect_right(a: List[int], num: int) -> int:
    left = 0
    right = len(a) - 1
    while left <= right:
        middle = left + (right - left) // 2
        if num < a[middle]:
            right = middle - 1
        else:
            left = middle + 1
    return left


def main():
    a = [1, 3, 3, 3, 3, 3, 3, 5]
    print(bisect_left(a, 3))
    print(bisect_right(a, 3))


if __name__ == '__main__':
    main()
