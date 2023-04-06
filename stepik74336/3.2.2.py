import sys

input = lambda: sys.stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


def solution():
    n, k = [int(num) for num in input().split()]
    a = []
    for i in range(n):
        a.append(int(input()))
    left, right = 1, max(a)
    while left <= right:
        mid = left + (right - left) // 2
        if sum(num // mid for num in a) >= k:
            left = mid + 1
        else:
            right = mid - 1
    print(left - 1)


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
