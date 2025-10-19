"""
@see <https://www.codetree.ai/ko/trails/complete/curated-cards/intro-repeated-output-2/description>
"""

"""
@see <intro_repeated_output_2>
"""


def print_str(n):
    if n == 0:
        return

    print_str(n-1)
    print("HelloWorld")


n = int(input())
print_str(n)
