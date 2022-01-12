"""
Автоматический анализ программ
При автоматическом анализе программ возникает такая задача.
Система равенств и неравенств
Проверить, можно ли присвоить переменным целые значения, чтобы
выполнить заданные равенства вида xi = xj и неравенства вида xp != xq.

Вход. Число переменных n, а также список равенств вида
xi = xj и неравенства вида xp != xq.

Выход. Проверить, выполнима ли данная система.

Формат входа. Первая строка содержит числа n; e; d. Каждая из сле-
дующих e строк содержит два числа i и j и задает равенство
xi = xj . Каждая из следующих d строк содержит два числа i и j и
задает неравенство xi != xj.
Переменные индексируются с 1:x1; : : : ; xn.

Формат выхода. Выведите 1, если переменным x1; : : : ; xn можно
присвоить целые значения, чтобы все равенства и неравенства
выполнились. В противном случае выведите 0.
Ограничения. 1 <= n <= 10^5; 0 <= e; d; e + d <= 2 <= 10^5; 1 <= i; j <= n.

Пример.
Вход:
4 6 0
1 2
1 3
1 4
2 3
2 4
3 4
Выход:
1
Все переменные просто равны друг другу, поэтому система вы-
полнима.

Пример.
Вход:
6 5 3
2 3
1 5
2 5
3 4
4 2
6 1
4 6
4 5
Выход:
0
x1 = x2 = x3 = x4 = x5, но x4 != x5.
"""


class DSU:
    def __init__(self, n: int):
        self.parent = list(range(n))

    def find(self, i: int) -> int:
        root = i
        while root != self.parent[root]:
            root = self.parent[root]
        while i != root:
            tmp = i
            i = self.parent[i]
            self.parent[tmp] = root
        return root

    def union(self, i: int, j: int):
        i_id = self.find(i)
        j_id = self.find(j)
        if i_id == j_id:
            return
        self.parent[i_id] = j_id


def main():
    n, e, d = (int(num) for num in input().split())
    dsu = DSU(n)
    equals = (tuple(map(lambda num: int(num) - 1, input().split())) for _ in range(e))
    for equal in equals:
        dsu.union(equal[0], equal[1])
    diffs = (tuple(map(lambda num: int(num) - 1, input().split())) for _ in range(d))
    print(0 if any(dsu.find(diff[0]) == dsu.find(diff[1]) for diff in diffs) else 1)


if __name__ == '__main__':
    main()
