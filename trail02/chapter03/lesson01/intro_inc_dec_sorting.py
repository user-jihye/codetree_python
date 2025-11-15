"""
@see <https://www.codetree.ai/ko/trails/complete/curated-cards/intro-inc-dec-sorting/description>
@problem <intro_inc_dec_sorting>
"""


n = int(input())
arr = list(map(int, input().split()))

arr.sort()
for x in arr:
    print(x, end=" ")
print()

arr.sort(reverse=True)
for x in arr:
    print(x, end=" ")