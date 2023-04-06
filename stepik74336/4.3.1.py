import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


def solution():
    n = int(input())
    q = deque([1])
    seen = set()
    while q:
        num = q.popleft()
        print(num, end=' ')
        for factor in [2, 3, 5]:
            x = num * factor
            if x <= n and x not in seen:
                q.append(x)
                seen.add(x)


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
