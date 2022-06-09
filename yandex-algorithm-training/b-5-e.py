"""
Даны три массива целых чисел
A,B,C и целое число S.
Найдите такие
i,j,k, что Ai + Bj + Ck = S.

Формат ввода
На первой строке число S (1≤S≤10^9). Следующие три строки содержат описание массивов
A,B,C в одинаковом формате: первое число задает длину n соответствующего массива (1≤n≤15000), затем заданы
n целых чисел от 1 до 10^9 — сам массив.
Формат вывода
Если таких i,j,k не существует, выведите единственное число − 1. Иначе выведите на одной строке три числа — i,j,k.
Элементы массивов нумеруются с нуля. Если ответов несколько, выведите лексикографически минимальный.
"""
import random
from typing import List


def solution(s: int, a: List[int], b: List[int], c: List[int]) -> List[int]:
    d = {}
    for i, num in enumerate(c):
        if s - num not in d:
            d[s - num] = i
    for i, num1 in enumerate(a):
        for j, num2 in enumerate(b):
            if num1 + num2 in d:
                return [i, j, d[num1 + num2]]
    return [-1, -1, -1]


def main():
    # s = int(input())
    # _, *a = (int(num) for num in input().split())
    # _, *b = (int(num) for num in input().split())
    # _, *c = (int(num) for num in input().split())
    a = [random.randrange(10000) for i in range(15000)]
    b = [random.randrange(10000) for i in range(15000)]
    c = [random.randrange(10000) for i in range(15000)]
    s = 30000
    ans = solution(s, a, b, c)
    if ans[0] == -1:
        print(-1)
    else:
        print(*ans)


if __name__ == '__main__':
    main()
