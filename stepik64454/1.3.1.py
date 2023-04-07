import sys


def input():
    return sys.stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


def solution():
    n, m = [int(num) for num in input().split()]
    ans = []
    while m:
        k = int(input())
        left = -1
        right = n
        cnt = 0
        while left + 1 < right:
            cnt += 1
            mid = left + (right - left) // 2
            if k <= mid:
                right = mid
            else:
                left = mid
        ans.append(cnt)
        m -= 1
    print(*ans, sep='\n')


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
