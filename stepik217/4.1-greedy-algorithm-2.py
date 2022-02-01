"""
Первая строка содержит количество предметов 1≤n≤10^3 и вместимость рюкзака 0≤W≤2⋅10^6.
Каждая из следующих n строк задаёт стоимость 0≤ci≤2⋅10^6 и объём 0<wi≤2⋅10^6 предмета (n, W, c_i, w_i — целые числа).
Выведите максимальную стоимость частей предметов
(от каждого предмета можно отделить любую часть, стоимость и объём при этом пропорционально уменьшатся),
помещающихся в данный рюкзак, с точностью не менее трёх знаков после запятой.

Sample Input:

3 50
60 20
100 50
120 30
Sample Output:

180.000
"""
import collections


def main():
    n, weight = map(int, input().split())
    Item = collections.namedtuple('Item', ['c', 'w'])
    items = sorted([Item(*map(int, input().split())) for _ in range(n)],
                   key=lambda item: item.c / item.w, reverse=True)
    cost = 0
    i = 0
    while i < n and weight > 0:
        cost += items[i].c if items[i].w <= weight else weight * items[i].c / items[i].w
        weight -= items[i].w
        i += 1
    print(f'{cost:.3f}')


if __name__ == '__main__':
    main()
