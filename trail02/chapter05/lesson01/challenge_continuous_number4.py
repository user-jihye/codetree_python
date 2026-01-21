"""
@see <https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-continuous-number4/description>
@problem <challenge_continuous_number4>
"""


n = int(input())
arr = [int(input()) for _ in range(n)]

max_len = 0
l = 1

if len(arr) == 1:
    max_len = 1

for i in range(1, n):
    if arr[i] > arr[i-1]:
        l += 1
    else:
        l = 1
    max_len = max(max_len, l)

print(max_len)