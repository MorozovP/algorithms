import array

base = int(input())
m = int(input())
text = [ord(x) for x in input()]
n = int(input())


hash_index = array.array('I',)


def polinom(base, m, sequence, hash_index, start):
    if sequence:
        hash_index.append(sequence[start - 1] % m)
        for j in range(start, len(sequence)):
            hash_index.append((hash_index[-1] * base + sequence[j]) % m)
    return 0


def build_hash_index_2(text, ind):
    for i in range(1, len(text)+1):
        polinom(base, m, sequence=text, hash_index=ind, start=i)
    return


build_hash_index_2(text, hash_index)

for _ in range(n):
    l, r = [int(x) for x in input().split()]
    x = len(text)
    n = x * (l - 1) - ((l - 1) * l) // 2
    number = n + r - 1
    print(hash_index[number])
