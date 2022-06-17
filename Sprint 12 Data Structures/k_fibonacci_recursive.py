# 12 K. Рекурсивные числа Фибоначчи

def commit_count(n):
    if n == 1 or n == 0:
        return 1
    return commit_count(n - 1) + commit_count(n - 2)


def main() -> None:
    n = int(input())
    print(commit_count(n))


if __name__ == '__main__':
    main()
