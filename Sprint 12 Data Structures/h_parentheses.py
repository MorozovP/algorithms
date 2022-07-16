# 12 H. Скобочная последовательность

def correct_parentheses(s):
    """
    :param s: str
    :return: bool
    >>> correct_parentheses('((])')
    False
    >>> correct_parentheses('()()()')
    True
    >>> correct_parentheses('{[[])')
    False

    """

    for i in range(len(s) // 2):
        s = s.replace('()', '')
        s = s.replace('[]', '')
        s = s.replace('{}', '')
    if len(s) == 0:
        return True
    return False


def main() -> None:
    arr = input()
    print(correct_parentheses(arr))

if __name__ == '__main__':
    main()
