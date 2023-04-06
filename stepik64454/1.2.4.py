import sys


def input():
    return sys.stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


def solution():
    n, q = (int(num) for num in input().split())
    a = [0 for i in range(n + 1)]
    total = 0
    for i, num in enumerate(input().split(), start=1):
        total += int(num)
        a[i] = total
    ans = []
    while q:
        l, r = (int(num) for num in input().split())
        ans.append(a[r] - a[l - 1])
        q -= 1
    print(*ans, sep='\n')


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
