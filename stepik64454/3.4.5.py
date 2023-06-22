from sys import stdin, stdout


def input():
    return stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    stdout.write(sep.join(map(str, args)))
    stdout.write(end)


def solution():
    n, m = [int(num) for num in input().split()]
    a = [[int(num) for num in input().split()] for i in range(n)]
    prev = [[0 for j in range(m)] for i in range(n)]
    row = [[10 ** 20, 0, 0] for i in range(n)]
    col = [[10 ** 20, 0, 0] for i in range(m)]
    row[0] = [a[0][0], 0, 0]
    col[0] = [a[0][0], 0, 0]
    cur = a[0][0]
    for j in range(1, m):
        mn = row[0][0]
        mini = row[0][1]
        minj = row[0][2]
        cur = mn + a[0][j]
        prev[0][j] = (mini, minj)
        if cur < mn:
            row[0][0] = cur
            row[0][1] = 0
            row[0][2] = j
        col[j][0] = cur
        col[j][1] = 0
        col[j][2] = j
    for i in range(1, n):
        mn = col[0][0]
        mini = col[0][1]
        minj = col[0][2]
        cur = mn + a[i][0]
        prev[i][0] = (mini, minj)
        if cur < mn:
            col[0][0] = cur
            col[0][1] = i
            col[0][2] = 0
        row[i][0] = cur
        row[i][1] = i
        row[i][2] = 0

    for i in range(1, n):
        for j in range(1, m):
            if row[i][0] < col[j][0]:
                mn = row[i][0]
                mini = row[i][1]
                minj = row[i][2]
            else:
                mn = col[j][0]
                mini = col[j][1]
                minj = col[j][2]
            cur = mn + a[i][j]
            prev[i][j] = (mini, minj)
            if cur < row[i][0]:
                row[i][0] = cur
                row[i][1] = i
                row[i][2] = j
            if cur < col[j][0]:
                col[j][0] = cur
                col[j][1] = i
                col[j][2] = j
    path = [(n - 1, m - 1)]
    i, j = n - 1, m - 1
    while i != 0 or j != 0:
        i, j = prev[i][j]
        path.append((i, j))
    print(cur, len(path))
    for i, j in reversed(path):
        print(i + 1, j + 1)


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
