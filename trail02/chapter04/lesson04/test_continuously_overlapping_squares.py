"""
@see <https://www.codetree.ai/ko/trails/complete/curated-cards/test-continuously-overlapping-squares/description>
@problem <test_continuously_overlapping_squares>
"""

checked = [[0] * 300 for _ in range(300)]
offset = 100

n = int(input())
for i in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    for x in range(x1 + offset, x2 + offset):
        for y in range(y1 + offset, y2 + offset):
            checked[x][y] = i % 2

total = 0
for x in range(300):
    for y in range(300):
        if checked[x][y] == 1:
            total += 1

print(total)