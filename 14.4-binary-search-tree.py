"""
Реализуйте структуру данных для хранения множества целых чисел,
поддерживающую запросы добавления, удаления, поиска, а также
суммы на отрезке. На вход в данной задаче будет дана последова-
тельность таких запросов. Чтобы гарантировать, что ваша программа
обрабатывает каждый запрос по мере поступления (то есть онлайн),
каждый запрос будет зависеть от результата выполнения одного из
предыдущих запросов. Если бы такой зависимости не было, задачу
можно было бы решить оффлайн: сначала прочитать весь вход и со-
хранить все запросы в каком-нибудь виде, а потом прочитать вход
еще раз, параллельно отвечая на запросы.
Формат входа. Изначально множество пусто. Первая строка содер-
жит число запросов n. Каждая из n следующих строк содержит
запрос в одном из следующих четырех форматов:
+ i: добавить число f(i) в множество (если оно уже есть,
проигнорировать запрос);
- i: удалить число f(i) из множества (если его нет, про-
игнорировать запрос);
? i: проверить принадлежность числа f(i) множеству;
s l r: посчитать сумму всех элементов множества, попа-
дающих в отрезок [f(l); f(r)].
Функция f определяется следующим образом. Пусть s—резуль-
тат последнего запроса суммы на отрезке (если таких запросов
еще не было, то s = 0). Тогда
f(x) = (x + s) mod 1 000 000 001 :

Формат выхода. Для каждого запроса типа ? i выведите «Found»
или «Not found». Для каждого запроса суммы выведите сумму
всех элементов множества, попадающих в отрезок [f(l); f(r)]. Га-
рантируется, что во всех тестах f(l) <= f(r).
Ограничения. 1 <= n <= 105; 0 <= i <= 10^9.

Пример.
Вход:
15
? 1
+ 1
? 1
+ 2
s 1 2
+ 1000000000
? 1000000000
- 1000000000
? 1000000000
s 999999999 1000000000
- 2
? 2
- 0
+ 9
s 0 9
Выход:
Not found
Found
3
Found
Not found
1
Not found
10
Для первых пяти запросов s = 0, для следующих пяти — s = 3,
для следующих пяти — s = 1. Заданные запросы разворачива-
ются в следующие: find(1), add(1), find(1), add(2), sum(1; 2) ! 3,
add(2), find(2)!Found, del(2), find(2)!Not found, sum(1; 2)!1,
del(3), find(3)!Not found, del(1), add(10), sum(1; 10)!10. Добав-
ление элемента дважды не изменяет множество, как и попытки
удалить элемент, которого в множестве нет.

Пример.
Вход:
5
? 0
+ 0
? 0
- 0
? 0
Выход:
Not found
Found
Not found
Пример.
Вход:
5
+ 491572259
? 491572259
? 899375874
s 310971296 877523306
+ 352411209
Выход:
Found
Not found
491572259
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

    def upperbond(self, key: int) -> Optional['Node']:
        if key == self.key:
            return self
        if key < self.key:
            if self.left:
                return self.left.upperbond(key)
            else:
                return self
        else:
            if self.right:
                return self.right.upperbond(key)
            else:
                return self.next_node()

    def lowerbond(self, key: int) -> Optional['Node']:
        if key == self.key:
            return self
        if key < self.key:
            if self.left:
                return self.left.lowerbond(key)
            else:
                return self.prev_node()
        else:
            if self.right:
                return self.right.lowerbond(key)
            else:
                return self

    def update_heights(self):
        node = self
        while node:
            left_height = node.left.height if node.left else 0
            right_height = node.right.height if node.right else 0
            node.height = (1 + max(left_height, right_height)) if (node.left or node.right) else 0
            node = node.parent

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
        self.root = self.root.delete(node)

    def upperbond(self, key) -> Optional['Node']:
        return self.root.upperbond(key) if self.root else None

    def lowerbond(self, key) -> Optional['Node']:
        return self.root.lowerbond(key) if self.root else None

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


def f(x: int, s: int) -> int:
    return (x + s) % 1000000001


def main():
    s = 0
    tree = Tree()
    n = int(input())
    for _ in range(n):
        cmd = input().split()
        if cmd[0] == '?':
            print('Found' if tree.find(f(int(cmd[1]), s)) else 'Not found')
        elif cmd[0] == '+':
            tree.insert(int(f(int(cmd[1]), s)))
        elif cmd[0] == '-':
            tree.delete(int(f(int(cmd[1]), s)))
        elif cmd[0] == 's':
            l = f(int(cmd[1]), s)
            r = f(int(cmd[2]), s)
            if l > r:
                s = 0
            else:
                node = tree.upperbond(l)
                last_node = tree.lowerbond(r)
                s = 0
                if node and last_node:
                    while node and node.key <= last_node.key:
                        s += node.key
                        node = node.next_node()
            print(s)


if __name__ == '__main__':
    main()
