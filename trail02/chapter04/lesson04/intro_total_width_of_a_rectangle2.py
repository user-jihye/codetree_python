"""
@see <https://www.codetree.ai/ko/trails/complete/curated-cards/intro-total-width-of-a-rectangle2/description>
@problem <intro_total_width_of_a_rectangle2>
"""


n = int(input())
offset = 100
arr = [[0] * 200 for _ in range(200)]
for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            arr[i][j] = 1

total = 0
for x in range(200):
    for y in range(200):
        if arr[x][y] == 1:
            total += 1

print(total)