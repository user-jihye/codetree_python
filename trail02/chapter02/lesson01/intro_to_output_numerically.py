"""
@see <https://www.codetree.ai/ko/trails/complete/curated-cards/intro-to-output-numerically/description>
"""

"""
@see <intro_to_output_numerically>
"""


def asc(n):
    if n == 0:
        return

    asc(n - 1)
    print(n, end=' ')


def des(n):
    if n == 0:
        return

    print(n, end=' ')
    des(n - 1)


n = int(input())
asc(n)
print()
des(n)