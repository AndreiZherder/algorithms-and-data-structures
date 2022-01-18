"""
"""
from typing import Optional


class BinaryTree:
    def __init__(self, key: int, parent: 'BinaryTree' = None):
        self.parent = parent
        self.key = key
        self.left = None
        self.right = None
        self.height = 0

    def __str__(self):
        lines, *_ = self.display_aux()
        return '\n'.join(lines)

    def display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = f"{self.key}({self.height})"
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left.display_aux()
            s = f"{self.key}({self.height})"
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right.display_aux()
            s = f"{self.key}({self.height})"
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left.display_aux()
        right, m, q, y = self.right.display_aux()
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

    def find(self, key: int) -> Optional['BinaryTree']:
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

    def insert(self, key):
        if self.key == key:
            return
        elif key < self.key:
            if self.left:
                self.left.insert(key)
            else:
                self.left = BinaryTree(key, self)
                self.update_parents_heights(self.left)
        elif self.right:
            self.right.insert(key)
        else:
            self.right = BinaryTree(key, self)
            self.update_parents_heights(self.right)

    def update_parents_heights(self, node: 'BinaryTree'):
        while node.parent:
            left_height = node.parent.left.height if node.parent.left else 0
            right_height = node.parent.right.height if node.parent.right else 0
            node.parent.height = (1 + max(left_height, right_height)) if (node.parent.left or node.parent.right) else 0
            node = node.parent


def main():
    tree = BinaryTree(5)
    for key in [1, 7, 6, 3, 4, 8, 2]:
        tree.insert(key)
    print(tree)


if __name__ == '__main__':
    main()
