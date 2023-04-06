import sys

input = lambda: sys.stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


def solution():
    n = int(input())
    a = [int(num) for num in input().split()]
    limits = [[0, 0] for i in range(n)]
    stack = []

    for i, num in enumerate(a):
        while stack and a[stack[-1]] >= num:
            stack.pop()
        if stack:
            limits[i][0] = stack[-1] + 1
        else:
            limits[i][0] = 0
        stack.append(i)

    a.reverse()
    stack = []
    for i, num in enumerate(a):
        while stack and a[stack[-1]] >= num:
            stack.pop()
        if stack:
            limits[n - i - 1][1] = n - stack[-1] - 2
        else:
            limits[n - i - 1][1] = n - 1
        stack.append(i)

    a.reverse()
    ans = 0
    for i in range(n):
        left, right = limits[i]
        ans = max(ans, (right - left + 1) * a[i])
    print(ans)


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
