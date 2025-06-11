"""
My little Queue
"""
from typing import Any


class Queue:
    def __init__(self):
        """
        Очередь с помощью python list
        TODO Описать где начало и конец очереди
        """
        self._list = []   # TODO инициализировать список

    def enqueue(self, elem: Any) -> None:
        """
        Добавление элемент в конец очереди

        :param elem: Элемент, который должен быть добавлен
        """
        self._list.append(elem)
        print(self._list)# TODO реализовать метод enqueue

    def dequeue(self) -> Any:
        """
        Извлечение элемента из начала очереди.

        :raise: IndexError - Ошибка, если очередь пуста

        :return: Извлеченный с начала очереди элемент.
        """
        if len(self._list) == 0:
            raise IndexError("Ошибка, очередь пуста")
        self._list.pop(0)  # TODO реализовать метод dequeue

    def peek(self, ind: int = 0) -> Any:
        """
        Просмотр произвольного элемента, находящегося в очереди, без его извлечения.

        :param ind: индекс элемента (отсчет с начала, 0 - первый с начала элемент в очереди, 1 - второй с начала элемент в очереди, и т.д.)

        :raise: TypeError - если указан не целочисленный тип индекса
        :raise: IndexError - если индекс вне границ очереди

        :return: Значение просмотренного элемента
        """

        if not isinstance(ind, int):
            raise TypeError("Указан не целочисленный тип индекса")
        if ind > len(self._list):
            raise IndexError("Индекс вне границ очереди")

        print(self._list.count(ind))  # TODO реализовать метод peek

    def clear(self) -> None:
        """ Очистка очереди. """
        self._list.clear()  # TODO реализовать метод clear

    def __len__(self):
        """ Количество элементов в очереди. """
        print(self._list.__len__())  # TODO реализовать метод __len__

if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(3)
    queue.enqueue(4)
    queue.enqueue(3)
    queue.enqueue(4)
    queue.__len__()
    queue.enqueue(3)
    queue.clear()
    queue.enqueue(4)
    queue.peek(0)