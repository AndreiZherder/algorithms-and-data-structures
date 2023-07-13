from collections import deque
from sys import stdin, stdout


def input():
    return stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    stdout.write(sep.join(map(str, args)))
    stdout.write(end)


def solution():
    n, m, p, q, x1, y1, x2, y2 = [int(num) for num in input().split()]
    if x1 == x2 and y1 == y2:
        print(0)
        return
    steps = ((p, q), (-p, -q), (q, p), (-q, -p), (-p, q), (p, -q), (-q, p), (q, -p))
    seen = {(x1, y1)}
    q = deque([(x1, y1, 0)])
    while q:
        x, y, depth = q.popleft()
        for dx, dy in steps:
            nx = x + dx
            ny = y + dy
            if 1 <= nx <= n and 1 <= ny <= m and (nx, ny) not in seen:
                if nx == x2 and ny == y2:
                    print(depth + 1)
                    return
                seen.add((nx, ny))
                q.append((nx, ny, depth + 1))
    print(-1)


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
