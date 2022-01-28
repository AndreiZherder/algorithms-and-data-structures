"""
Ваша цель в данной задаче — реализовать структуру данных Rope.
Данная структура данных хранит строку и позволяет эффективно вы-
резать кусок строки и переставить его в другое место.
Формат входа. Первая строка содержит исходную строку S, вто-
рая — число запросов q. Каждая из последующих q строк задает
запрос тройкой чисел i; j; k и означает следующее: вырезать под-
строку S[i::j] (где i и j индексируются с нуля) и вставить ее после
k-го символа оставшейся строки (где k индексируется с едини-
цы), при этом если k = 0, то вставить вырезанный кусок надо в
начало.
Формат выхода. Выведите полученную (после всех q запросов) стро-
ку.
Ограничения. S содержит только буквы латинского алфавита.
1 <= |S| <= 300 000; 1 <= q <= 100 000; 0 <= i <= j  <= n - 1; 0 <= k <= n-(j-i+1).

Пример.
Вход:
hlelowrold
2
1 1 2
6 6 7
Выход:
helloworld
hlelowrold - hellowrold - helloworld

Пример.
Вход:
abcdef
2
0 1 1
4 5 0
Выход:
efcabd
abcdef - cabdef - efcabd
"""
import random
import time
from collections import namedtuple
from typing import Optional


class Node:
    def __init__(self, key: str = None, parent: 'Node' = None):
        self.parent = parent
        self.key = key
        self.left: Optional['Node'] = None
        self.right: Optional['Node'] = None
        self.height = 0
        self.size = 1

    def __str__(self):
        lines, *_ = self.__display_aux()
        return '\n'.join(lines)

    def __getitem__(self, i) -> Optional['Node']:
        node = self
        pos = node.size - (node.right.size if node.right else 0) - 1
        if i == pos:
            return node
        elif i < pos:
            return node.left[i] if node.left else None
        else:
            return node.right[i - (node.left.size + 1 if node.left else 1)] if node.right else None

    def __display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if not self.right and not self.left:
            line = f"{self.key}({self.height})({self.size})"
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if not self.right:
            lines, n, p, x = self.left.__display_aux()
            s = f"{self.key}({self.height})({self.size})"
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if not self.left:
            lines, n, p, x = self.right.__display_aux()
            s = f"{self.key}({self.height})({self.size})"
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left.__display_aux()
        right, m, q, y = self.right.__display_aux()
        s = f"{self.key}({self.height})({self.size})"
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

    def delete(self, node: 'Node') -> Optional['Node']:
        # no children
        if not node.left and not node.right:
            if not node.parent:
                return None
            if node.parent.left == node:
                node.parent.left = None
            else:
                node.parent.right = None
            node.parent.update_heights()

            node = node.parent
            ret = node
            while node:
                node = self.balance(node)
                ret = node
                node = node.parent
            return ret

        # one child
        elif (node.left and not node.right) or (node.right and not node.left):
            child = node.left if node.left else node.right
            if not node.parent:
                child.parent = None
                return child
            else:
                if node.parent.left == node:
                    node.parent.left = child
                else:
                    node.parent.right = child
                child.parent = node.parent
                node.parent.update_heights()

                node = node.parent
                ret = node
                while node:
                    node = self.balance(node)
                    ret = node
                    node = node.parent
                return ret

        # two children
        else:
            node2 = node.left
            while node2.right:
                node2 = node2.right
            node.key, node2.key = node2.key, node.key
            return self.delete(node2)

    def next_node(self) -> Optional['Node']:
        if self.right:
            node = self.right
            while node.left:
                node = node.left
            return node
        else:
            node = self
            while node.parent and node.parent.right == node:
                node = node.parent
            return node.parent

    def prev_node(self) -> Optional['Node']:
        if self.left:
            node = self.left
            while node.right:
                node = node.right
            return node
        else:
            node = self
            while node.parent and node.parent.left == node:
                node = node.parent
            return node.parent

    def update_heights(self):
        node = self
        while node:
            left_height = node.left.height if node.left else 0
            right_height = node.right.height if node.right else 0
            node.height = (1 + max(left_height, right_height)) if (node.left or node.right) else 0
            left_size = node.left.size if node.left else 0
            right_size = node.right.size if node.right else 0
            node.size = 1 + left_size + right_size
            node = node.parent

    def balance_factor(self, node: 'Node') -> int:
        return (node.right.height if node.right else 0) - (node.left.height if node.left else 0)

    def balance(self, node: 'Node') -> 'Node':
        ret = node
        if self.balance_factor(node) >= 2:
            if self.balance_factor(node.right) < 0:
                self.rotateright(node.right)
            ret = self.rotateleft(node)
            while self.balance_factor(node) >= 2:
                if self.balance_factor(node.right) < 0:
                    self.rotateright(node.right)
                self.rotateleft(node)
        if self.balance_factor(node) <= -2:
            if self.balance_factor(node.left) > 0:
                self.rotateleft(node.left)
            ret = self.rotateright(node)
            while self.balance_factor(node) <= -2:
                if self.balance_factor(node.left) > 0:
                    self.rotateleft(node.left)
                self.rotateright(node)
        return ret

    def rotateright(self, p: 'Node') -> 'Node':
        q = p.left
        p.left = q.right
        if q.right:
            q.right.parent = p
        q.right = p
        q.parent = p.parent
        p.parent = q
        if q.parent:
            if q.parent.left == p:
                q.parent.left = q
            else:
                q.parent.right = q
        p.update_heights()
        return q

    def rotateleft(self, q: 'Node') -> 'Node':
        p = q.right
        q.right = p.left
        if p.left:
            p.left.parent = q
        p.left = q
        p.parent = q.parent
        q.parent = p
        if p.parent:
            if p.parent.left == q:
                p.parent.left = p
            else:
                p.parent.right = p
        q.update_heights()
        return p


