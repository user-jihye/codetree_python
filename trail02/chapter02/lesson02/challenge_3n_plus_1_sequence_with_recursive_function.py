"""
@see <https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-3n-plus-1-sequence-with-recursive-function/description>
@problem <challenge_3n_plus_1_sequence_with_recursive_function>
"""


def func(n, cnt):
    if n == 1:
        return cnt

    if n % 2 == 0:
        return func(n / 2, cnt + 1)
    else:
        return func(n * 3 + 1, cnt + 1)


n = int(input())
print(func(n, 0))