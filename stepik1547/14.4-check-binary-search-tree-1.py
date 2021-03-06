"""
Проверка свойства дерева поиска
Проверить, является ли данное двоичное дерево деревом поиска.
Вход. Двоичное дерево.
Выход. Проверить, является ли оно корректным деревом
поиска: верно ли, что для любой вершины дерева ее ключ
больше всех ключей в левом поддереве данной вершины и
меньше всех ключей в правом поддереве.
Вы тестируете реализацию двоичного дерева поиска. У вас уже на-
писан код, который ищет, добавляет и удаляет ключи, а также выво-
дит внутреннее состояние структуры данных после каждой операции.
Вам осталось проверить, что в каждый момент дерево остается кор-
ректным деревом поиска. Другими словами, вы хотите проверить,
что для дерева корректно работает поиск, если ключ есть в дереве,
то процедура поиска его обязательно найдет, если ключа нет — то не
найдет.

Формат входа. Первая строка содержит число вершин n. Вершины
дерева пронумерованы числами от 0 до n-1. Вершина 0 является
корнем. Каждая из следующих n строк содержит информацию о
вершинах 0; 1; : : : ; n-1: i-я строка задајт числа keyi, lefti и righti,
где keyi — ключ вершины i, lefti — индекс левого сына верши-
ны i, а righti — индекс правого сына вершины i. Если у верши-
ны i нет одного или обоих сыновей, соответствующее значение
равно -1.
Формат выхода. Выведите «CORRECT», если дерево является кор-
ректным деревом поиска, и «INCORRECT» в противном случае.
Ограничения. 0 <= n <= 105; -2^31 < keyi < 2^31 - 1; -1 <= lefti; righti <= n - 1.
Гарантируется, что вход задает корректное двоичное де-
рево: в частности, если lefti != -1 и righti != -1, то lefti != righti;
никакая вершина не является сыном двух вершин; каждая вер-
шина является потомком корня.

Пример.
Вход:
3
2 1 2
1 -1 -1
3 -1 -1
Выход:
CORRECT

Пример.
Вход:
3
1 1 2
2 -1 -1
3 -1 -1
Выход:
INCORRECT

Пример.
Вход:
0
Выход:
CORRECT
Пустое дерево считается корректным.

Пример.
Вход:
5
1 -1 1
2 -1 2
3 -1 3
4 -1 4
5 -1 -1
Выход:
CORRECT


Пример.
Вход:
7
4 1 2
2 3 4
6 5 6
1 -1 -1
3 -1 -1
5 -1 -1
7 -1 -1
Выход:
CORRECT

Пример.
Вход:
4
4 1 -1
2 2 3
1 -1 -1
5 -1 -1
Выход:
INCORRECT
"""
import sys
from collections import namedtuple
from typing import List

Node = namedtuple('Node', 'key left right')


class Tree:
    def __init__(self, nodes: List[Node]):
        self.nodes = nodes

    def check(self, i: int) -> (bool, int, int):
        if not self.nodes:
            return True, 0, 0
        left_maximum = -2 ** 31
        left_minimum = 2 ** 31 - 1
        right_maximum = -2 ** 31
        right_minimum = 2 ** 31 - 1
        if self.nodes[i].left != -1:
            res = self.check(self.nodes[i].left)
            if not res[0] or res[1] >= self.nodes[i].key:
                return False, 0, 0
            left_maximum = res[1]
            left_minimum = res[2]
        if self.nodes[i].right != -1:
            res = self.check(self.nodes[i].right)
            if not res[0] or res[2] <= self.nodes[i].key:
                return False, 0, 0
            right_maximum = res[1]
            right_minimum = res[2]
        maximum = max(left_maximum, right_maximum, self.nodes[i].key)
        minimum = min(left_minimum, right_minimum, self.nodes[i].key)
        return True, maximum, minimum


def main():
    sys.setrecursionlimit(100000)
    n = int(input())
    tree = Tree([Node(*map(int, input().split())) for _ in range(n)])
    print('CORRECT' if tree.check(0)[0] else 'INCORRECT')


if __name__ == '__main__':
    main()
