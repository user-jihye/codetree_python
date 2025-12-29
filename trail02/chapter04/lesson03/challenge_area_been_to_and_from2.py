"""
@see <https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-area-been-to-and-from2/description>
@problem <challenge_area_been_to_and_from2>
"""


n = int(input())

offset = 1000
checked = [0] * 2001
curr = 1000

for _ in range(n):
    xi, dir = input().split()
    xi = int(xi)

    if dir == 'R':
        for i in range(curr, curr + xi):
            checked[i] += 1
        curr += xi

    else:
        for i in range(curr - xi, curr):
            checked[i] += 1
        curr -= xi

cnt = 0
for elem in checked:
    if elem >= 2:
        cnt += 1

print(cnt)