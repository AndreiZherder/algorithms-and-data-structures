"""
По данному числу 1≤n≤10^9 найдите максимальное число k, для которого n можно представить как сумму k
различных натуральных слагаемых. Выведите в первой строке число k, во второй — k слагаемых.

Sample Input 1:

4
Sample Output 1:

2
1 3
Sample Input 2:

6
Sample Output 2:

3
1 2 3
"""


def main():
    n = int(input())
    a = 1
    ans = []
    while n - a > a:
        ans.append(a)
        n -= a
        a += 1
    ans.append(n)
    print(len(ans))
    print(*ans)


if __name__ == '__main__':
    main()
