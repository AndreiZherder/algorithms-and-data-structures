from collections import deque
from sys import stdin, stdout


def input():
    return stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    stdout.write(sep.join(map(str, args)))
    stdout.write(end)


def solution():
    n, m = [int(num) for num in input().split()]
    grid = []
    for i in range(2 * n + 1):
        grid.append(input())
    n = 2 * n + 1
    m = 2 * m + 1
    d = set()
    for i in range(1, n, 2):
        for j in range(1, m, 2):
            if grid[i][j] == 'S':
                start = (i, j)
            if grid[i][j] == 'D':
                d.add((i, j))
    seen = [[0 for j in range(m)] for i in range(n)]
    seen[start[0]][start[1]] = 1
    q = deque([start])
    while q:
        i, j = q.popleft()
        if grid[i - 1][j] == '-':
            for ni in range(i + 2, n, 2):
                if grid[ni - 1][j] == '-':
                    break
                else:
                    if not seen[ni][j]:
                        if grid[ni][j] == 'D':
                            d.remove((ni, j))
                        seen[ni][j] = 1
                        if grid[ni][j - 1] == '|' or grid[ni][j + 1] == '|':
                            q.append((ni, j))
                    elif seen[ni][j] & 1:
                        break
                    else:
                        seen[ni][j] |= 1
        if grid[i + 1][j] == '-':
            for ni in range(i - 2, 0, -2):
                if grid[ni + 1][j] == '-':
                    break
                else:
                    if not seen[ni][j]:
                        if grid[ni][j] == 'D':
                            d.remove((ni, j))
                        seen[ni][j] = 1
                        if grid[ni][j - 1] == '|' or grid[ni][j + 1] == '|':
                            q.append((ni, j))
                    elif seen[ni][j] & 1:
                        break
                    else:
                        seen[ni][j] |= 1
        if grid[i][j - 1] == '|':
            for nj in range(j + 2, m, 2):
                if grid[i][nj - 1] == '|':
                    break
                else:
                    if not seen[i][nj]:
                        if grid[i][nj] == 'D':
                            d.remove((i, nj))
                        seen[i][nj] = 2
                        if grid[i - 1][nj] == '-' or grid[i + 1][nj] == '-':
                            q.append((i, nj))
                    elif seen[i][nj] & 2:
                        break
                    else:
                        seen[i][nj] |= 2
        if grid[i][j + 1] == '|':
            for nj in range(j - 2, 0, -2):
                if grid[i][nj + 1] == '|':
                    break
                else:
                    if not seen[i][nj]:
                        if grid[i][nj] == 'D':
                            d.remove((i, nj))
                        seen[i][nj] = 2
                        if grid[i - 1][nj] == '-' or grid[i + 1][nj] == '-':
                            q.append((i, nj))
                    elif seen[i][nj] & 2:
                        break
                    else:
                        seen[i][nj] |= 2
    for i, j in d:
        if isinstance(grid[i], str):
            grid[i] = list(grid[i])
        grid[i][j] = ' '
    print('\n'.join(''.join(row) for row in grid))


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
