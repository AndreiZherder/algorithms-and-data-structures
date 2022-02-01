"""
У вас есть примитивный калькулятор, который умеет выполнять всего три операции с текущим числом x:
заменить x на 2x, 3x или x+1. По данному целому числу 1≤n≤10^5 определите минимальное число операций k, необходимое,
чтобы получить n из 1. Выведите k и последовательность промежуточных чисел.

Sample Input 1:

1
Sample Output 1:

0
1
Sample Input 2:

5
Sample Output 2:

3
1 2 4 5
Sample Input 3:

96234
Sample Output 3:

14
1 3 9 10 11 22 66 198 594 1782 5346 16038 16039 32078 96234
"""
from typing import List


def calc(x: int) -> (int, List[int]):
    inf = 10 ** 5 + 1
    dp = [inf for _ in range(x + 1)]
    prev = [-1 for _ in range(x + 1)]
    dp[0] = 0
    dp[1] = 0
    for i in range(2, x + 1):
        a = (dp[i // 2] + 1 if i % 2 == 0 else inf, i // 2)
        b = (dp[i // 3] + 1 if i % 3 == 0 else inf, i // 3)
        c = (dp[i - 1] + 1, i - 1)
        m = min(a, b, c)
        dp[i] = m[0]
        prev[i] = m[1]
    i = x
    seq = []
    while i >= 1:
        seq.append(i)
        i = prev[i]

    return dp[x], list(reversed(seq))


def main():
    x = int(input())
    k, seq = calc(x)
    print(k)
    print(*seq)


if __name__ == '__main__':
    main()
