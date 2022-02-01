"""
Лена руководит разработкой тестирующей системы, в которой реализованы интерактивные задачи.
До заверщения очередной стадии проекта осталось написать модуль,
определяющий итоговый вердикт системы для интерактивной задачи.
Итоговый вердикт определяется из кода завершения задачи, вердикта интерактора и вердикта чекера по следующим правилам:

Вердикт чекера и вердикт интерактора — это целые числа от 0 до 7 включительно.
Код завершения задачи — это целое число от -128 до 127 включительно.
Если интерактор выдал вердикт 0, итоговый вердикт равен 3 в случае, если программа завершилась с ненулевым кодом,
и вердикту чекера в противном случае.
Если интерактор выдал вердикт 1, итоговый вердикт равен вердикту чекера.
Если интерактор выдал вердикт 4, итоговый вердикт равен 3 в случае, если программа завершилась с ненулевым кодом,
и 4 в противном случае.
Если интерактор выдал вердикт 6, итоговый вердикт равен 0.
Если интерактор выдал вердикт 7, итоговый вердикт равен 1.
В остальных случаях итоговый вердикт равен вердикту интерактора.
Ваша задача — реализовать этот модуль.

Формат ввода
Входной файл состоит из трёх строк. В первой задано целое число
r (−128 ≤ r ≤ 127) — код завершения задачи, во второй — целое число
i (0 ≤ i ≤ 7) — вердикт интерактора, в третьей — целое число
c (0 ≤ c ≤ 7) — вердикт чекера.
Формат вывода
Выведите одно целое число от 0 до 7 включительно — итоговый вердикт системы.
"""


def solution(r: int, i: int, c: int) -> int:
    if i == 0:
        if r != 0:
            return 3
        else:
            return c
    elif i == 1:
        return c
    elif i == 4:
        if r != 0:
            return 3
        else:
            return 4
    elif i == 6:
        return 0
    elif i == 7:
        return 1
    else:
        return i


def main():
    r = int(input())
    i = int(input())
    c = int(input())
    print(solution(r, i, c))


if __name__ == '__main__':
    main()
