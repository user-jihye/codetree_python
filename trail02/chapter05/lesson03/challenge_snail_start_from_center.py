"""
@see <https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-snail-start-from-center/description>
@problem <challenge_snail_start_from_center>
"""


n = int(input())
arr = [[0] * n for _ in range(n)]

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
dir = 0
step = 1
'''
1칸 → 방향 전환
1칸 → 방향 전환
2칸 → 방향 전환
2칸 → 방향 전환
3칸 → 방향 전환
3칸 → 방향 전환
'''

x = y = n // 2
arr[x][y] = 1
num = 2

while num <= n * n:
    for _ in range(2):
        for _ in range(step):
            if num > n * n:
                break
            x += dx[dir]
            y += dy[dir]
            arr[x][y] = num
            num += 1
        dir = (dir + 1) % 4
    step += 1

for i in range(n):
    for j in range(n):
        print(arr[i][j], end=' ')
    print()