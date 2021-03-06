"""
В строкоремонтную мастерскую принесли строку, состоящую из строчных латинских букв.
Заказчик хочет сделать из неё палиндром.
В мастерской могут за 1 байтландский тугрик заменить произвольную букву в строке любой выбранной заказчиком буквой.
Какую минимальную сумму придётся заплатить заказчику за ремонт строки?
Напомним, что палиндромом называется строка, которая равна самой себе, прочитанной в обратном направлении.

Формат ввода
Входные данные содержат непустую строку, состоящую из строчных латинских букв, которую принёс заказчик.
Длина строки не превосходит 10^4

Формат вывода
Выведите одно целое число — минимальную сумму,
которую заказчику придётся заплатить за превращение принесённой заказчиком строки в палиндром.
"""


def solution(s: str) -> int:
    cost = 0
    n = len(s)
    for i in range(n // 2):
        if s[i] != s[n - 1 - i]:
            cost += 1

    return cost


def main():
    s = input()
    print(solution(s))


if __name__ == '__main__':
    main()
