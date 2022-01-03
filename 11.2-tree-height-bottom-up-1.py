"""
Высота дерева
Вычислить высоту данного дерева.
Вход. Корневое дерево с вершинами 0; : : : ; n-1, заданное
как последовательность parent0; : : : ; parentn-1, где parenti —
родитель i-й вершины.
Выход. Высота дерева.

Деревья имеют огромное количество при-
менений в Computer Science. Они используются
как для представления данных, так и во мно-
гих алгоритмах машинного обучения. Далее
мы также узнаем, как сбалансированные де-
ревья используются для реализации словарей
и ассоциативных массивов. Данные структуры
данных так или иначе используются во всех
языках программирования и базах данных.
Ваша цель в данной задаче — научиться хранить и эффективно об-
рабатывать деревья, даже если в них сотни тысяч вершин.

Формат входа. Первая строка содержит натуральное число n. Вторая
строка содержит n целых чисел parent0; : : : ; parentn-1. Для каждо-
го 0 <= i <= n-1, parenti — родитель вершины i; если parenti = -1,
то i является корнем. Гарантируется, что корень ровно один. Га-
рантируется, что данная последовательность задает дерево.
Формат выхода. Высота дерева.
Ограничения. 1 <= n <= 10^5.

Пример.
Вход:
5
4 -1 4 1 1
Выход:
3

Пример.
Вход:
5
-1 0 4 0 3
Выход:
4
"""
from typing import List


def height(a: List[int], d: dict, i: int) -> int:
    if i in d:
        return d[i]
    if a[i] == -1:
        d[i] = 1
        return 1
    d[i] = 1 + height(a, d, a[i])
    return d[i]


def main():
    n = int(input())
    a = [int(num) for num in input().split()]
    d = {}
    print(max(height(a, d, i) for i in range(n)))


if __name__ == '__main__':
    main()
