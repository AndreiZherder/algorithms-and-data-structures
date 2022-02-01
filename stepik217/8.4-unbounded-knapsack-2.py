"""
Даны:
номиналы монет: w
вместимость рюкзака: capacity
монеты можно брать неограниченное число раз
Найти минимальное количество монет, которые мождно поместить в рюкзак и их индексы в списке w
"""
from typing import List


def unbounded_knapsack(w: List[int], capacity: int) -> (int, List[int]):
    n = len(w)
    dp = [1000 for i in range(capacity + 1)]
    dp[0] = 0
    prev = [-1 for i in range(capacity + 1)]
    for i in range(1, capacity + 1):
        m = dp[i]
        for j in range(n):
            if w[j] <= i and dp[i - w[j]] + 1 < m:
                m = dp[i - w[j]] + 1
                prev[i] = j
            dp[i] = m
    ans = []
    i = capacity
    while i > 0:
        ans.append(prev[i])
        i -= w[prev[i]]
    return dp[capacity], ans


def main():
    w = [1, 5, 10, 25, 21]
    capacity = 63
    m, ans = unbounded_knapsack(w, capacity)
    print(f'm = {m}')
    print('indexes:', end=' ')
    for j in ans:
        print(j, end=' ')
    print('\nitems:', end=' ')
    for j in ans:
        print(w[j], end=' ')


if __name__ == '__main__':
    main()
