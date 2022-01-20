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
from collections import namedtuple
from typing import List

Node = namedtuple('Node', 'key left right')


class Tree:
    def __init__(self, nodes: List[Node]):
        self.nodes = nodes

    def inorder(self, i: int) -> (List[Node], int):
        height = 0
        stack = [i]
        i = self.nodes[i].left
        while stack:
            while i != -1:
                stack.append(i)
                height += 1
                i = self.nodes[i].left
            i = stack.pop()
            height -= 1
            yield self.nodes[i], height
            i = self.nodes[i].right
            if i != -1:
                stack.append(i)
                height += 1
                i = self.nodes[i].left

    def check(self) -> bool:
        if not self.nodes:
            return True
        nodes = self.inorder(0)
        prev = next(nodes)
        for node in nodes:
            if node[0].key < prev[0].key:
                return False
            if node[0].key == prev[0].key and prev[1] > node[1]:
                return False
            prev = node
        return True


def main():
    n = int(input())
    tree = Tree([Node(*map(int, input().split())) for _ in range(n)])
    print('CORRECT' if tree.check() else 'INCORRECT')


if __name__ == '__main__':
    main()
