"""
Данная задача полностью аналогична предыдущей, но проверять те-
перь нужно более общее свойство. Дереву разрешается содержать
равные ключи, но они всегда должны находиться в правом поддереве.
Формально, двоичное дерево называется деревом поиска, если для
любой вершины ее ключ больше всех ключей из ее левого поддерева
и не меньше всех ключей из правого поддерева.
Ограничения. 0 <= n <= 10^5;-2^31 <= keyi <= 2^31-1 (таким образом, в ка-
честве ключей допустимы минимальное и максимальное зна-
чение 32-битного целого типа, будьте осторожны с переполне-
нием); -1 <= lefti; righti <= n -1 1. Гарантируется, что вход зада-
ет корректное двоичное дерево: в частности, если lefti != -1 и
righti != -1, то lefti != righti; никакая вершина не является сыном
двух вершин; каждая вершина является потомком корня.

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
3
2 1 2
1 -1 -1
2 -1 -1
Выход:
CORRECT

Пример.
Вход:
3
2 1 2
2 -1 -1
3 -1 -1
Выход:
INCORRECT

Пример.
Вход:
1
2147483647 -1 -1
Выход:
CORRECT
2147483647

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
            if not res[0] or res[2] < self.nodes[i].key:
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
