import sys

input = lambda: sys.stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


def solution():
    n = int(input())
    a = [int(num) for num in input().split()]
    ans = 0
    stack = []
    for i in range(n - 1, -1, -1):
        while stack and stack[-1][0] < a[i]:
            stack.pop()
        if stack and stack[-1][0] == a[i]:
            ans += stack[-1][1]
            stack[-1][1] += 1
            if len(stack) > 1:
                ans += 1
        else:
            if stack:
                ans += 1
            stack.append([a[i], 1])
    stack = []
    for i in range(n):
        while stack and stack[-1][0] <= a[i]:
            stack.pop()
        if stack:
            ans += 1
        stack.append([a[i], 1])
    print(ans)


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
