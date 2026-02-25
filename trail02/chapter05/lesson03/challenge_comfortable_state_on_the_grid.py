"""
@see <https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-comfortable-state-on-the-grid/description>
@problem <challenge_comfortable_state_on_the_grid>
"""


n, m = map(int, input().split())
arr = [[0] * (n+1) for _ in range(n+1)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for _ in range(m):
    x, y = map(int, input().split())
    arr[x][y] = 1
    cnt = 0
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 1 <= nx <= n and 1 <= ny <= n and arr[nx][ny] == 1:
            cnt += 1
    if cnt == 3:
        print(1)  # 편안한 상태
    else:
        print(0)