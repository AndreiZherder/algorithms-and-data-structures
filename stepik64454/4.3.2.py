from collections import deque
from sys import stdin, stdout
from types import GeneratorType


def input():
    return stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    stdout.write(sep.join(map(str, args)))
    stdout.write(end)


def solution():
    def bfs(start: int) -> int:
        seen = [False for i in range(n)]
        q = deque([(start, 0)])
        seen[start] = True
        ans = 0
        while q:
            v, dist = q.popleft()
            ans += dist
            for u in g[v]:
                if not seen[u]:
                    seen[u] = True
                    q.append((u, dist + 1))
        return ans
    n, m = (int(num) for num in input().split())
    g = [[] for i in range(n)]
    for i in range(m):
        v, u = (int(num) for num in input().split())
        v -= 1
        u -= 1
        g[v].append(u)
        g[u].append(v)
    print(sum(bfs(v) for v in range(n)) // 2)


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
