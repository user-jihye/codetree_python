"""
@see <https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-the-total-area-of-colored-paper/description>
@problem <challenge_the_total_area_of_colored_paper>
"""


n = int(input())
offset = 100
checked = [[0] * 201 for _ in range(201)]
for _ in range(n):
    x, y = map(int, input().split())
    for i in range(x + offset, x + offset + 8):
        for j in range(y + offset, y + offset + 8):
            checked[i][j] = 1

total = 0
for i in range(0, 201):
    for j in range(0, 201):
        total += checked[i][j]

print(total)