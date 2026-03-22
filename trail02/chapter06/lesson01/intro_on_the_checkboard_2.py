"""
@see <https://www.codetree.ai/ko/trails/complete/curated-cards/intro-on-the-checkboard-2/description>
@problem <intro_on_the_checkboard_2>
"""


r, c = map(int, input().split())
arr = [input().split() for _ in range(r)]

cnt = 0
for x1 in range(1, r):
    for y1 in range(1, c):
        for x2 in range(x1+1, r-1):
            for y2 in range(y1+1, c-1):
                if arr[0][0] != arr[x1][y1] and arr[x1][y1] != arr[x2][y2] and arr[x2][y2] != arr[r-1][c-1]:
                    cnt += 1

print(cnt)