# 67932189

from typing import Tuple

NUMBER_OF_ROWS = 4
NUMBER_OF_PLAYERS = 2


def typing_trainer(k: int, digits: str) -> int:
    nums_dict: dict = {}
    for num in digits:
        nums_dict[num] = nums_dict.get(num, 0) + 1
    result: int = 0
    for num in nums_dict.values():
        if num <= k * NUMBER_OF_PLAYERS:
            result += 1
    return result


def read_input() -> Tuple[int, str]:
    digits: str = ''
    k: int = int(input())
    for _ in range(NUMBER_OF_ROWS):
        for c in input():
            if c.isdigit():
                digits += c
    return k, digits


def main() -> None:
    k, digits = read_input()
    result = typing_trainer(k, digits)
    print(result)


if __name__ == '__main__':
    main()
