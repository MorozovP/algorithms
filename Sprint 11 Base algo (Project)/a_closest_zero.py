# 67931953

from typing import List


def closest_zero(arr: List[int]) -> List[int]:
    arr.reverse()
    zero_index: int = -1
    for index, value in enumerate(arr):
        if value == 0:
            zero_index = index
        elif zero_index != -1 and (index - zero_index < value or value == -1):
            arr[index] = index - zero_index
    return arr


def read_input() -> List[int]:
    _ = input()
    arr: list = [0 if x == '0' else -1 for x in input().split()]
    return arr


def main() -> None:
    array: list = read_input()
    result: list = closest_zero(closest_zero(array))
    print(*result)


if __name__ == '__main__':
    main()
