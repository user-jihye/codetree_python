"""
@see <https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-star-output-with-recursive-function/description>
@problem <challenge_star_output_with_recursive_function>
"""


def print_star(n):
    if n == 0:
        return

    print_star(n - 1)
    print("*" * n)


n = int(input())
print_star(n)