import sys

input = lambda: sys.stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


def solution():
    n = int(input())
    a = [int(num) for num in input().split()] + [0]
    m = int(input())
    b = [int(num) for num in input().split()]
    ans = []
    for x in b:
        cnt = 0
        for i, y in enumerate(a):
            if y == x:
                cnt += 1
            else:
                if cnt:
                    ans.append(((i - cnt) + (i - 1)) // 2 + 1)
                    break
        else:
            ans.append(0)
    print(*ans)


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
