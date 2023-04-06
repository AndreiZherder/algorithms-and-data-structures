import sys

input = lambda: sys.stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


def solution():
    n, s = [int(num) for num in input().split()]
    ts = []
    ws = []
    for i in range(n):
        t, w = [int(num) for num in input().split()]
        ts.append(t)
        ws.append(w)
    left = 0
    w, t = min(zip(ws, ts), key=lambda x: (x[0], -x[1]))
    right = s // w * t
    while left <= right:
        mid = left + (right - left) // 2
        if s <= sum(mid // t * w for w, t in zip(ws, ts)):
            right = mid - 1
        else:
            left = mid + 1
    print(sum(w * ((left + t - 1) // t) for w, t in zip(ws, ts)))


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
