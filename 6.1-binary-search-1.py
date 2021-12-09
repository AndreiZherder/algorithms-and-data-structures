"""
В первой строке даны целое число 1≤n≤10^5 и массив A[1…n] из n различных натуральных чисел, не превышающих 10^9,
в порядке возрастания,
во второй — целое число 1≤k≤10^5 и k натуральных чисел b1,..., bk, не превышающих 10^9.
Для каждого i от 1 до k необходимо вывести индекс 1≤j≤n, для которого A[j]=bi, или -1, если такого j нет.
Sample Input:

5 1 5 8 12 13
5 8 1 23 1 11
Sample Output:

3 1 -1 1 -1
"""
from typing import List


def index(a: List[int], num: int) -> int:
    left = 0
    right = len(a) - 1
    while left <= right:
        middle = (left + right) // 2
        if num == a[middle]:
            return middle
        elif num < a[middle]:
            right = middle - 1
        else:
            left = middle + 1
    return -2


def main():
    n, *a = (int(j) for j in input().split())
    k, *b = (int(j) for j in input().split())
    print(*(index(a, b[i]) + 1 for i in range(k)))


if __name__ == '__main__':
    main()
