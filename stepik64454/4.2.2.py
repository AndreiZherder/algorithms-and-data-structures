from collections import defaultdict
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
    def dfs(v: int):
        for u in g[v]:
            if u not in seen:
                seen.add(u)
                components[-1].append(u)
                yield dfs(u)
        yield

    n, m = (int(num) for num in input().split())
    g = defaultdict(list)
    for i in range(m):
        v, u = (int(num) for num in input().split())
        v -= 1
        u -= 1
        g[v].append(u)
        g[u].append(v)
    seen = set()
    cnt = 0
    components = []
    for v in range(n):
        if v not in seen:
            cnt += 1
            components.append([v])
            seen.add(v)
            dfs(v)
    ans = [0 for i in range(n)]
    for i, nodes in enumerate(sorted(components, key=min)):
        for v in nodes:
            ans[v] = i + 1
    print(cnt)
    print(*ans)


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
