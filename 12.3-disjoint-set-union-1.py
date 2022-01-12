"""
4.1 Объединение таблиц
Ваша цель в данной задаче — реализовать симуляцию объединения
таблиц в базе данных.
В базе данных есть n таблиц, пронумерованных от 1 до n, над од-
ним и тем же множеством столбцов (атрибутов). Каждая таблица со-
держит либо реальные записи в таблице, либо символьную ссылку на
другую таблицу. Изначально все таблицы содержат реальные записи,
и i-я таблица содержит ri записей. Ваша цель — обработать m запро-
сов типа (destinationi; sourcei):
1. Рассмотрим таблицу с номером destinationi. Пройдясь по цепоч-
ке символьных ссылок, найдем номер реальной таблицы, на ко-
торую ссылается эта таблица:
пока таблица destinationi содержит символическую ссылку:
destinationi  <- symlink(destinationi)
2. Сделаем то же самое с таблицей sourcei.
3. Теперь таблицы destinationi и sourcei содержат реальные запи-
си. Если destinationi != sourcei, скопируем все записи из таблицы
sourcei в таблицу destinationi, очистим таблицу sourcei и пропи-
шем в нее символическую ссылку на таблицу destinationi.
4. Выведем максимальный размер среди всех n таблиц. Размером
таблицы называется число строк в ней. Если таблица содержит
символическую ссылку, считаем ее размер равным нулю.

Формат входа. Первая строка содержит числа n и m — число таблиц
и число запросов, соответственно. Вторая строка содержит n це-
лых чисел r1; : : : ; rn — размеры таблиц. Каждая из последующих
m строк содержит два номера таблиц destinationi и sourcei, кото-
рые необходимо объединить.

Формат выхода. Для каждого из m запросов выведите максималь-
ный размер таблицы после соответствующего объединения.
23
Ограничения. 1 <= n;m <= 100 000; 0 <= ri <= 10 000;
1 <= destinationi; sourcei <= n.
Пример.
Вход:
5 5
1 1 1 1 1
3 5
2 4
1 4
5 4
5 3
Выход:
2
2
3
5
5

Изначально каждая таблица содержит ровно одну строку.
1. После первой операции объединения все записи из табли-
цы 5 копируются в таблицу 3. Теперь таблица 5 является
ссылкой на таблицу 3, а таблица 3 содержит две записи.
2. Вторая операция аналогичным образом переносит все за-
писи из таблицы 2 в таблицу 4.
3. Третья операция пытается объединить таблицы 1 и 4, но
таблица 4 ссылается на таблицу 2, поэтому все записи из
таблицы 2 копируются в таблицу 1. Таблица 1 теперь содер-
жит три строки.
4. Чтобы произвести четвјртую операцию, проследим пути
из ссылок: 4 -> 2 -> 1 и 5 -> 3. Скопируем все записи из
таблицы 1 в таблицу 3, после чего в таблице 3 будет пять
записей.
5. После этого все таблицы ссылаются на таблицу 3, поэтому
все оставшиеся запросы объединения ничего не меняют.


Пример.
Вход:
6 4
10 0 5 0 3 3
6 6
6 5
5 4
4 3
Выход:
10
10
10
11
1. Запрос объединения таблицы 6 с собой ничего не меняет,
максимальным размером по-прежнему остајтся 10 (табли-
ца 1).
2. Записи из таблицы 5 копируются в таблицу 6, размер таб-
лицы 6 становится равным 6.
3. Записи из таблицы 4 копируются в таблицу 6, размер таб-
лицы 6 становится равным 10.
4. Записи из таблицы 3 копируются в таблицу 6, размер таб-
лицы 6 становится равным 11.
"""
from collections import namedtuple
from typing import List


class Node:
    def __init__(self, parent: int, rank: int, val: int):
        self.parent = parent
        self.rank = rank
        self.val = val


class DSU:
    def __init__(self, vals: List[int]):
        self.nodes = [Node(i, 0, vals[i]) for i in range(len(vals))]
        self.maximum = max(node.val for node in self.nodes)

    def find(self, i: int) -> int:
        while i != self.nodes[i].parent:
            i = self.nodes[i].parent
        return i

    def union(self, i: int, j: int):
        i_id = self.find(i)
        j_id = self.find(j)
        if i_id == j_id:
            return
        if self.nodes[i_id].rank > self.nodes[j_id].rank:
            self.nodes[j_id].parent = i_id
            self.nodes[i_id].val += self.nodes[j_id].val
            self.nodes[j_id].val = 0
            self.maximum = max(self.maximum, self.nodes[i_id].val)
        else:
            self.nodes[i_id].parent = j_id
            self.nodes[j_id].val += self.nodes[i_id].val
            self.nodes[i_id].val = 0
            self.maximum = max(self.maximum, self.nodes[j_id].val)
            if self.nodes[i_id].rank == self.nodes[j_id].rank:
                self.nodes[j_id].rank += 1


def main():
    n, m = (int(num) for num in input().split())
    dsu = DSU([int(num) for num in input().split()])
    Request = namedtuple('Request', ['dest', 'source'])
    requests = (Request._make(map(lambda num: int(num) - 1, input().split())) for _ in range(m))
    for request in requests:
        dsu.union(request.dest, request.source)
        print(dsu.maximum)


if __name__ == '__main__':
    main()
