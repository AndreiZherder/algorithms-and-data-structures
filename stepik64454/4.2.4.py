from collections import defaultdict
from sys import stdin, stdout


def input():
    return stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    stdout.write(sep.join(map(str, args)))
    stdout.write(end)


def solution():
    def dfs(v: int):
        for u, i in g[v]:
            if u not in seen:
                seen.add(u)
                ans.append(i + 1)
                dfs(u)

    n, m = (int(num) for num in input().split())
    g = defaultdict(list)
    for i in range(m):
        v, u = (int(num) for num in input().split())
        g[v].append((u, i))
        g[u].append((v, i))
    seen = {1}
    ans = []
    dfs(1)
    print(n - 1)
    print(*ans)


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
