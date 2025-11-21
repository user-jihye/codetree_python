"""
@see <https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-two-equal-series/description>
@problem <challenge_two_equal_series>
"""


n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()

if (A == B):
    print("Yes")
else:
    print("No")