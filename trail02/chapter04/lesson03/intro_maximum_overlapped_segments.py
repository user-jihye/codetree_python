"""
@see <https://www.codetree.ai/ko/trails/complete/curated-cards/intro-maximum-overlapped-segments/description>
@problem <intro_maximum_overlapped_segments>
"""


# 지점 =! 구간
# 구간: [x1, x2] -> x1 부터 x2-1까지 표시해 주면 됨

n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

offset = 0
for x1, x2 in segments:
    if x1 < 0:
        tmp = abs(x1)
        offset = tmp if tmp > offset else offset
    if x2 < 0:
        tmp = abs(x2)
        offset = tmp if tmp > offset else offset

lst = [0] * 201
for x1, x2 in segments:
    for i in range(x1 + offset, x2 + offset):
        lst[i] += 1

print(max(lst))