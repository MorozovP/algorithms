def binary_search(arr, left, right, price):
    if right <= left or price > int(arr[right - 1]):
        return -1
    mid = (left + right) // 2
    if (int(arr[mid]) >= price and mid == left) or (
            int(arr[mid]) >= price > int(arr[mid - 1])):
        return mid + 1
    elif int(arr[mid]) < price:
        return binary_search(arr, mid, right, price)
    else:
        return binary_search(arr, left, mid, price)


def read_input():
    _ = input()
    arr: list = input().split()
    price = int(input())
    return arr, price


def main() -> None:
    array, price = read_input()
    day_1 = binary_search(array, 0, len(array), price)
    day_2 = binary_search(array, 0, len(array), price * 2)
    print(day_1, day_2)


if __name__ == '__main__':
    main()
