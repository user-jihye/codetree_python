"""
@see <https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-minimum-area-of-rectangle-to-cover-debris/description>
@problem <challenge_minimum_area_of_rectangle_to_cover_debris>
"""


checked = [[0] * 3000 for _ in range(3000)]
offset = 1000

x1, y1, x2, y2 = map(int, input().split())
for i in range(x1 + offset, x2 + offset):
    for j in range(y1 + offset, y2 + offset):
        checked[i][j] = 1

nx1, ny1, nx2, ny2 = map(int, input().split())
for i in range(nx1 + offset, nx2 + offset):
    for j in range(ny1 + offset, ny2 + offset):
        checked[i][j] = 0

min_x, max_x = 3000, -1
min_y, max_y = 3000, -1

for i in range(x1 + offset, x2 + offset):
    for j in range(y1 + offset, y2 + offset):
        if checked[i][j] == 1:
            min_x = min(min_x, i)
            max_x = max(max_x, i)
            min_y = min(min_y, j)
            max_y = max(max_y, j)

if max_x == -1 or max_y == -1:
    print(0)
else:
    print((max_x - min_x + 1) * (max_y - min_y + 1))