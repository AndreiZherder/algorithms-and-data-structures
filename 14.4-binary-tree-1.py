"""
"""
from typing import Optional


class Node:
    def __init__(self, key, parent=None):
        self.parent = parent
        self.height = parent.height + 1 if parent else 0
        self.key = key
        self.left = None
        self.right = None

    def __str__(self):
        ans = ''
        if self.left:
            ans += self.left.__str__()
        else:
            ans += '|'
        ans += str(self.key) + '(' + str(self.height) + ')' + ('' if not self.right else ' ')
        if self.right:
            ans += self.right.__str__()
        else:
            ans += '| '
        return ans

    def find(self, key):
        """
        return Optional[Node]
        """
        if self.key == key:
            return self
        elif key < self.key and self.left:
            return self.left.find(key)
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
                self.left = Node(key, self)
        elif self.right:
            self.right.insert(key)
        else:
            self.right = Node(key, self)


class BinaryTree:
    def __init__(self):
        self.root = None

    def __str__(self):
        return self.root.__str__()

    def find(self, key):
        return self.root.find(key) if self.root else None

    def insert(self, key):
        if self.root:
            self.root.insert(key)
        else:
            self.root = Node(key)


def main():
    # lst = [5, 3, 7, 4, 6]
    lst = [3, 1, 2, 4, 5]
    tree = BinaryTree()
    for key in lst:
        tree.insert(key)
    print(tree)


if __name__ == '__main__':
    main()
