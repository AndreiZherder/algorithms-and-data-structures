from collections import deque
from sys import stdin, stdout


def input():
    return stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    stdout.write(sep.join(map(str, args)))
    stdout.write(end)


def solution():
    n, k = [int(num) for num in input().split()]
    a = [int(num) for num in input().split()] + [0]
    dp = [10 ** 20 for i in range(n + 1)]
    dp[-1] = 0
    prev = [-1 for i in range(n)]
    q = deque([-1])
    for i in range(n):
        while q[0] < i - k:
            q.popleft()
        dp[i] = dp[q[0]] + a[i]
        prev[i] = q[0]
        while q and dp[q[-1]] >= dp[i]:
            q.pop()
        q.append(i)
    i = n - 1
    path = []
    while i != -1:
        path.append(i + 1)
        i = prev[i]
    print(dp[n - 1], len(path))
    print(*reversed(path))





def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
