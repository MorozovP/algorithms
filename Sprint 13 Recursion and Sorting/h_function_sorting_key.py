from functools import cmp_to_key as cmp


def largest_number(seq):
    seq.sort(key=cmp(compare), reverse=True)
    print(*seq, sep='')


def compare(x, y):
    return 1 if x + y > y + x else -1


def read_input():
    return input().split()


_ = input()
largest_number(read_input())
