def bubble_sort(seq):
    flag_1 = True
    n = len(seq) - 1
    for j in range(n):
        flag_2 = False
        for i in range(n - j):
            if seq[i] > seq[i + 1]:
                flag_1 = False
                flag_2 = True
                seq[i], seq[i + 1] = seq[i + 1], seq[i]
        if flag_2:
            print(*seq)
    if flag_1:
        print(*seq)


_ = input()
seq = [int(x) for x in input().split()]

bubble_sort(seq)
