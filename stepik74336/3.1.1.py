import sys

input = lambda: sys.stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


def solution():
    n = int(input())
    a = [int(num) for num in input().split()]
    m = int(input())
    b = [int(num) for num in input().split()]
    ans = []
    for num in b:
        for i in range(n):
            if a[i] > num:
                ans.append(0)
                break
            if a[i] == num:
                ans.append(i + 1)
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
