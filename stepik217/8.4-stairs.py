"""
Даны число 1≤n≤10^2 ступенек лестницы и целые числа −10^4≤a1,…,an≤10^4, которыми помечены ступеньки.
Найдите максимальную сумму, которую можно получить, идя по лестнице снизу вверх (от нулевой до n-й ступеньки),
каждый раз поднимаясь на одну или две ступеньки.

Sample Input 1:

2
1 2
Sample Output 1:

3
Sample Input 2:

2
2 -1
Sample Output 2:

1
Sample Input 3:

3
-1 2 1
Sample Output 3:

3
"""
from typing import List


def stairs(a: List[int], n: int) -> int:
    if n <= 2:
        return sum(a)
    a0, a1 = a[0], a[0] + a[1]
    ans = 0
    for i in range(2, n):
        ans = max(a0, a1) + a[i]
        a0, a1 = a1, ans
    return ans


def main():
    n = 1 + int(input())
    a = [0] + [int(num) for num in input().split()]
    print(stairs(a, n))


if __name__ == '__main__':
    main()
