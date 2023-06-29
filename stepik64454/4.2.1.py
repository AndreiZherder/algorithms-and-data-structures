from collections import defaultdict
from sys import stdin, stdout


def input():
    return stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    stdout.write(sep.join(map(str, args)))
    stdout.write(end)


def solution():
    def dfs(v: int):
        ans.append(v)
        for u in g[v]:
            if u not in seen:
                seen.add(u)
                dfs(u)
                ans.append(v)

    n, m = (int(num) for num in input().split())
    g = defaultdict(list)
    for i in range(m):
        v, u = (int(num) for num in input().split())
        g[v].append(u)
        g[u].append(v)
    v = int(input())
    ans = []
    seen = {v}
    dfs(v)
    print(len(ans))
    print(*ans)


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
