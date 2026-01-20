"""
@see <https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-continuous-number3/description>
@problem <challenge_continuous_number3>
"""


n = int(input())
arr = [int(input()) for _ in range(n)]

ans, cnt = 0, 1
for i in range(1, n):
    if arr[i-1] * arr[i] > 0:
        cnt += 1
    elif arr[i-1] * arr[i] < 0:
        ans = max(cnt, ans)
        cnt = 1

print(max(cnt, ans))


