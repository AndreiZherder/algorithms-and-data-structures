"""
Первая строка входа содержит число операций 1≤n≤10^5.
Каждая из последующих nn строк задают операцию одного из следующих двух типов:
Insert x, где 0≤x≤10^9 — целое число;
ExtractMax
Первая операция добавляет число x в очередь с приоритетами, вторая — извлекает максимальное число и выводит его.
Sample Input:

6
Insert 200
Insert 10
ExtractMax
Insert 5
Insert 500
ExtractMax

Sample Output:

200
500
"""


class Heapq:
    def __init__(self):
        self.heap = []

    def __str__(self):
        return str(self.heap)

    def push(self, item):
        self.heap.append(item)
        self._siftup(len(self.heap) - 1)

    def pop(self):
        if self.heap:
            self.heap[0], self.heap[len(self.heap) - 1] = self.heap[len(self.heap) - 1], self.heap[0]
            item = self.heap.pop()
            self._siftdown(0)
            return item

    def _siftdown(self, i):
        max_child_i = self._get_max_child_i(i)
        while 2 * i + 1 < len(self.heap) and self.heap[i] < self.heap[max_child_i]:
            self.heap[i], self.heap[max_child_i] = self.heap[max_child_i], self.heap[i]
            i = max_child_i
            max_child_i = self._get_max_child_i(i)

    def _siftup(self, i):
        while i >= 1 and self.heap[i] > self.heap[(i - 1) // 2]:
            self.heap[(i - 1) // 2], self.heap[i] = self.heap[i], self.heap[(i - 1) // 2]
            i = (i - 1) // 2

    def _get_max_child_i(self, i):
        if (2 * i + 2) < len(self.heap):
            return 2 * i + 1 if self.heap[2 * i + 1] > self.heap[2 * i + 2] else 2 * i + 2
        else:
            return 2 * i + 1


def main():
    n = int(input())
    h = Heapq()
    for operation in (input().split() for _ in range(n)):
        if operation[0] == 'Insert':
            h.push(int(operation[1]))
        if operation[0] == 'ExtractMax':
            print(h.pop())


if __name__ == '__main__':
    main()