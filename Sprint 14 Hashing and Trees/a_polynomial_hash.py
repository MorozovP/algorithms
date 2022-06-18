"""
h(s)=((((s1 * q + s2) * q + s3) * q + ⋯ + sn−1)q + sn) modR.
R и q — выбранные константы. Для беззнаковых 4-байтовых целых чисел удобно
выбрать R=2^32. Для 8-байтовых чисел можно взять R=2^64.
В качестве q обычно берут какое-нибудь большое простое число. Например, часто
используют число q = 1 000 000 007 = 10^9 + 7, потому что оно большое, но всё
ещё меньше, чем 2^32, и его легко запомнить.
"""

q = int(input())
R = int(input())
text = input()


def polinom(q, R, text):
    if text:
        answer = ord(text[0])
        for item in text[1:]:
            answer = (answer * q + ord(item)) % R
        return answer % R
    return 0


print(polinom(q, R, text))
