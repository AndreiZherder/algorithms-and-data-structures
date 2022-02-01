"""
Хеширование цепочками — один из наи-
более популярных методов реализации
хеш-таблиц на практике. Ваша цель в дан-
ной задаче—реализовать такую схему, ис-
пользуя таблицу с m ячейками и полино-
миальной хеш-функцией на строках
h(S) = sum(s[i] * x ** i % p) % m
где S[i]—ASCII-код i-го символа строки S, p = 1 000 000 007—простое
число, а x = 263.
Ваша программа должна поддерживать следующие
типы запросов:

add string: добавить строку string в таблицу. Если такая
строка уже есть, проигнорировать запрос;
del string: удалить строку string из таблицы. Если такой
строки нет, проигнорировать запрос;
find string: вывести «yes» или «no» в зависимости от того,
есть в таблице строка string или нет;
check i: вывести i-й список (используя пробел в качестве раз-
делителя); если i-й список пуст, вывести пустую строку.
При добавлении строки в цепочку, строка должна добавляться в на-
чало цепочки.

Формат входа. Первая строка размер хеш-таблицы m. Следующая
строка содержит количество запросов n. Каждая из последую-
щих n строк содержит запрос одного из перечисленных выше
четырех типов.

Формат выхода. Для каждого из запросов типа find и check выве-
дите результат в отдельной строке.

Ограничения. 1 <= n <= 10^5; n / 5 <= m <= n. Все строки имеют длину
от одного до пятнадцати и содержат только буквы латинского
алфавита.

Пример.
Вход:
5
12
add world
add HellO
check 4
find World
find world
del world
check 4
del HellO
add luck
add GooD
check 2
del good
Выход:
HellO world
no
yes
HellO
GooD luck

ASCII коды букв ’w’, ’o’, ’r’, ’l’, ’d’ равны 119, 111, 114, 108, 100,
соответственно. Поэтому
h(world) = (119 + 111 * 263 + 114 * 263 ** 2 + 108 * 263 ** 3+
100 * 263 ** 4 mod 1 000 000 007) mod 5 = 4 :
Оказывается, что h(HellO) тоже равно четырем. Поскольку но-
вые строки добавляются в начало списка, после второго запро-
са add список содержит строки HellO и world (именно в таком
порядке). Строка World не находится, а world находится. По-
сле удаления строки world в цепочке 4 остается только строка
HellO. И так далее.

Пример.
Вход:
4
8
add test
add test
find test
del test
find test
find Test
add Test
find Test
Выход:
yes
no
no
yes


Пример.
Вход:
3
12
check 0
find help
add help
add del
add add
find add
find del
del del
find del
check 0
check 1
check 2
Выход:
no
yes
yes
no
add help

Обратите внимание на то, что нужно выводить пустую строку в
случае, если соответствующая цепочка пуста. Строки в запросах
могут совпадать с названиями запросов.
Указания.
Будьте осторожны с переполнением целого типа. Исполь-
зуйте long long в C++ и long в Java при необходимости.
При вычислении значения многочлена по модулю p берите
результат по модулю p после каждой арифметической опе-
рации.
Будьте осторожны с отрицательными числами по модулю p.
Во многих языках программирования (-2)%5 != 3%5. Один
из способов избежать этого — использовать x = ((a%p) + p)%p вместо x = a%p.
"""


class StringHashMap:
    def __init__(self, m: int):
        self.m = m
        self.hashmap = [[] for _ in range(m)]

    def hash(self, s: str):
        x = 263
        p = 1000000007
        acc = ord(s[0])
        mul = 1
        for c in s[1:]:
            mul = (mul * x) % p
            acc = (acc + ((ord(c) * mul) % p)) % p
        return acc % self.m

    def add(self, s: str):
        hash = self.hash(s)
        try:
            i = self.hashmap[hash].index(s)
        except ValueError:
            i = -1
        if i == -1:
            self.hashmap[hash].append(s)

    def delete(self, s: str):
        hash = self.hash(s)
        try:
            i = self.hashmap[hash].index(s)
        except ValueError:
            i = -1
        if i != -1:
            self.hashmap[hash].pop(i)

    def find(self, s: str):
        try:
            i = self.hashmap[self.hash(s)].index(s)
        except ValueError:
            i = -1
        return i

    def check(self, i: int):
        return list(reversed(self.hashmap[i]))


def main():
    m, n = int(input()), int(input())
    d = StringHashMap(m)
    for _ in range(n):
        cmd = input().split()
        if cmd[0] == 'add':
            d.add(cmd[1])
        elif cmd[0] == 'del':
            d.delete(cmd[1])
        elif cmd[0] == 'find':
            print('yes' if d.find(cmd[1]) != -1 else 'no')
        elif cmd[0] == 'check':
            print(*d.check(int(cmd[1])))


if __name__ == '__main__':
    main()
