"""
По данным n отрезкам необходимо найти множество точек минимального размера,
для которого каждый из отрезков содержит хотя бы одну из точек.

В первой строке дано число 1≤n≤100 отрезков. Каждая из последующих n строк содержит по два числа 0≤l≤r≤10^9,
задающих начало и конец отрезка.
Выведите оптимальное число m точек и сами m точек. Если таких множеств точек несколько, выведите любое из них.

Sample Input 1:

3
1 3
3 6
2 5
Sample Output 1:

1
3
Sample Input 2:

4
4 7
1 3
2 5
5 6
Sample Output 2:

2
3 6
"""
import collections


def main():
    Section = collections.namedtuple('Section', ['left', 'right'])
    n = int(input())
    sections = sorted([Section(*map(int, input().split())) for _ in range(n)], key=lambda x: x.right)
    right = sections[0].right
    ans = [right]
    for section in sections:
        if section.left > right:
            right = section.right
            ans.append(right)
    print(len(ans))
    print(*ans)


if __name__ == '__main__':
    main()
