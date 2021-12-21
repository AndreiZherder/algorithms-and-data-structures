"""
Найти длину максимальной возрастающей последовательности и одну из таких последовательностей.
"""
from typing import List


def longest_increasing_subsequence(a: List[int]) -> (int, List[int]):
    n = len(a)
    if n == 0:
        return 0, []
    f = [0 for _ in range(n)]
    prev = [-1 for _ in range(n)]
    for i in range(n):
        m = 0
        for j in range(i):
            if a[j] < a[i] and f[j] > m:
                m = f[j]
                prev[i] = j
        f[i] = 1 + m

    m = 0
    m_pos = 0
    for i, num in enumerate(f):
        if num > m:
            m = num
            m_pos = i
    i = m_pos
    seq = [a[i]]
    while prev[i] != -1:
        i = prev[i]
        seq.append(a[i])
    return m, *reversed(seq)


def main():
    a = [7, 2, 1, 3, 8, 4, 9, 1, 2, 6, 5, 9, 3, 8, 1]
    length, *seq = longest_increasing_subsequence(a)
    print(length)
    print(*seq)


if __name__ == '__main__':
    main()
