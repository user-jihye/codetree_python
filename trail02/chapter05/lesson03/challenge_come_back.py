"""
@see <https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-come-back/description>
@problem <challenge_come_back>
"""


n = int(input())

# 0: W, 1: S, 2: N, 3: E
move = {
    'W': [0, -1],
    'S': [1, 0],
    'N': [-1, 0],
    'E': [0, 1]
}

x, y = 0, 0
time = 0
for _ in range(n):
    dir, cnt = input().split()
    cnt = int(cnt)
    for _ in range(cnt):
        x = x + move[dir][0]
        y = y + move[dir][1]
        time += 1

        if x == 0 and y == 0:
            print(time)
            exit()

print(-1)
