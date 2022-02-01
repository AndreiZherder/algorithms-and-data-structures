"""
Вычислите расстояние редактирования двух данных непустых строк длины не более 10^2,
содержащих строчные буквы латинского алфавита.

Sample Input 1:

ab
ab
Sample Output 1:

0
Sample Input 2:

short
ports
Sample Output 2:

3
"""


def levenshtein_distance(a: str, b: str) -> int:
    n = len(a) + 1
    m = len(b) + 1
    d = [[0 for j in range(m)] for i in range(n)]
    for i in range(n):
        d[i][0] = i
    for j in range(m):
        d[0][j] = j
    for i in range(1, n):
        for j in range(1, m):
            d[i][j] = min(d[i][j - 1] + 1,
                          d[i - 1][j] + 1,
                          d[i - 1][j - 1] + (0 if a[i - 1] == b[j - 1] else 1))
    return d[-1][-1]


def main():
    a, b = input(), input()
    print(levenshtein_distance(a, b))


if __name__ == '__main__':
    main()
