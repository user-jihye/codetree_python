"""
@see <https://www.codetree.ai/ko/trails/complete/curated-cards/intro-sum-from-1-to-a-certain-number-2/description>
@problem <intro_sum_from_1_to_a_certain_number_2>
"""


def func(n):
    if n == 1:
        return 1

    return func(n-1) + n


n = int(input())
print(func(n))