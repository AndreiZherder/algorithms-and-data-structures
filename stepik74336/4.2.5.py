import sys

input = lambda: sys.stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


def solution():
    s = input()
    stack = []
    d = {
        '}': '{',
        ')': '(',
        ']': '['
    }
    ans = 0
    for c in s:
        if c not in d:
            stack.append(c)
        else:
            if not stack:
                print('-1')
                return
            if stack[-1] != d[c]:
                ans += 1
            stack.pop()
    if stack:
        print('-1')
    else:
        print(ans)


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
