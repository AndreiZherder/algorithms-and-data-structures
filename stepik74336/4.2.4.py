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
    for c in s:
        if c not in d:
            stack.append(c)
        else:
            if not stack or stack[-1] != d[c]:
                print('NO')
                return
            stack.pop()
    if stack:
        print('NO')
    else:
        print('YES')


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
