import sys
from collections import deque


def input():
    return sys.stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


def solution():
    mod = 10 ** 9 + 7
    n = int(input())
    s = input()
    dp = deque()
    total = 0
    for i in range(min(3, n)):
        if s[i] == '0':
            cur = total + 1
            total += cur
            dp.append(cur)
        else:
            dp.append(0)
    total = sum(dp)
    for i in range(3, n):
        if s[i] == '1':
            x = 0
        else:
            x = total
        dp.append(x)
        total = (total + x - dp.popleft()) % mod
    print(dp[-1])


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()