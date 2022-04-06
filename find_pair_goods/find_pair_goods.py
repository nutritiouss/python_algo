from itertools import combinations


def from_chaos_to_order(list_example):
    # будем работать с моножествами пар
    analog_set = list(map(set, list_example))
    trigger = True
    # пока есть пересечения аналогов do
    while trigger:
        # флаг на случай, если пересечение множеств пустое
        trigger = False
        # проитерируемся по комбинации пар
        for s, t in combinations(analog_set, 2):
            # если пересечение пар не пустое
            if s & t:
                # добавим элементы t в множество s
                s.update(t)
                # очистим обьединенную пару в analog_set
                t.symmetric_difference_update(t)
                trigger = True
    #  выведем пары в соответствии с заданием
    for i in filter(None, map(tuple, analog_set)):
        print(i)

list_example = [[1102, 214], [214, 2007], [42, 315], [42, 316], [406, 2007], [4011, 512]]
from_chaos_to_order(list_example)
