"""
@see <https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-painting-white-black/description>
@problem <challenge_painting_white_black>
"""


# 왼쪽 -> 흰색
# 오른쪽 -> 검은색
checked = [[0, 0, 'n'] for _ in range(200001)]
cur = 100000

n = int(input())
for _ in range(n):
    dx, dir = input().split()
    dx = int(dx)

    if dir == 'R':
        for i in range(cur, cur + dx):
            if checked[i][2] == 'g':
                continue

            checked[i][1] += 1

            if checked[i][0] >= 2 and checked[i][1] >= 2:
                checked[i][2] = 'g'
            else:
                checked[i][2] = 'b'
        cur = cur + dx - 1

    else:
        for i in range(cur, cur - dx, -1):
            if checked[i][2] == 'g':
                continue

            checked[i][0] += 1

            if checked[i][0] >= 2 and checked[i][1] >= 2:
                checked[i][2] = 'g'
            else:
                checked[i][2] = 'w'
        cur = cur - dx + 1

white = 0
black = 0
gray = 0
for w_cnt, b_cnt, color in checked:
    if color == 'w':
        white += 1
    elif color == 'b':
        black += 1
    elif color == 'g':
        gray += 1

print(white, black, gray)