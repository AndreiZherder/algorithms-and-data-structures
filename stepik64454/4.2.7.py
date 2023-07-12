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
        for u in g[v]:
            if color[u] == WHITE:
                color[u] = GREY
                par[u] = v
                if (yield dfs(u)):
                    yield True
                color[u] = BLACK
            elif color[u] == GREY:
                if u == v:
                    ans.append(v + 1)
                else:
                    cur = v
                    while cur != u:
                        ans.append(cur + 1)
                        cur = par[cur]
                    ans.append(cur + 1)
                yield True
        yield False

    WHITE = 0
    GREY = 1
    BLACK = 2
    n, m = (int(num) for num in input().split())
    g = [[] for i in range(n)]
    color = [WHITE for i in range(n)]
    par = [-1 for i in range(n)]
    for i in range(m):
        v, u = (int(num) for num in input().split())
        v -= 1
        u -= 1
        g[v].append(u)
    ans = []
    for v in range(n):
        if color[v] == WHITE:
            color[v] = GREY
            if dfs(v):
                print('YES')
                print(len(ans))
                print(*reversed(ans))
                return
            color[v] = BLACK
    print('NO')


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
