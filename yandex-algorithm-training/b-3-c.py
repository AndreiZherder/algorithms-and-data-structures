"""
Дан список. Выведите те его элементы, которые встречаются в списке только один раз.
Элементы нужно выводить в том порядке, в котором они встречаются в списке.

Формат ввода
Вводится список чисел. Все числа списка находятся на одной строке.

Формат вывода
Выведите ответ на задачу.
"""
from collections import Counter


def main():
    d = Counter(input().split())
    for k, v in d.items():
        if v == 1:
            print(k, end=' ')


if __name__ == '__main__':
    main()
