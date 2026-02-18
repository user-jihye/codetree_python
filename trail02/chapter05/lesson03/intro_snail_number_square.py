"""
@see <https://www.codetree.ai/ko/trails/complete/curated-cards/intro-snail-number-square/description>
@problem <intro_snail_number_square>
"""


def in_range(n, m, x, y):
    return 0 <= x < n and 0 <= y < m


n, m = map(int, input().split())
arr = list([0] * m for _ in range(n))

# 오른쪽, 아래쪽, 왼쪽, 위쪽
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

dir = 0
x, y = 0, 0
arr[x][y] = 1
for num in range(2, n*m+1):
    nx, ny = x + dx[dir], y + dy[dir]

    if not in_range(n, m, nx, ny) or arr[nx][ny] != 0:
        dir = (dir + 1) % 4

    x, y = x + dx[dir], y + dy[dir]
    arr[x][y] = num

for i in range(n):
    for j in range(m):
        print(arr[i][j], end = ' ')
    print()
