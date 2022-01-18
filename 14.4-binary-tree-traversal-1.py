"""
Обход двоичного дерева
Построить in-order, pre-order и post-order обходы данного двоичного де-
рева.
Вход. Двоичное дерево.
Выход. Все его вершины в трех разных порядках: in-order,
pre-order и post-order.
In-order обход соответствует следующей рекурсивной процедуре,
получающей на вход корень v текущего поддерева: произвести ре-
курсивный вызов для v.left, напечатать v.key, произвести рекурсив-
ный вызов для v.right.
Pre-order обход: напечатать v.key, произве-
сти рекурсивный вызов для v.left, произвести рекурсивный вызов для
v.right.
Post-order: произвести рекурсивный вызов для v.left, произве-
сти рекурсивный вызов для v.right, напечатать v.key.

Формат входа. Первая строка содержит число вершин n. Вершины
дерева пронумерованы числами от 0 до n-1. Вершина 0 является
корнем. Каждая из следующих n строк содержит информацию о
вершинах 0; 1; : : : ; n-1: i-я строка задает числа keyi, lefti и righti,
где keyi — ключ вершины i, lefti — индекс левого сына верши-
ны i, а righti — индекс правого сына вершины i. Если у верши-
ны i нет одного или обоих сыновей, соответствующее значение
равно -1.

Формат выхода. Три строки: in-order, pre-order и post-order обходы.
Ограничения. 1 <= n <= 10^5; 0 <= keyi <= 10^9; -1 <= lefti; righti <= n - 1.
Гарантируется, что вход задает корректное двоичное дерево: в
частности, если lefti != -1 и righti != -1, то lefti != righti; ника-
кая вершина не является сыном двух вершин; каждая вершина
является потомком корня.

Пример.
Вход:
5
4 1 2
2 3 4
5 -1 -1
1 -1 -1
3 -1 -1
Выход:
1 2 3 4 5
4 2 1 3 5
1 3 2 5 4

Пример.
Вход:
10
0 7 2
10 -1 -1
20 -1 6
30 8 9
40 3 -1
50 -1 -1
60 1 -1
70 5 4
80 -1 -1
90 -1 -1
Выход:
50 70 80 30 90 40 0 20 10 60
0 70 50 40 30 80 90 20 60 10
50 80 90 30 40 70 10 60 20 0
"""
from collections import namedtuple
from typing import List

Node = namedtuple('Node', 'key left right')


class Tree:
    def __init__(self, nodes: List[Node]):
        self.nodes = nodes

    def preorder(self, i: int):
        yield self.nodes[i].key
        if self.nodes[i].left != -1:
            yield from self.preorder(self.nodes[i].left)
        if self.nodes[i].right != -1:
            yield from self.preorder(self.nodes[i].right)

    def inorder(self, i: int):
        if self.nodes[i].left != -1:
            yield from self.inorder(self.nodes[i].left)
        yield self.nodes[i].key
        if self.nodes[i].right != -1:
            yield from self.inorder(self.nodes[i].right)

    def postorder(self, i: int):
        if self.nodes[i].left != -1:
            yield from self.postorder(self.nodes[i].left)
        if self.nodes[i].right != -1:
            yield from self.postorder(self.nodes[i].right)
        yield self.nodes[i].key


def main():
    n = int(input())
    tree = Tree([Node(*map(int, input().split())) for _ in range(n)])
    print(*tree.inorder(0))
    print(*tree.preorder(0))
    print(*tree.postorder(0))


if __name__ == '__main__':
    main()
