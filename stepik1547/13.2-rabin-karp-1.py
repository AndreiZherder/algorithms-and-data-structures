"""
Поиск образца в тексте
Найти все вхождения строки Pattern в строку Text.
Вход. Строки Pattern и Text.
Выход. Все индексы i строки Text, начиная с которых стро-
ка Pattern входит в Text:
Text[i::i + |Pattern| - 1] = Pattern.
Реализуйте алгоритм Карпа–Рабина.
Формат входа. Образец Pattern и текст Text.
Формат выхода. Индексы вхождений строки
Pattern в строку Text в возрастающем порядке, используя индек-
сацию с нуля.
Ограничения. 1 <= |Pattern| <= |Text| <= 5 * 10^5.
Суммарная длина всех вхождений образ-
ца в текста не превосходит 10^8. Обе стро-
ки содержат буквы латинского алфавита.

Пример.
Вход:
aba
abacaba
Выход:
0 4
Образец aba входит в позициях 0 (abacaba) и 4 (abacaba) в
текст abacaba.

Пример.
Вход:
Test
testTesttesT
Выход:
4

Пример.
Вход:
aaaaa
baaaaaaa
Выход:
1 2 3
Данный пример демонстрирует, что вхождения могут наклады-
ваться друг на друга.
Подсказки по реализации.
Будьте осторожны с переполнением целого типа. Приме-
няйте операцию взятия по модулю p после каждой арифме-
тической операции.
Будьте осторожны с взятием отрицательных чисел по моду-
лю.
Будьте осторожны с операцией взяти подстроки — она мо-
жет оказаться дорогой по времени и по памяти.
"""
from typing import List


class RabinKarp:
    def __init__(self):
        self.p = 1000000007
        self.x = 263
        self.xs = []
        self.prev_hash = 0

    def find(self, s: str, pattern: str) -> List[int]:
        ans = []
        self.xcalc(len(pattern))
        pattern_hash = self.hash(pattern, 0, len(pattern))
        text_hash = self.hash(s, len(s) - len(pattern), len(pattern))
        if pattern_hash == text_hash and self.equal(s, len(s) - len(pattern), pattern):
            ans.append(len(s) - len(pattern))
        self.prev_hash = text_hash
        for i in range(len(s) - len(pattern) - 1, -1, -1):
            text_hash = self.rolling_hash(s, i, len(pattern))
            if pattern_hash == text_hash and s[i:i + len(pattern)] == pattern:
                ans.append(i)
            self.prev_hash = text_hash
        return ans

    def xcalc(self, win_len: int):
        self.xs = [1]
        for i in range(1, win_len):
            self.xs.append((self.xs[i - 1] * self.x) % self.p)

    def hash(self, s: str, start: int, win_len: int) -> int:
        acc = 0
        for i in range(win_len):
            acc = (acc + (ord(s[start + i]) * (self.xs[i] % self.p)) % self.p) % self.p
        return acc

    def rolling_hash(self, s: str, start: int, win_len: int) -> int:
        tmp = ord(s[start + win_len]) * (self.xs[-1] % self.p) % self.p
        tmp = (self.prev_hash - tmp) % self.p
        tmp = tmp * self.x % self.p
        return (tmp + ord(s[start])) % self.p

    def equal(self, s: str, start: int, pattern: str):
        return all(pattern[i] == s[start + i] for i in range(len(pattern) - 1, -1, -1))


def main():
    pattern, s = input(), input()
    print(*reversed(RabinKarp().find(s, pattern)))


if __name__ == '__main__':
    main()
