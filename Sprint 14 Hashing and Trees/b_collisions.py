from random import choices

alphabet = list('abcdefghijklmnopqrstuvwxyz')
Q = 1000
R = 123987123
WORD_LENGTH = 7  # >= 6


def polynom(q, R, text):
    if text:
        answer = ord(text[0])
        for item in text[1:]:
            answer = (answer * q + ord(item)) % R
        return answer % R
    return 0


result = dict()

while True:
    word = ''.join(choices(alphabet, k=WORD_LENGTH))
    polynom_hash = polynom(Q, R, word)
    if polynom_hash in result.keys() and word != result[polynom_hash]:
        print('hash of words', word, 'and', result[polynom_hash], 'is',
              polynom_hash)
        break
    result[polynom_hash] = word
