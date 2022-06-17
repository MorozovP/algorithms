sequence_1 = list(input())
sequence_2 = list(input())


def is_subsequence(subsequence, sequence):
    if len(subsequence) > len(sequence):
        return False
    left = 0
    for character in subsequence:
        try:
            right = sequence.index(character, left)
        except:
            return False
        left = right + 1
    return True


print(is_subsequence(sequence_1, sequence_2))
