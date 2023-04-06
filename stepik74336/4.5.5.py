import sys

input = lambda: sys.stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


def solution():
    n = int(input())
    a = [int(num) for num in input().split()]
    ans = []

    tree = dict()
    for num in a:
        root = 0
        while root in tree:
            if num < tree[root]:
                root = root * 2 + 1
            else:
                root = root * 2 + 2
        tree[root] = num
        if root == 0:
            ans.append(-1)
        else:
            ans.append(tree[(root - 1) // 2])
    print(*ans, end=' \n')


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
