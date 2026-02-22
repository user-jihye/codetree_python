"""
@see <https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-come-back-2/description>
@problem <challenge_come_back_2>
"""
# 동, 남, 서, 북
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

commands = input()
x, y = 0, 0
dir = 3
time = 0
for c in commands:
    if c == 'R':
        dir = (dir + 1) % 4
    elif c == 'L':
        dir = (dir + 3) % 4
    elif c == 'F':
        x, y = x + dx[dir], y + dy[dir]

    time += 1

    if x == 0 and y == 0:
        print(time)
        exit()

print(-1)