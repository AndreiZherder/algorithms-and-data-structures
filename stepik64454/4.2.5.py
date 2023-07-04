from collections import defaultdict, Counter
from functools import lru_cache
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
    def build_tree(v: int):
        for u in tree[v]:
            if u not in seen:
                seen.add(u)
                parent[u] = v
                yield build_tree(u)
        yield

    @bootstrap
    def is_ancestor(v: int, a: int) -> bool:
        if (v, a) in cache:
            yield cache[(v, a)]
        if v == -1:
            ans = False
        elif v == a:
            ans = True
        else:
            ans = yield is_ancestor(parent[v], a)
        cache[(v, a)] = ans
        yield ans

    n, m = (int(num) for num in input().split())
    if m < n - 1:
        print('NO')
        return
    edges = []
    for i in range(m):
        edges.append(tuple(int(num) - 1 for num in input().split()))
    q = int(input())
    if q != n - 1:
        print('NO')
        return
    if q == m:
        print('YES')
        return
    spanning_edges = [edges[int(num) - 1] for num in input().split()]
    tree = defaultdict(list)
    cnt = Counter()
    for v, u in spanning_edges:
        cnt[v] += 1
        cnt[u] += 1
        tree[v].append(u)
        tree[u].append(v)
    root = min(cnt, key=cnt.get)

    parent = [-1 for i in range(n)]
    seen = {root}
    build_tree(root)

    cache = dict()
    for v, u in edges:
        if not is_ancestor(u, v) and not is_ancestor(v, u):
            print('NO')
            return
    print('YES')


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
