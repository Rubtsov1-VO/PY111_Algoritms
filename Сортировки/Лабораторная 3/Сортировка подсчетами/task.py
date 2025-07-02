from typing import Sequence


def sort(container: Sequence[int]) -> Sequence[int]:
    """
    Сортировка подсчетами

    1. Определите максимальное значение в массиве и заполните вспомогательный массив с подсчетом количества элементов.
    2. Посчитайте количество каждого объекта
    3. Зная количество каждого объекта, восстановите отсортированный массив

    :param container: Массив, который надо отсортировать
    :return: Отсортированный в порядке возрастания массив
    """
    ...  # TODO реализовать алгоритм сортировки подсчетами
    if not container:
        return container

    min_value = min(container)
    max_value = max(container)

    count_range = max_value - min_value + 1
    count = [0] * count_range

    for num in container:
        count[num - min_value] += 1

    sorted_arr = []
    for index, freq in enumerate(count):
        sorted_arr.extend([index + min_value] * freq)

    return sorted_arr