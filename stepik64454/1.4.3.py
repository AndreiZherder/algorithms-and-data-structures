import sys

input = lambda: sys.stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


def solution():
    def can_place(mid: int) -> bool:
        y = mid // h
        x = mid // w
        return x * y >= n


    w, h, n = [int(num) for num in input().split()]
    if w > h:
        w, h = h, w
    left = h
    right = n * h
    while left <= right:
        mid = left + (right - left) // 2
        if can_place(mid):
            right = mid - 1
        else:
            left = mid + 1
    print(left)


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
