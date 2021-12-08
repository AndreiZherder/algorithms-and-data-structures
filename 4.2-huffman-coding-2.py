"""
Восстановите строку по её коду и беспрефиксному коду символов.
В первой строке входного файла заданы два целых числа k и l через пробел — количество различных букв,
встречающихся в строке, и размер получившейся закодированной строки, соответственно.
В следующих k строках записаны коды букв в формате "letter: code".
Ни один код не является префиксом другого. Буквы могут быть перечислены в любом порядке.
В качестве букв могут встречаться лишь строчные буквы латинского алфавита;
каждая из этих букв встречается в строке хотя бы один раз.
Наконец, в последней строке записана закодированная строка.
Исходная строка и коды всех букв непусты.
Заданный код таков, что закодированная строка имеет минимальный возможный размер.

В первой строке выходного файла выведите строку s. Она должна состоять из строчных букв латинского алфавита.
Гарантируется, что длина правильного ответа не превосходит 10^4 символов.

Sample Input 1:
1 1
a: 0
0

Sample Output 1:
a

Sample Input 2:
4 14
a: 0
b: 10
c: 110
d: 111
01001100100111

Sample Output 2:
abacabad
"""


def huffman_decode(encoded_string: str, huffman_decode_dict: dict):
    decoded_string = []
    bits = []
    for bit in encoded_string:
        bits.append(bit)
        if ''.join(bits) in huffman_decode_dict:
            decoded_string.append(huffman_decode_dict[''.join(bits)])
            bits = []
    return ''.join(decoded_string)


def main():
    n, _ = map(int, input().split())
    huffman_decode_dict = {}
    for _ in range(n):
        symbol, bits = input().split(': ')
        huffman_decode_dict[bits] = symbol
    encoded_string = input()
    print(huffman_decode(encoded_string, huffman_decode_dict))


if __name__ == '__main__':
    main()
