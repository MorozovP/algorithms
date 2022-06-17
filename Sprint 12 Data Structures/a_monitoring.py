# 12 A. Мониторинг

from typing import Tuple


def print_result(m, n, matrix) -> None:
    for i in range(n):
        for j in range(m):
            print(matrix[j][i], end=' ')
        print()


def read_input() -> Tuple[int, int, list]:
    m, n = int(input()), int(input())
    matrix = []
    for _ in range(m):
        row = [c for c in input().split()]
        matrix.append(row)
    return m, n, matrix


def main() -> None:
    m, n, matrix = read_input()
    print_result(m, n, matrix)


if __name__ == '__main__':
    main()
