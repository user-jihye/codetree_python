"""
@see <https://www.codetree.ai/ko/trails/complete/curated-cards/intro-move-in-direction/description>
@problem <intro_move_in_direction>
"""


n = int(input())
x, y = 0, 0
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]
dir = {'W': 0, 'S': 1, 'N': 2, 'E': 3}
for _ in range(n):
    direction, distance = input().split()
    distance = int(distance)
    x += dx[dir[direction]] * distance
    y += dy[dir[direction]] * distance

print(x, y)