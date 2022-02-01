"""
По данной непустой строке s длины не более 10^4, состоящей из строчных букв латинского алфавита,
постройте оптимальный беспрефиксный код.
В первой строке выведите количество различных букв k, встречающихся в строке,
и размер получившейся закодированной строки. В следующих kk строках запишите коды букв в формате "letter: code".
В последней строке выведите закодированную строку.
Sample Input 1:
a

Sample Output 1:
1 1
a: 0
0

Sample Input 2:
abacabad

Sample Output 2:
4 14
a: 0
b: 10
c: 110
d: 111
01001100100111
"""
import collections
from functools import total_ordering
import heapq
from typing import List


def huffman_encode(input_string: str):
    @total_ordering
    class Node:
        def __init__(self, freq: int, symbol: str, left=None, right=None, bit: str = ''):
            self.freq = freq
            self.symbol = symbol
            self.left = left
            self.right = right
            self.bit = bit

        def __str__(self):
            return f'{self.symbol}: {self.freq}'

        def __lt__(self, other):
            return self.freq < other.freq

        def __eq__(self, other):
            return self.freq == other.freq

    def get_huffman_dict(node: Node, d: dict, bits: List[str] = None):
        if bits is None:
            bits = []
        if not node.left and not node.right:
            d[node.symbol] = ''.join(bits + [node.bit])
            return
        get_huffman_dict(node.left, d, bits + [node.bit])
        get_huffman_dict(node.right, d, bits + [node.bit])

    freq = collections.Counter(input_string)
    nodes = []
    for symbol in freq:
        heapq.heappush(nodes, Node(freq[symbol], symbol))
    while len(nodes) > 1:
        node1 = heapq.heappop(nodes)
        node1.bit = '0'
        node2 = heapq.heappop(nodes)
        node2.bit = '1'
        heapq.heappush(nodes, Node(node1.freq + node2.freq, '', node1, node2))

    if len(freq) == 1:
        huffman_dict = {nodes[0].symbol: '0'}
    else:
        huffman_dict = {}
        get_huffman_dict(nodes[0], huffman_dict)
    encoded_string = ''.join([huffman_dict[symbol] for symbol in input_string])
    return freq, huffman_dict, encoded_string


def main():
    input_string = input()
    freq, huffman_dict, encoded_string = huffman_encode(input_string)
    print(len(freq), len(encoded_string))
    for symbol, bits in sorted(huffman_dict.items()):
        print(f'{symbol}: {bits}')
    print(encoded_string)


if __name__ == '__main__':
    main()
