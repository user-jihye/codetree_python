"""
@see <https://www.codetree.ai/ko/trails/complete/curated-cards/intro-area-of-non-overlapping-rectangle/description>
@problem <intro_area_of_non_overlapping_rectangle>
"""


checked = [[0] * 2001 for _ in range(2001)]
offset = 1000

# 직사각형 A, B
for _ in range(2):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1 + offset, x2 + offset):
        for j in range(y1 + offset, y2 + offset):
            checked[i][j] = 1

# 직사각형 M
x1, y1, x2, y2 = map(int, input().split())
for i in range(x1 + offset, x2 + offset):
    for j in range(y1 + offset, y2 + offset):
        checked[i][j] = 0

total = 0
for i in range(2001):
    for j in range(2001):
        total += checked[i][j]

print(total)