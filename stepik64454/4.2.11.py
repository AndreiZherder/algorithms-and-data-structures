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
    def dfs(v: int) -> bool:
        if g[v]:
            seen = False
            for u in g[v]:
                indegree[u] -= 1
                if indegree[u] == 0:
                    root = u
                    if seen:
                        yield False
                    seen = True
            if not (yield dfs(root)):
                yield False
        yield True

    n, m = (int(num) for num in input().split())
    g = [[] for i in range(n)]
    indegree = [0 for i in range(n)]
    for i in range(m):
        v, u = (int(num) for num in input().split())
        v -= 1
        u -= 1
        g[u].append(v)
        indegree[v] += 1
    seen = False
    for v in range(n):
        if indegree[v] == 0:
            root = v
            if seen:
                print('NO')
                return
            seen = True
    if dfs(root):
        print('YES')
    else:
        print('NO')





def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
