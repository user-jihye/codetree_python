"""
@see <https://www.codetree.ai/ko/trails/complete/curated-cards/intro-small-marble-movement/description>
@problem <intro_small_marble_movement>
"""


def in_range(x, y, n):
    return 0 <= x < n and 0 <= y < n


n, t = map(int, input().split())
r, c, d = input().split()

dir = {
    'U': 0,
    'D': 3,
    'R': 1,
    'L': 2
}
dx = [-1, 0, 0, 1]
dy = [0, 1, -1, 0]

x, y = int(r) - 1, int(c) - 1
d = dir[d]

time = 1
while time <= t:
    nx, ny = x + dx[d], y + dy[d]
    if not in_range(nx, ny, n):
        d = 3 - d
    else:
        x, y = nx, ny

    time += 1

print(x+1, y+1)