"""
Дано целое число 1≤n≤10^5 и массив A[1…n], содержащий неотрицательные целые числа, не превосходящие 10^9.
Найдите наибольшую невозрастающую подпоследовательность в A.
В первой строке выведите её длину k, во второй — её индексы 1<i<…<ik≤n.
Решите за O(n*log(n)).

Sample Input:

5
5 3 4 4 2
Sample Output:

4
1 3 4 5
"""
from typing import List


def reversed_bisect_right(a: List[int], num: int) -> int:
    left = 0
    right = len(a) - 1
    while left <= right:
        middle = left + (right - left) // 2
        if num <= a[middle]:
            left = middle + 1
        else:
            right = middle - 1
    return left


def longest_nonincreasing_subsequence(a: List[int]) -> (int, List[int]):
    n = len(a)
    if n <= 1:
        return n, list(a)
    inf = 10 ** 9 + 1

    # dp[i] -  the element at which a subsequence of length i terminates.
    # If there are multiple such sequences, then we take the one that ends in the biggest element.
    # dpi[i] - the index of element at which a subsequence of length i terminates.
    dp = [-inf for _ in range(n + 2)]
    dp[0] = inf
    dpi = [-1 for _ in range(n + 2)]
    # a:    5   3   4   4   2
    # i:    0   1   2   3   4
    # dp:   inf 5   4   4   2   -inf    -inf

    # prev[i] is the index of the previous element for the optimal subsequence ending in element i.
    previ = [-1 for _ in range(n + 2)]
    length = 1
    for i in range(n):
        pos = reversed_bisect_right(dp, a[i])
        dp[pos] = a[i]
        dpi[pos] = i
        previ[i] = dpi[pos - 1]
        if pos > length:
            length = pos
    seq = []
    i = dpi[length]
    for pos in range(length - 1, -1, -1):
        seq.append(i + 1)
        i = previ[i]
    return length, list(reversed(seq))


def main():
    n = int(input())
    a = [int(num) for num in input().split()]
    length, seq = longest_nonincreasing_subsequence(a)
    print(length)
    print(*seq)


if __name__ == '__main__':
    main()
