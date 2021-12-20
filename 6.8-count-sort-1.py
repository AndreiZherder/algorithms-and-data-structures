"""
Первая строка содержит число 1≤n≤10^4,
вторая — n натуральных чисел, не превышающих 10. Выведите упорядоченную по неубыванию последовательность этих чисел.

Sample Input:
5
2 3 9 2 9

Sample Output:
2 2 3 9 9
"""


def main():
    n = int(input())
    m = 10
    a = [0]
    a.extend([int(num) for num in input().split()])
    b = [0 for _ in range(m + 1)]
    ans = [0 for _ in range(n + 1)]
    for i in range(1, n + 1):
        b[a[i]] += 1
    for i in range(2, m + 1):
        b[i] += b[i - 1]
    for i in range(n, 0, -1):
        ans[b[a[i]]] = a[i]
        b[a[i]] -= 1
    for i in range(1, n + 1):
        print(ans[i], end=' ')


if __name__ == '__main__':
    main()
