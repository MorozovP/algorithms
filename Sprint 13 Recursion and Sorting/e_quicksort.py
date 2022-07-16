def partition(s, pivot):
    left, center, right = [], [], []
    for item in s:
        if item < pivot:
            left.append(item)
        elif item == pivot:
            center.append(item)
        else:
            right.append(item)
    return left, center, right


def quicksort(sequence):
    if len(sequence) < 2:
        return sequence
    else:
        pivot = sequence[-1]
        left, center, right = partition(sequence, pivot)
        return quicksort(left) + center + quicksort(right)


def houses_counter(prices, amount):
    """
    Подсчет количества домов, которые можно купить на имеющуюся сумму.
    :param prices: List[int]
    :param amount: int
    :return: int
    >>> houses_counter([999, 999, 999], 1000)
    1
    """
    if prices:
        prices = quicksort(prices)
    tmp = 0
    for i in range(len(prices)):
        tmp += prices[i]
        if tmp > amount:
            return i
        if i == len(prices) - 1:
            return i + 1
    return 0


def read_input():
    _, amount = [int(x) for x in input().split()]
    prices = [int(x) for x in input().split() if int(x) <= amount]
    return amount, prices


def main():
    amount, prices = read_input()
    result = houses_counter(prices, amount)
    print(result)


if __name__ == '__main__':
    main()
