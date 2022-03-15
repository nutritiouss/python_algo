import time


def time_of_function(function):
    """Вычисление времени выполнения функции"""

    def wrapped(*args):
        start_time = time.perf_counter_ns()
        res = function(*args)
        time_execute = round((time.perf_counter_ns() - start_time) / pow(10, 6), 5)
        print('Время выполнения расчета функции {}: {} милисекунд'.format(function.__name__, time_execute))
        return res

    return wrapped


def cast_to_int(digit):
    """Приведение строкового типа к целочисленному"""
    try:
        digit = int(digit)
        return digit
    except ValueError as error:
        print(error)
        exit()


@time_of_function
def newton_approx_square_root(x):
    '''Функция находит квадратный корень с минимальной точностью 0,001,
     используя метод последовательных приближений Ньютона.'''
    aprox = x / 2
    counter = 0
    while abs(x - aprox ** 2) > 0.001:
        print("{} -я итерация, решение :  {}".format(counter + 1, round(aprox, 3)))
        aprox = (aprox + x / aprox) / 2
        counter += 1
    print("Квадратный корень из {} равен {}".format(x, round(aprox, 3)))
    return round(aprox, 3)


while True:
    a = input('Введите положительное натуральное арабское число и нажмите Enter:').strip()
    if a.isdigit():
        break
    print('Необходимо ввести положительное натуральное арабское число')
a = cast_to_int(a)
square_root = newton_approx_square_root(a)
