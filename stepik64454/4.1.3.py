from collections import defaultdict
from sys import stdin, stdout


def input():
    return stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    stdout.write(sep.join(map(str, args)))
    stdout.write(end)


def solution():
    n, m = (int(num) for num in input().split())
    g = defaultdict(set)
    for i in range(m):
        i, j = (int(num) for num in input().split())
        g[i].add(j)
        g[j].add(i)
    for i in range(n):
        for j in range(n):
            if j + 1 in g[i + 1]:
                print(1, end='')
            else:
                print(0, end='')
        print()


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
