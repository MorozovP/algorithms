# B. Эффективная быстрая сортировка 
# 68782590


from dataclasses import dataclass, field
from typing import List


@dataclass(order=True)
class Participant:
    """Участники соревнования."""
    score: int = field(compare=False)
    score_to_compare: int = field(init=False, repr=False)
    penalty: int
    login: str

    def __post_init__(self):
        self.score_to_compare = self.score * (-1)


def partition(n: List[Participant], low: int, high: int) -> int:
    """
    Вспомогательная функция быстрой сортировки. Сравнивает элементы массива с опорным
    элементом и перемещает элементы меньшие опорного в начало массива, элементы
    больше опорного - в конец. Возвращает индекс опорного элемента.
    """
    i: int = low - 1
    pivot: Participant = n[high]
    for j in range(low, high):
        if n[j] <= pivot:
            i += 1
            n[i], n[j] = n[j], n[i]
    n[i + 1], n[high] = n[high], n[i + 1]
    return i + 1


def quicksort_inplace(n: list, low: int = 0, high: int = None) -> None:
    """ Функция быстрой сортировки."""
    if high is None:
        high = len(n) - 1
    if low < high:
        pivot_index = partition(n, low, high)
        quicksort_inplace(n, low, pivot_index - 1)
        quicksort_inplace(n, pivot_index, high)


def read_input() -> List[Participant]:
    n: int = int(input())
    participant_list: list = []
    for _ in range(n):
        tmp: list = input().split()
        participant = Participant(login=tmp[0], score=int(tmp[1]),
                                  penalty=int(tmp[2]))
        participant_list.append(participant)
    return participant_list


def main() -> None:
    participant_list: list = read_input()
    quicksort_inplace(participant_list)
    print(*[participant.login for participant in participant_list], sep='\n')


if __name__ == '__main__':
    main()
