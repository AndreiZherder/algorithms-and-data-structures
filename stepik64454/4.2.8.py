from sys import stdin, stdout
from types import GeneratorType


def input():
    return stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    stdout.write(sep.join(map(str, args)))
    stdout.write(end)


def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        to = f(*args, **kwargs)
        while True:
            if type(to) is GeneratorType:
                stack.append(to)
                to = next(to)
            else:
                stack.pop()
                if not stack:
                    break
                to = stack[-1].send(to)
        return to
    return wrappedfunc


def solution():
    @bootstrap
    def dfs(v: int, par: int) -> bool:
        for u in g[v]:
            if u != par:
                if not seen[u]:
                    seen[u] = True
                    parent[u] = v
                    if (yield dfs(u, v)):
                        yield True
                else:
                    cur = v
                    while cur != u:
                        ans.append(cur + 1)
                        cur = parent[cur]
                    ans.append(cur + 1)
                    yield True
        yield False

    n, m = (int(num) for num in input().split())
    g = [[] for i in range(n)]
    seen = [False for i in range(n)]
    parent = [-1 for i in range(n)]
    for i in range(m):
        v, u = (int(num) for num in input().split())
        if v == u:
            print('YES')
            print(1)
            print(v)
            return
        v -= 1
        u -= 1
        g[v].append(u)
        g[u].append(v)
    ans = []
    for v in range(n):
        if not seen[v]:
            seen[v] = True
            if dfs(v, -1):
                print('YES')
                print(len(ans))
                print(*reversed(ans))
                return
    print('NO')


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
