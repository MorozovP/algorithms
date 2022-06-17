# B. Калькулятор
# 68450761

class Queue:
    """Очередь, реализованная на основе списка."""

    def __init__(self):
        self.__items: list = []

    def push(self, arr: list) -> None:
        self.__items = arr

    def pop(self) -> str:
        return self.__items.pop(0)

    def is_empty(self) -> bool:
        return len(self.__items) == 0


class Calculator:
    """
    Калькулятор. Функции:
    reverse_polish_notation - вычисляет значение по правилам обратной
    польской записи.
    """
    actions: dict = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: a // b,
    }

    @classmethod
    def action(cls, x: str, a: int, b: int):
        return cls.actions[x](a, b)

    @classmethod
    def reverse_polish_notation(cls, queue: Queue) -> int:
        """
        Функция принимает выражение, в виде списка операндов и знаков операций.
        Вычисляет значение выражения согласно правилам обратной польской
        записи.
        :param queue: Queue
        :return: int
        """
        stack: list = []
        while not queue.is_empty():
            x: str = queue.pop()
            if x not in cls.actions.keys():
                stack.append(int(x))
            else:
                b: int = stack.pop()
                a: int = stack.pop()
                res: int = cls.action(x, a, b)
                stack.append(res)
        return stack[-1]


def main() -> None:
    queue = Queue()
    queue.push(input().split())
    print(Calculator.reverse_polish_notation(queue))


if __name__ == '__main__':
    main()
