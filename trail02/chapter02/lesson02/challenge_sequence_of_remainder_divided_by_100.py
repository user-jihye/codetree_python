"""
@see <https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-sequence-of-remainder-divided-by-100/description>
@problem <challenge_sequence_of_remainder_divided_by_100>
"""
def func(n):
    if n == 1:
        return 2
    elif n == 2:
        return 4

    return func(n-2) * func(n-1) % 100


n = int(input())
print(func(n))