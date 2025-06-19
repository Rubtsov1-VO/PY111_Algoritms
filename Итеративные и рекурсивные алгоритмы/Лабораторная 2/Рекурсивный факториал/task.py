def factorial_recursive(n: int) -> int:
    """
    Рассчитать факториал числа n рекурсивным способом

    :param n: Число, факториал которого нужно найти
    :return: n! - факториал числа n
    """
    ...  # TODO реализовать рекурсивный алгоритм нахождения факториала
    if n < 0:
        raise ValueError
    elif not isinstance(n, int):
        raise TypeError
    elif n == 0:
        return 1
    else:
        return n * factorial_recursive(n - 1)



