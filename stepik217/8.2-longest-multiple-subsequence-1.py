"""
Дано целое число 1≤n≤10^3и массив A[1…n] натуральных чисел, не превосходящих 2⋅10^9.
Выведите максимальное 1≤k≤n, для которого найдётся подпоследовательность 1 ≤ i1 < i2 <…< ik ≤n длины k,
в которой каждый элемент делится на предыдущий.

Sample Input:

4
3 6 7 12
Sample Output:

3
"""
from typing import List


def longest_multiple_subsequence(a: List[int]) -> int:
    n = len(a)
    if n == 0:
        return 0
    f = [0 for _ in range(n)]
    f[0] = 1
    for i in range(1, n):
        m = 0
        for j in range(0, i):
            if a[i] % a[j] == 0 and f[j] > m:
                m = f[j]
        f[i] = 1 + m

    return max(f)


def main():
    n = int(input())
    a = [int(num) for num in input().split()]
    print(longest_multiple_subsequence(a))


if __name__ == '__main__':
    main()
