import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


def solution():
    n, d = (int(num) for num in input().split())
    q = deque((int(num) for num in input().split()))
    ans = 0
    while q:
        if len(q) == 1:
            q.popleft()
            ans += 1
        elif q[0] + q[-1] > d:
            q.pop()
            ans += 1
        else:
            q.pop()
            q.popleft()
            ans += 1
    print(ans)


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
