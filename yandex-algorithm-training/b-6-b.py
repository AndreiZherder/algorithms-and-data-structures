"""
Требуется определить в заданном массиве номер самого левого и самого правого элемента, равного искомому числу.

Формат ввода
В первой строке вводится одно натуральное число N, не превосходящее 10^5: количество чисел в массиве.
Во второй строке вводятся N натуральных чисел, не превосходящих 10^9, каждое следующее не меньше предыдущего.
В третьей строке вводится количество искомых чисел M – натуральное число, не превосходящее 10^6.
В четвертой строке вводится M натуральных чисел, не превосходящих 10^9.

Формат вывода
Для каждого запроса выведите в отдельной строке через пробел два числа:
номер элемента самого левого и самого правого элементов массива, равных числу-запросу.
Элементы массива нумеруются с единицы.Если в массиве нет такого числа,
выведите в соответствующей строке два нуля, разделенных пробелом.
"""
from bisect import bisect_right, bisect_left
from typing import List, Tuple


def solution(nums: List[int], queries: List[int]) -> List[Tuple[int, int]]:
    ans = []
    for query in queries:
        left = bisect_left(nums, query)
        if left == len(nums) or nums[left] != query:
            left = 0
        else:
            left += 1
        right = bisect_right(nums, query) - 1
        if nums[right] != query:
            right = 0
        else:
            right += 1
        ans.append((left, right))
    return ans


def main():
    n = int(input())
    nums = [int(num) for num in input().split()]
    m = int(input())
    queries = [int(query) for query in input().split()]
    for left, right in solution(nums, queries):
        print(left, right)


if __name__ == '__main__':
    main()