class Tree:
    def __init__(self, node: 'Node' = None):
        self.root = node

    def __str__(self):
        return self.root.__str__() if self.root else 'None'

    def __getitem__(self, i: int) -> Optional['Node']:
        if not self.root:
            return None
        node = self.root
        pos = node.size - (node.right.size if node.right else 0) - 1
        if i == pos:
            return node
        elif i < pos:
            return node.left[i] if node.left else None
        else:
            return node.right[i - (node.left.size + 1 if node.left else 1)] if node.right else None

    def inorder(self):
        if not self.root:
            return
        node = self.root
        stack = []
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                yield node.key
                node = node.right

    def delete(self, i: int, node: 'Node' = None):
        if not node:
            node = self[i] if self.root else None
        if not node:
            return
        self.root = self.root.delete(node)

    def merge(self, other: 'Tree'):
        if not self.root or not other.root:
            if not self.root:
                self.root = other.root
            return
        if self.root.height >= other.root.height:
            max_node = self.max()
            self.delete(0, node=max_node)
            gamma = self.root
            while gamma and gamma.right and gamma.height - other.root.height > 1:
                gamma = gamma.right
            if gamma == self.root:
                t = Node(max_node.key)
                t.left = self.root
                if self.root:
                    self.root.parent = t
                t.right = other.root
                other.root.parent = t
            else:
                t = Node(max_node.key, gamma)
                t.left = gamma.right
                if gamma.right:
                    gamma.right.parent = t
                t.right = other.root
                other.root.parent = t
                gamma.right = t
        else:
            min_node = other.min()
            other.delete(0, node=min_node)
            gamma = other.root
            while gamma and gamma.left and gamma.height - self.root.height > 1:
                gamma = gamma.left
            t = Node(min_node.key, gamma)
            t.right = gamma.left
            if gamma.left:
                gamma.left.parent = t
            t.left = self.root
            self.root.parent = t
            gamma.left = t

        t.update_heights()
        node = t
        ret = node
        while node:
            node = node.balance(node)
            ret = node
            node = node.parent
        self.root = ret

    def split(self, tree: 'Tree', i: int) -> ('Tree', 'Tree'):
        if not tree.root:
            return tree, Tree()
        pos = tree.root.size - (tree.root.right.size if tree.root.right else 0) - 1
        if i < pos:
            tree1 = Tree()
            tree1.root = tree.root.left
            if tree1.root:
                tree1.root.parent = None
            tree2 = Tree()
            tree2.root = tree.root.right
            if tree2.root:
                tree2.root.parent = None
            v1, v2 = tree.split(tree1, i)

            t = tree.root
            t.left = v2.root
            if v2.root:
                v2.root.parent = t
            t.right = tree2.root
            if tree2.root:
                tree2.root.parent = t
            t.update_heights()
            v2.root = t.balance(t)
            if v2.root:
                v2.root.parent = None

            return v1, v2
        else:
            tree1 = Tree()
            tree1.root = tree.root.left
            if tree1.root:
                tree1.root.parent = None
            tree2 = Tree()
            tree2.root = tree.root.right
            if tree2.root:
                tree2.root.parent = None
            v1, v2 = tree.split(tree2, i - (tree.root.left.size + 1 if tree.root.left else 1))

            t = tree.root
            t.left = tree1.root
            if tree1.root:
                tree1.root.parent = t
            t.right = v1.root
            if v1.root:
                v1.root.parent = t
            t.update_heights()
            tree1.root = t.balance(t)
            if tree1.root:
                tree1.root.parent = None

            return tree1, v2

    def min(self) -> Optional['Node']:
        if not self.root:
            return None
        node = self.root
        while node.left:
            node = node.left
        return node

    def max(self) -> Optional['Node']:
        if not self.root:
            return None
        node = self.root
        while node.right:
            node = node.right
        return node


def main():
    # s = input()
    lst = []
    l = 300000
    for i in range(l):
        lst.append(random.choice('abcdefghijklmnopqrstuvwxyz'))
    s = ''.join(lst)
    tree = Tree(Node(s[0]))
    t1 = time.perf_counter_ns()
    for c in s:
        tree1 = Tree(Node(c))
        tree.merge(tree1)
    t2 = time.perf_counter_ns()
    print('make tree, ns:', t2 - t1)

    # n = int(input())
    n = 100000
    Command = namedtuple('Command', 'i j k')
    # commands = (Command(*map(int, input().split())) for _ in range(n))
    commands = (Command(0, 0, 1) for _ in range(n))
    t1 = time.perf_counter_ns()
    for command in commands:
        tree, tree3 = tree.split(tree, command.i - 1)
        part, tree3 = tree3.split(tree3, command.j - command.i)
        tree.merge(tree3)
        tree, tree3 = tree.split(tree, command.k - 1)
        tree.merge(part)
        tree.merge(tree3)
    t2 = time.perf_counter_ns()
    print('commands , ns:', t2 - t1)
    # print(''.join(tree.inorder()))


if __name__ == '__main__':
    main()
