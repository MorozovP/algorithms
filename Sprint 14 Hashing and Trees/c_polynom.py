import array

def polinom(base, modulo, sequence):
    hash_index = [0]
    base_powers = array.array('I', [1])
    if sequence:
        for j in range(len(sequence)):
            hash_index.append((hash_index[j] * base + sequence[j]) % modulo)
            base_powers.append((base_powers[j] * base) % modulo)
    return hash_index, base_powers


def get_hash(start, end, hash_index, base_power, modulo):
    if start == 0:
        return hash_index[end]
    return (hash_index[end] - hash_index[start] * base_power) % modulo


def read_input():
    base = int(input())
    modulo = int(input())
    sequence = [ord(x) for x in input()]
    n = int(input())
    return base, modulo, sequence, n


def main():
    base, modulo, sequence, n = read_input()
    hash_index, base_powers = polinom(base, modulo, sequence)
    for _ in range(n):
        l, r = [int(x) for x in input().split()]
        print(get_hash(l-1, r, hash_index, base_powers[r-l+1], modulo))


if __name__ == '__main__':
    main()

