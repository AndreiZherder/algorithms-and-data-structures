from collections import defaultdict
from sys import stdin, stdout


def input():
    return stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    stdout.write(sep.join(map(str, args)))
    stdout.write(end)


def solution():
    n = int(input())
    g = defaultdict(list)
    m = 0
    for i in range(n):
        row = input()
        for j in range(i + 1, n):
            if row[j] == '1':
                g[i + 1].append(j + 1)
                m += 1
    print(m)
    for i in range(1, n + 1):
        if i in g:
            for j in g[i]:
                print(i, j)


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
