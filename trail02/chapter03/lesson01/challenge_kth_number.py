"""
@see <https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-kth-number/description>
@problem <challenge_kth_number>
"""


n, k = map(int, input().split())
nums = list(map(int, input().split()))

nums.sort()
print(nums[k-1])