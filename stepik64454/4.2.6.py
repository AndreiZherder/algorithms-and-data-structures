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
    def dfs(v: int, par: int) -> bool:
        for u in g[v]:
            if u in seen:
                if u != par:
                    yield True
            else:
                seen.add(u)
                cur = yield dfs(u, v)
                if cur:
                    yield True
        yield False

    n, m = (int(num) for num in input().split())
    g = defaultdict(list)
    for i in range(m):
        v, u = (int(num) for num in input().split())
        g[v].append(u)
        g[u].append(v)
    seen = set()
    ans = False
    for i in range(n):
        if i not in seen:
            seen.add(i)
            ans |= dfs(i, -1)
    print('YES' if ans else "NO")


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
