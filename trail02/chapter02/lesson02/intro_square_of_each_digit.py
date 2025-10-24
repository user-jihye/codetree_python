"""
@see <https://www.codetree.ai/ko/trails/complete/curated-cards/intro-square-of-each-digit/description>
@problem <intro_square_of_each_digit>
"""
def func(n):
    if n < 10:
        return n ** 2

    return func(n // 10) + (n % 10) ** 2


n = int(input())
print(func(n))