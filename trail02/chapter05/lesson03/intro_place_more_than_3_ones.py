"""
@see <https://www.codetree.ai/ko/trails/complete/curated-cards/intro-place-more-than-3-ones/description>
@problem <intro_place_more_than_3_ones>
"""


def in_range(n, x, y):
    return 0 <= x < n and 0 <= y < n


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

dxs = [0, 0, -1, 1]
dys = [-1, 1, 0, 0]

result = 0
for i in range(n):
    for j in range(n):
        cnt = 0
        for dx, dy in zip(dxs, dys):
            nx, ny = i + dx, j + dy
            if in_range(n, nx, ny) and arr[nx][ny] == 1:
                cnt += 1

        if cnt >= 3:
            result += 1

print(result)