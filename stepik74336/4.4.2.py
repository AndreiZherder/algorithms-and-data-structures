import sys

input = lambda: sys.stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


def solution():
    def dfs(i: int) -> int:
        if 2 * i + 1 > m - 1:
            return tree[i]
        tree[i] = dfs(2 * i + 1) + dfs(2 * i + 2)
        return tree[i]

    n = int(input())
    a = [int(num) for num in input().split()]
    pos, b = [int(num) for num in input().split()]
    k = (n - 1).bit_length()
    m = (1 << (k + 1)) - 1
    tree = [0 for i in range(m)]
    tree[(1 << k) - 1:(1 << k) - 1 + n] = a
    dfs(0)
    print(*tree, end=' \n')

    i = (1 << k) - 1 + pos
    tree[i] += b
    while i != 0:
        i = (i - 1) // 2
        tree[i] = tree[2 * i + 1] + tree[2 * i + 2]
    print(*tree, end=' \n')


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
