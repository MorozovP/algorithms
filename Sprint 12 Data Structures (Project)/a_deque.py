# A. Дек
# 68377950

class QueueIsFullError(Exception):
    """Ошибка при попытке добавить элемент в заполненную очередь."""
    def __str__(self):
        return repr(self)


class QueueIsEmptyError(Exception):
    """Ошибка при попытке извлечь элемент из пустой очереди."""
    def __str__(self):
        return repr(self)


class Queue:
    """Очередь, реализованная с использованием кольцевого буфера."""
    def __init__(self, max_size: int):
        self.__max_size: int = max_size
        self.__queue: list = [None] * max_size
        self.__head: int = 0
        self.__tail: int = 0
        self.__size: int = 0

    def is_empty(self) -> bool:
        return self.__size == 0

    def move_pointer(self, pointer: int, direction: bool = True) -> int:
        if direction:
            return (pointer + 1) % self.__max_size
        return (pointer - 1) % self.__max_size

    def push_back(self, value: str) -> None:
        if self.__size == self.__max_size:
            raise QueueIsFullError('error')
        if self.__queue[self.__tail]:
            self.__tail = self.move_pointer(self.__tail)
        self.__queue[self.__tail] = value
        self.__size += 1

    def push_front(self, value: str) -> None:
        if self.__size == self.__max_size:
            raise QueueIsFullError('error')
        if self.__queue[self.__head]:
            self.__head = self.move_pointer(self.__head, direction=False)
        self.__queue[self.__head] = value
        self.__size += 1

    def pop_front(self) -> None:
        if self.is_empty():
            raise QueueIsEmptyError('error')
        value = self.__queue[self.__head]
        self.__queue[self.__head] = None
        if self.__size > 1:
            self.__head = self.move_pointer(self.__head)
        self.__size -= 1
        print(value)

    def pop_back(self) -> None:
        if self.is_empty():
            raise QueueIsEmptyError('error')
        value = self.__queue[self.__tail]
        self.__queue[self.__tail] = None
        if self.__size > 1:
            self.__tail = self.move_pointer(self.__tail, direction=False)
        self.__size -= 1
        print(value)


def main() -> None:
    n: int = int(input())
    max_size: int = int(input())
    queue: Queue = Queue(max_size)
    for _ in range(n):
        args: list = input().split()
        getattr(queue, args.pop(0))(*args)


if __name__ == '__main__':
    main()
