from collections import defaultdict
from sys import stdin, stdout


def input():
    return stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    stdout.write(sep.join(map(str, args)))
    stdout.write(end)


def solution():
    n, m = (int(num) for num in input().split())
    g = defaultdict(list)
    for i in range(m):
        i, j = (int(num) for num in input().split())
        g[i].append(j)
        g[j].append(i)
    for i in range(1, n + 1):
        print(len(g[i]), *sorted(g[i]))


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
