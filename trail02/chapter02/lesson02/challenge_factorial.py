"""
@see <https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-factorial/description>
@problem <challenge_factorial>
"""


def fec(n):
    if n == 0:
        return 1

    return n * fec(n-1)


n = int(input())
print(fec(n))