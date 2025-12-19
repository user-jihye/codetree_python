"""
@see <https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-decimal-and-binary-number-2/description>
@problem <challenge_decimal_and_binary_number_2>
"""

def binary_to_decimal(binary):
    decimal = 0
    power = 0
    for i in range(len(binary) - 1, -1, -1):
        decimal += binary[i] * (2 ** power)
        power += 1

    return decimal * 17


def decimal_to_binary(decimal):
    temp = []
    while decimal > 0:
        temp.append(decimal % 2)
        decimal //= 2

    return ''.join(map(str, temp[::-1]))


lst = list(map(int, input()))
a = binary_to_decimal(lst)
b = decimal_to_binary(a)
print(b)