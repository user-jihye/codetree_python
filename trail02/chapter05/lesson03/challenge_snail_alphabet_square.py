"""
@see <https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-snail-alphabet-square/description>
@problem <challenge_snail_alphabet_square>
"""


n, m = map(int, input().split())
arr = [[0] * m for _ in range(n)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
dir = 0
x, y = 0, 0
arr[x][y] = 65

for _ in range(n * m - 1):
    nx, ny = x + dx[dir], y + dy[dir]
    if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 0:
        arr[nx][ny] = arr[x][y] + 1
        x, y = nx, ny
    else:
        dir = (dir + 1) % 4
        nx, ny = x + dx[dir], y + dy[dir]
        arr[nx][ny] = arr[x][y] + 1
        x, y = nx, ny

for i in range(n):
    for j in range(m):
        num = (arr[i][j] - 65) % 26 + 65
        print(chr(num), end=' ')
    print()