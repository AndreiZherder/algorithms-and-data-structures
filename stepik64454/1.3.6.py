import sys


def input():
    return sys.stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


def solution():
    n, m = [int(num) for num in input().split()]
    a = [int(num) for num in input().split()]
    ans = []
    while m:
        x = int(input())
        left = 0
        right = n - 1
        while left <= right:
            mid = left + (right - left) // 2
            if a[mid] <= x:
                right = mid - 1
            else:
                left = mid + 1
        if left < n:
            ans.append(str(left + 1))
        else:
            ans.append('NO SOLUTION')
        m -= 1
    print('\n'.join(ans))


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
