"""
@see <https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-group-of-pairs/description>
@problem <challenge_group_of_pairs>
"""


n = int(input())
lst = list(map(int, input().split()))
lst.sort()

max_val = 0
for i in range(n):
    sum_val = lst[i] + lst[-(i + 1)]
    if max_val < sum_val:
        max_val = sum_val

print(max_val)