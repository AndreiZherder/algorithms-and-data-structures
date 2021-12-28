"""
Первая строка входа содержит целые числа 1≤W≤10^4 и 1≤n≤300 — вместимость рюкзака и число золотых слитков.
Следующая строка содержит n целых чисел 0≤w1,…,wn≤10^5, задающих веса слитков.
Найдите максимальный вес золота, который можно унести в рюкзаке.

Sample Input:

10 3
1 4 8
Sample Output:

9
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
    capacity, n = (int(num) for num in input().split())
    w = [int(num) for num in input().split()]
    c = w.copy()
    maxcost, ans = bounded_knapsack(w, c, capacity)
    print(maxcost)
    """
    print(f'maxcost = {maxcost}')
    print('indexes:', end=' ')
    for j in ans:
        print(j, end=' ')
    print('\nitems:', end=' ')
    for j in ans:
        print(w[j], end=' ')
    """


if __name__ == '__main__':
    main()
