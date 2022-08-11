"""
Дан массив из N  целых чисел. Все числа от −10^9 до 10^9.
Нужно уметь отвечать на запросы вида “Cколько чисел имеют значения от L до R?”.

Формат ввода
Число N (1≤N≤10^5). Далее N целых чисел.
Затем число запросов
K (1≤K≤10^5).
Далее K пар чисел L, R (−10^9≤L≤R≤10^9) — собственно запросы.

Формат вывода
Выведите
K чисел — ответы на запросы.
"""
from bisect import bisect_right, bisect_left
from typing import List, Tuple


def solution(nums: List[int], queries: List[Tuple[int]]) -> List[int]:
    ans = []
    nums.sort()
    for left, right in queries:
        ans.append(bisect_right(nums, right) - bisect_left(nums, left))
    return ans


def main():
    n = int(input())
    nums = [int(num) for num in input().split()]
    k = int(input())
    queries = [tuple(int(num) for num in input().split()) for i in range(k)]
    print(*solution(nums, queries))


if __name__ == '__main__':
    main()
