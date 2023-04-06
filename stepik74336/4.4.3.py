import sys

input = lambda: sys.stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


def solution():
    n = int(input())
    a = [int(num) for num in input().split()]
    ans = []
    tree = [None for i in range((1 << 21) - 1)]
    for num in a:
        root = 0
        while tree[root]:
            if num < tree[root]:
                root = root * 2 + 1
            else:
                root = root * 2 + 2
        tree[root] = num
        ans.append(root + 1)
    print(*ans, end=' \n')


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
