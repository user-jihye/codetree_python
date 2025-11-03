"""
@see <https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-sum-of-large-numeric-digits/description>
@problem <challenge_sum_of_large_numeric_digits>
"""

def func(x):
    if x < 10:
        return x

    return func(x // 10) + (x % 10)


a, b, c = map(int, input().split())
print(func(a * b * c))