from collections import deque
from sys import stdin, stdout
from types import GeneratorType


def input():
    return stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    stdout.write(sep.join(map(str, args)))
    stdout.write(end)


def solution():
    n, m = (int(num) for num in input().split())
    g = [[] for i in range(n)]
    seen = [False for i in range(n)]
    for i in range(m):
        v, u = (int(num) for num in input().split())
        v -= 1
        u -= 1
        g[v].append(u)
        g[u].append(v)
    start = int(input()) - 1
    q = deque([start])
    seen[start] = True
    ans = []
    while q:
        v = q.popleft()
        ans.append(v + 1)
        for u in g[v]:
            if not seen[u]:
                seen[u] = True
                q.append(u)
    print(*ans)


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
