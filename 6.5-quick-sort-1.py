"""
В первой строке задано два целых числа 1≤n≤50000 и 1≤m≤50000 — количество отрезков и точек на прямой, соответственно.
Следующие n строк содержат по два целых числа a_i b_ib, a_i<=b_ia — координаты концов отрезков.
Последняя строка содержит m целых чисел — координаты точек. Все координаты не превышают 10^8  по модулю.
Точка считается принадлежащей отрезку, если она находится внутри него или на границе.
Для каждой точки в порядке появления во вводе выведите, скольким отрезкам она принадлежит.

Sample Input:

2 3
0 5
7 10
1 6 11
Sample Output:

1 0 0
"""
import bisect
import random
from typing import List


def partition(a: List[int], l: int, r: int):
    rand = random.randrange(l, r + 1)
    a[l], a[rand] = a[rand], a[l]
    x = a[l]
    j1 = l
    j2 = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j2 += 1
            a[i], a[j2] = a[j2], a[i]
    for i in range(l + 1, j2 + 1):
        if a[i] < x:
            j1 += 1
            a[i], a[j1] = a[j1], a[i]
    a[l], a[j1] = a[j1], a[l]
    a[j1], a[j2] = a[j2], a[j1]
    return j1, j2


def quick_sort(a: List[int], l: int, r: int):
    while l < r:
        m1, m2 = partition(a, l, r)
        if m1 - l <= r - m2:
            quick_sort(a, l, m1 - 1)
            l = m2 + 1
        else:
            quick_sort(a, m2 + 1, r)
            r = m1 - 1


def main():
    n, m = (int(_) for _ in input().split())
    section_beginings = []
    section_endings = []
    for _ in range(n):
        section = [int(_) for _ in input().split()]
        section_beginings.append(section[0])
        section_endings.append(section[1])
    points = [int(_) for _ in input().split()]
    quick_sort(section_beginings, 0, n - 1)
    quick_sort(section_endings, 0, n - 1)
    for i in range(m):
        beginings_left_cnt = bisect.bisect(section_beginings, points[i])
        endings_left_cnt = bisect.bisect_left(section_endings, points[i])
        print(beginings_left_cnt - endings_left_cnt, end=' ')


if __name__ == '__main__':
    main()
