"""
Стек с поддержкой максимума
Реализовать стек с поддержкой операций push, pop и max.
Вход. Последовательность запросов push, pop и max.
Выход. Для каждого запроса max вывести максимальное
число, находящееся на стеке.
Стек — абстрактная структура данных,
поддерживающая операции push и pop.
Несложно реализовать стек так, чтобы обе
эти операции работали за константное
время. В данной задаче ваша цель — рас-
ширить интерфейс стека так, чтобы он до-
полнительно поддерживал операцию max
и при этом чтобы время работы всех опе-
раций по-прежнему было константным.
Формат входа. Первая строка содержит число запросов q. Каждая из
последующих q строк задает запрос в одном из следующих фор-
матов: push v, pop, or max.
Формат выхода. Для каждого запроса max выведите (в отдельной
строке) текущий максимум на стеке.
Ограничения. 1 <= q <= 400 000, 0 <= v <= 100 000.

Пример.
Вход:
3
push 1
push 7
pop
Выход:
Выход пуст, потому что нет max запросов.

Пример.
Вход:
5
push 2
push 1
max
pop
max
Выход:
2
2

Пример.
Вход:
6
push 7
push 1
push 7
max
pop
max
Выход:
7
7

Пример.
Вход:
5
push 1
push 2
max
pop
max
Выход:
2
1

Пример.
Вход:
10
push 2
push 3
push 9
push 7
push 2
max
max
max
pop
max
Выход:
9
9
9
9
"""


class MaxStack(list):
    def __init__(self):
        super().__init__()
        self.maxstack = []
        self.maximum = 0

    def append(self, num: int) -> None:
        super().append(num)
        self.maximum = max(self.maximum, num)
        self.maxstack.append(self.maximum)

    def pop(self, index: int = ...) -> int:
        self.maxstack.pop()
        if self.maxstack:
            self.maximum = self.maxstack[-1]
        else:
            self.maximum = 0
        return super().pop()

    def max(self) -> int:
        return self.maximum


def main():
    n = int(input())
    maxstack = MaxStack()
    for _ in range(n):
        command = input().split()
        if command[0] == 'push':
            maxstack.append(int(command[1]))
        elif command[0] == 'pop':
            maxstack.pop()
        elif command[0] == 'max':
            print(maxstack.max())


if __name__ == '__main__':
    main()
