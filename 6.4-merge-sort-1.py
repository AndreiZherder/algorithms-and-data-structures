"""
Первая строка содержит число 1≤n≤10^5,
вторая — массив [1…n], содержащий натуральные числа, не превосходящие 10^9.
Необходимо посчитать число пар индексов 1≤i<j≤n, для которых A[i]>A[j].
(Такая пара элементов называется инверсией массива.
Количество инверсий в массиве является в некотором смысле его мерой неупорядоченности:
например, в упорядоченном по неубыванию массиве инверсий нет вообще,
а в массиве, упорядоченном по убыванию, инверсию образуют каждые два элемента.)
5
2 3 9 2 9
Sample Output:

2
"""
from collections import deque
from typing import List


def merge(a: List[int], b: List[int], cnt: List[int]) -> List[int]:
    i, j = 0, 0
    c = []
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
            cnt[0] += len(a) - i
    if i == len(a):
        while j < len(b):
            c.append(b[j])
            j += 1
    else:
        while i < len(a):
            c.append(a[i])
            i += 1
    return c


def main():
    n = int(input())
    q = deque(([int(_)] for _ in input().split()))
    cnt = [0]
    while len(q) > 1:
        if len(q) % 2 == 1:
            q.append(merge(b=q.pop(), a=q.pop(), cnt=cnt))
        for i in range(len(q) // 2):
            q.append(merge(a=q.popleft(), b=q.popleft(), cnt=cnt))
    print(cnt[0])


if __name__ == '__main__':
    main()
