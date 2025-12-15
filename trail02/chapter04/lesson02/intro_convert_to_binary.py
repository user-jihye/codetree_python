"""
@see <https://www.codetree.ai/ko/trails/complete/curated-cards/intro-convert-to-binary/description>
@problem <intro_convert_to_binary>
"""


n = int(input())
digits = []

while True:
    if n < 2:
        digits.append(n)
        break

    digits.append(n % 2)
    n //= 2

for x in digits[::-1]:
    print(x, end="")