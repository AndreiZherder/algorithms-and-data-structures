import sys
from collections import deque


def input():
    return sys.stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


def solution():
    mod = 10 ** 9 + 7
    n, k = (int(num) for num in input().split())
    s = input()
    dp = deque()
    total = 0
    for i in range(min(k, n)):
        if s[i] == '0':
            cur = total + 1
            total = (total + cur) % mod
            dp.append(cur)
        else:
            dp.append(0)
    for i in range(k, n):
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