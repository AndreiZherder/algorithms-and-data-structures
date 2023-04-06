import sys
from heapq import heapify, heappop, heappush

input = lambda: sys.stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


def solution():
    n = int(input())
    a = [int(num) for num in input().split()]
    heapify(a)
    ans = 0
    while len(a) > 1:
        x = heappop(a)
        y = heappop(a)
        ans += x + y
        heappush(a, x + y)
    print(ans)


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
