"""
@see <https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-3n-plus-1-sequence-with-recursive-function/description>
@problem <challenge_3n_plus_1_sequence_with_recursive_function>
"""


def func(n):
    if n == 1:
        return 0

    if n % 2 == 0:
        return func(n / 2) + 1
    else:
        return func(n * 3 + 1) + 1


n = int(input())
print(func(n))