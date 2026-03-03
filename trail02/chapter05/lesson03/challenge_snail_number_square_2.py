"""
@see <https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-snail-number-square-2/description>
@problem <challenge_snail_number_square_2>
"""


n, m = map(int, input().split())
arr = [[0] * m for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

dir = 0
x, y = 0, 0
arr[x][y] = 1
while arr[x][y] < n * m:
    nx, ny = x + dx[dir], y + dy[dir]
    if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 0:
        arr[nx][ny] = arr[x][y] + 1
        x, y = nx, ny
    else:
        dir = (dir + 1) % 4

for x in range(n):
    for y in range(m):
        print(arr[x][y], end=' ')
    print()