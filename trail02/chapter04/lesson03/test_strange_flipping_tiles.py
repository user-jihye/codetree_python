"""
@see <https://www.codetree.ai/ko/trails/complete/curated-cards/test-strange-flipping-tiles/description>
@problem <test_strange_flipping_tiles>
"""


n = int(input())
checked = [0] * 200001
cur = 100000
for _ in range(n):
    x, dir = input().split()
    x = int(x)

    # 왼쪽 -> 흰색 -> 1
    # 오른쪽 -> 검은색 -> 2
    if dir == 'L':
        for i in range(cur, cur - x, -1):
            checked[i] = 1
        cur = cur - x + 1

    elif dir == 'R':
        for i in range(cur, cur + x):
            checked[i] = 2
        cur = cur + x - 1

w = 0
b = 0
for color in checked:
    if color == 1:
        w += 1
    elif color == 2:
        b += 1

print(w, b)