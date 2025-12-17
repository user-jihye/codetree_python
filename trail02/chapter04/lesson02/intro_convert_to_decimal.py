"""
@see <https://www.codetree.ai/ko/trails/complete/curated-cards/intro-convert-to-decimal/description>
@problem <intro_convert_to_decimal>
"""


binary = list(map(int, input()))

decimal = 0
power = 0
for i in range(len(binary)-1, -1, -1):
    decimal += binary[i] * (2 ** power)
    power += 1

print(decimal)