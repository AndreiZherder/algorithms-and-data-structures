"""
Витя работает недалеко от одной из станций кольцевой линии Московского метро,
а живет рядом с другой станцией той же линии.
Требуется выяснить, мимо какого наименьшего количества промежуточных станций необходимо проехать Вите по кольцу,
чтобы добраться с работы домой.

Формат ввода
Станции пронумерованы подряд натуральными числами 1, 2, 3, …, N (1-я станция – соседняя с N-й), N не превосходит 100.

Вводятся три числа: сначала N – общее количество станций кольцевой линии, а затем i и j – номера станции,
на которой Витя садится, и станции, на которой он должен выйти. Числа i и j не совпадают. Все числа разделены пробелом.

Формат вывода
Требуется выдать минимальное количество промежуточных станций (не считая станции посадки и высадки),
которые необходимо проехать Вите.
"""


def solution(n: int, i: int, j: int) -> int:
    return min((j - i) % n - 1, (i - j) % n - 1)


def main():
    n, i, j = (int(_) for _ in input().split())
    print(solution(n, i, j))


if __name__ == '__main__':
    main()
