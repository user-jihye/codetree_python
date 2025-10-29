"""
@see <https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-output-value-based-on-odd-even-numbers/description>
@problem <challenge_output_value_based_on_odd_even_numbers>
"""


def sum_val(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2

    return n + sum_val(n-2)


n = int(input())
print(sum_val(n))