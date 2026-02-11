"""
@see <https://www.codetree.ai/ko/trails/complete/curated-cards/intro-text-based-commands2/description>
@problem <intro_text_based_commands2>
"""


x, y = 0, 0
now = 3
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

directions = input()
for dir in directions:
    if dir == 'R':
        now = (now + 1) % 4

    elif dir == 'L':
        now = (now + 3) % 4

    elif dir == 'F':
        x += dx[now]
        y += dy[now]

print(x, y)