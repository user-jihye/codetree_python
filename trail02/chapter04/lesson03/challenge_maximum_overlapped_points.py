"""
@see <https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-maximum-overlapped-points/description>
@problem <challenge_maximum_overlapped_points>
"""


n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

lst = [0] * 101
for x1, x2 in segments:
    for idx in range(x1, x2+1):
        lst[idx] += 1

print(max(lst))