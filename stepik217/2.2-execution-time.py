"""
Измерить время выполнения функции
"""
import time
import matplotlib.pyplot as plt
import functools


def timed(f, *args, n=100):
    acc = float('Inf')
    for _ in range(n):
        t1 = time.perf_counter_ns()
        f(*args)
        t2 = time.perf_counter_ns()
        acc = min(acc, t2 - t1)
    return acc


def fib0(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib0(n - 2) + fib0(n - 1)


@functools.lru_cache()
def fib1(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib1(n - 2) + fib1(n - 1)


def fib2(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    f0, f1 = 0, 1
    for _ in range(2, n + 1):
        f0, f1 = f1, f0 + f1
    return f1


def main():
    n = 200
    fig, ax = plt.subplots()
    ax.plot(list(range(n)), [timed(fib2, i) for i in range(n)])
    ax.set_xlabel('n')
    ax.set_ylabel('time, ns')
    ax.set_title('Execution time')
    ax.grid()
    fig.show()


if __name__ == '__main__':
    main()
