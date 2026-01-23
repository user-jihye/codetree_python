"""
@see <https://www.codetree.ai/ko/trails/complete/curated-cards/test-subsequence-above-t/description>
@problem <test_subsequence_above_t>
"""


n, t = map(int, input().split())
arr = list(map(int, input().split()))

ans, l = 0, 0
for i in range(n):
    if arr[i] > t:
        l += 1
    else:
        l = 0

    ans = max(ans, l)

print(ans)