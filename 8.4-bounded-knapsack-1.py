"""
Даны:
веса предметов: w
стоимости предметов: c
вместимость рюкзака: capacity
каждый предмет можно взять один раз
Найти максимальную стоимость предметов, которые мождно поместить в рюкзак и индексы этих предметов в списке w
"""
from typing import List


def bounded_knapsack(w: List[int], c: List[int], capacity: int) -> (int, List[int]):
    n = len(w)
    dp = [[0 for j in range(capacity + 1)] for i in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, capacity + 1):
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w[i - 1]] + c[i - 1] if w[i - 1] <= j else 0)
    ans = []
    i = n
    j = capacity
    while i > 0:
        if dp[i - 1][j] != dp[i][j]:
            ans.append(i - 1)
            j -= w[i - 1]
        i -= 1

    return dp[n][capacity], ans


def main():
    # w = [5, 7, 3, 2, 1, 10]
    # c = [4, 15, 5, 3, 2, 6]
    # w = [6, 3, 4, 2]
    # c = [30, 14, 16, 9]
    w = [7, 3, 1, 5, 4]
    c = [10, 4, 2, 6, 7]
    capacity = 12
    maxcost, ans = bounded_knapsack(w, c, capacity)
    print(f'maxcost = {maxcost}')
    print('indexes:', end=' ')
    for j in ans:
        print(j, end=' ')
    print('\nitems:', end=' ')
    for j in ans:
        print(w[j], end=' ')


if __name__ == '__main__':
    main()
