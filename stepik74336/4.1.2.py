import sys
from collections import defaultdict

input = lambda: sys.stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


def solution():

    n = int(input())
    a = [int(num) for num in input().split()]

    d = defaultdict(list)
    gone = set()
    ans = []

    b = []
    for num in a:
        if num < 0:
            gone.add(-num)
        else:
            b.append(num)

    for i, prev in enumerate(b, start=1):
        d[prev].append(i)
    for prev in range(n + 1):
        stack = []
        while d[prev] or stack:
            if d[prev]:
                next = d[prev].pop()
                if next not in gone:
                    ans.append(next)
                stack.append(prev)
                prev = next
            else:
                prev = stack.pop()
    if ans:
        print(*ans)
    else:
        print(0)


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
