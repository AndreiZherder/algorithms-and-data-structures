import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


def solution():
    n = int(input())
    q = deque()
    ans = []
    i = 1
    for x in (int(num) for num in input().split()):
        if x == 1:
            q.appendleft(i)
            i += 1
        elif x == 2:
            q.append(i)
            i += 1
        elif x == 3:
            if q:
                ans.append(q.popleft())
            else:
                ans.append(-1)
        else:
            if q:
                ans.append(q.pop())
            else:
                ans.append(-1)
    print(*ans, end=' \n')


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
