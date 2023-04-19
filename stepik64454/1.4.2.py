import sys

input = lambda: sys.stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


def solution():
    def f(x: float) -> float:
        ans = 0
        for i in range(n + 1):
            ans += a[i] * x ** i
        return ans


    cx, cy, cd = [float(num) for num in input().split()]
    n = int(input())
    a = [float(num) for num in input().split()]
    a.reverse()
    x = float(input())
    left = x
    right = x + 3 * cd
    for i in range(100):
        mid = left + (right - left) / 2
        if (mid - cx) ** 2 + (f(mid) - cy) ** 2 > cd ** 2:
            right = mid
        else:
            left = mid
    print(mid)


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
