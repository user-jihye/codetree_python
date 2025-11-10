"""
@see <https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-a-strange-sequence/description>
@problem <challenge_a_strange_sequence>
"""


def func(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2

    return func(n//3) + func(n-1)


n = int(input())
print(func(n))