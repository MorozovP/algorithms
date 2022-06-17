# A. Поиск в сломанном массиве
# 68739945


def broken_search(nums: list, target: int) -> int:
    """
    Функция осуществляет поиск в частично отсортированном массиве,
    при условии, что массив состоит из двух отсортированных подмассивов.
    :param nums: list
    :param target: int
    :return: int
    """
    left: int = 0
    right: int = len(nums)

    def binary_search(nums: list, target: int, left: int, right: int) -> int:
        """
        Функция бинарного поиска в отсортированном подмассиве.
        :param nums: list
        :param target: int
        :param left: int
        :param right: int
        :return: int
        """
        if left >= right:
            return -1
        middle = (left + right) // 2
        if nums[middle] == target:
            return middle
        elif target < nums[middle]:
            return binary_search(nums, target, left, middle)
        else:
            return binary_search(nums, target, middle + 1, right)

    def divide_and_search(nums: list, target: int, left: int,
                          right: int) -> list:
        """
        Функция поиска подмассива, содержащего в себе искомый элемент.
        Возвращает индексы начала и конца такого подмассива.
        :param nums: list
        :param target: int
        :param left: int
        :param right: int
        :return: list
        """
        if right - left == 1:
            return [left, right]
        middle = (left + right) // 2
        if nums[left] <= nums[middle]:
            if nums[left] <= target <= nums[middle]:
                return [left, middle + 1]
            else:
                return divide_and_search(nums, target, middle, right)
        else:
            if nums[middle] <= target <= nums[-1]:
                return [middle, right]
            else:
                return divide_and_search(nums, target, left, middle)

    if __name__ == '__main__':
        params = divide_and_search(nums, target, left, right)
        return binary_search(nums, target, *params)
