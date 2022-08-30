"""
Даны n точек на прямой, нужно покрыть их k отрезками одинаковой длины ℓ.
Найдите минимальное ℓ.

Формат ввода
На первой строке n (1≤n≤10^5) и k (1≤k≤n). На второй n чисел xi (∣∣xi∣∣≤10^9).
Формат вывода
Минимальное такое ℓ, что точки можно покрыть k отрезками длины ℓ.
"""
from bisect import bisect_right
from typing import List


def solution(n: int, k: int, xs: List[int]) -> int:
    def cover(n: int, k: int, l: int, xs: List[int]) -> bool:
        i = 0
        while k:
            i = bisect_right(xs, xs[i] + l)
            if i == n:
                return True
            k -= 1
        return False

    xs.sort()
    left, right = 0, (xs[-1] - xs[0] + 1) // k
    while left <= right:
        mid = left + (right - left) // 2
        if cover(n, k, mid, xs):
            right = mid - 1
        else:
            left = mid + 1
    return left


def main():
    n, k = map(int, input().split())
    xs = list(map(int, input().split()))
    print(solution(n, k, xs))


if __name__ == '__main__':
    main()
