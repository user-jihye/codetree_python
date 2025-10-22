"""
@see <https://www.codetree.ai/ko/trails/complete/curated-cards/test-star-output-with-recursive-function-2/description>
@problem <test_star_output_with_recursive_function_2>
"""


def print_star(n):
    if n == 0:
        return

    print("* " * n)
    print_star(n - 1)
    print("* " * n)


n = int(input())
print_star(n)