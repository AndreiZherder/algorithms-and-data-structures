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
from typing import List, Tuple


def solution(s: int, a: List[Tuple[int, int]],
             b: List[Tuple[int, int]],
             c: List[Tuple[int, int]]) -> Tuple[int, int, int]:
    a.sort()
    b.sort()
    c.sort(key=lambda item: (item[0], -item[1]))
    ans = (15000, 15000, 15000)
    for num1, i in a:
        pos = len(c) - 1
        for num2, j in b:
            while pos >= 0 and c[pos][0] > s - (num1 + num2):
                pos -= 1
            if pos >= 0 and c[pos][0] == s - (num1 + num2):
                ans = min(ans, (i, j, c[pos][1]))

    return ans


def main():
    s = int(input())
    _, *a = ((int(num), i - 1) for i, num in enumerate(input().split()))
    _, *b = ((int(num), i - 1) for i, num in enumerate(input().split()))
    _, *c = ((int(num), i - 1) for i, num in enumerate(input().split()))
    ans = solution(s, a, b, c)
    if ans[0] == 15000:
        print(-1)
    else:
        print(*ans)


if __name__ == '__main__':
    main()
