"""
Даны:
веса предметов: w
стоимости предметов: c
вместимость рюкзака: capacity
предметы можно брать неограниченное число раз
Найти максимальную стоимость предметов, которые мождно поместить в рюкзак и индексы этих предметов в списке w
"""
from typing import List


def unbounded_knapsack(w: List[int], c: List[int], capacity: int) -> (int, List[int]):
    n = len(w)
    dp = [0 for i in range(capacity + 1)]
    prev = [-1 for i in range(capacity + 1)]
    for i in range(1, capacity + 1):
        m = dp[i]
        for j in range(n):
            if w[j] <= i and dp[i - w[j]] + c[j] > m:
                m = dp[i - w[j]] + c[j]
                prev[i] = j
            dp[i] = m
    ans = []
    i = capacity
    while i > 0:
        ans.append(prev[i])
        i -= w[prev[i]]
    return dp[capacity], ans


def main():
    # w = [5, 7, 3, 2, 1, 10]
    # c = [4, 15, 5, 3, 2, 6]
    w = [6, 3, 4, 2]
    c = [30, 14, 16, 9]
    capacity = 10
    maxcost, ans = unbounded_knapsack(w, c, capacity)
    print(f'maxcost = {maxcost}')
    print('indexes:', end=' ')
    for j in ans:
        print(j, end=' ')
    print('\nitems:', end=' ')
    for j in ans:
        print(w[j], end=' ')


if __name__ == '__main__':
    main()
