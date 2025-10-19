"""
@see <https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-the-flower-of-the-recursive-function/description>
@problem <challenge_the_flower_of_the_recursive_function>
"""


def print_num(n):
    if n == 0:
        return

    print(n, end=" ")
    print_num(n - 1)
    print(n, end=" ")


n = int(input())
print_num(n)