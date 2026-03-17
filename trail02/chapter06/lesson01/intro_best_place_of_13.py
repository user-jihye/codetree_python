"""
@see <https://www.codetree.ai/ko/trails/complete/curated-cards/intro-best-place-of-13/description>
@problem <intro_best_place_of_13>
"""


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

max_cnt = 0
for i in range(n):
    for j in range(n - 2):
        max_cnt = max(max_cnt, arr[i][j] + arr[i][j+1] + arr[i][j+2])

print(max_cnt)