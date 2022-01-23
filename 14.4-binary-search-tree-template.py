"""
"""
from typing import Optional


class Node:
    def __init__(self, key: int = None, parent: 'Node' = None):
        self.parent = parent
        self.key = key
        self.left: Optional['Node'] = None
        self.right: Optional['Node'] = None
        self.height = 0

    def __str__(self):
        lines, *_ = self.__display_aux()
        return '\n'.join(lines)

    def __display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if not self.right and not self.left:
            line = f"{self.key}({self.height})"
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if not self.right:
            lines, n, p, x = self.left.__display_aux()
            s = f"{self.key}({self.height})"
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if not self.left:
            lines, n, p, x = self.right.__display_aux()
            s = f"{self.key}({self.height})"
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left.__display_aux()
        right, m, q, y = self.right.__display_aux()
        s = f"{self.key}({self.height})"
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

    def update_heights(self):
        node = self
        while node:
            left_height = node.left.height if node.left else 0
            right_height = node.right.height if node.right else 0
            node.height = (1 + max(left_height, right_height)) if (node.left or node.right) else 0
            node = node.parent

    def find(self, key: int) -> Optional['Node']:
        if self.key == key:
            return self
        elif key < self.key:
            if self.left:
                return self.left.find(key)
            else:
                return None
        elif self.right:
            return self.right.find(key)
        else:
            return None

    def insert(self, key) -> 'Node':
        if self.key == key:
            return self
        elif key < self.key:
            if self.left:
                self.left.insert(key)
                return self.balance(self)
            else:
                self.left = Node(key, self)
                self.update_heights()
                return self
        elif self.right:
            self.right.insert(key)
            return self.balance(self)
        else:
            self.right = Node(key, self)
            self.update_heights()
            return self

    def balance_factor(self, node: 'Node') -> int:
        return (node.right.height if node.right else 0) - (node.left.height if node.left else 0)

    def balance(self, node: 'Node') -> 'Node':
        if self.balance_factor(node) == 2:
            if self.balance_factor(node.right) < 0:
                self.rotateright(node.right)
            return self.rotateleft(node)
        if self.balance_factor(node) == -2:
            if self.balance_factor(node.left) > 0:
                self.rotateleft(node.left)
            return self.rotateright(node)
        return node

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

    def rotateleft(self, q: 'Node')  -> 'Node':
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
    def __init__(self):
        self.root: Optional['Node'] = None

    def __str__(self):
        return self.root.__str__() if self.root else 'None'

    def find(self, key: int) -> Optional['Node']:
        return self.root.find(key) if self.root else None

    def insert(self, key):
        if self.root:
            self.root = self.root.insert(key)
        else:
            self.root = Node(key)

    def delete(self, key):
        node = self.root.find(key) if self.root else None
        if not node:
            return
        self.__delete_node(node)

    def __delete_node(self, node: Node):
        # no children
        if not node.left and not node.right:
            if node == self.root:
                self.root = None
                return
            if node.parent.left == node:
                node.parent.left = None
            else:
                node.parent.right = None
            node.parent.update_heights()
        # one child
        elif (node.left and not node.right) or (node.right and not node.left):
            child = node.left if node.left else node.right
            if node == self.root:
                self.root = child
                child.parent = None
            else:
                if node.parent.left == node:
                    node.parent.left = child
                else:
                    node.parent.right = child
                child.parent = node.parent
                node.parent.update_heights()
        # two children
        else:
            node2 = node.left
            while node2.right:
                node2 = node2.right
            node.key, node2.key = node2.key, node.key
            self.__delete_node(node2)

    def min(self) -> Optional[int]:
        if not self.root:
            return None
        node = self.root
        while node.left:
            node = node.left
        return node.key

    def max(self) -> Optional[int]:
        if not self.root:
            return None
        node = self.root
        while node.right:
            node = node.right
        return node.key


def main():
    tree = Tree()
    for key in range(11):
        tree.insert(key)
    print(tree)


if __name__ == '__main__':
    main()
