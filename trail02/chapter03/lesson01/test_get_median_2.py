"""
@see <https://www.codetree.ai/ko/trails/complete/curated-cards/test-get-median-2/description>
@problem <test_get_median_2>
"""


n = int(input())
arr = list(map(int, input().split()))
lst = []

for i in range(n):
    lst.append(arr[i])

    if i % 2 == 0:
        lst.sort()
        print(lst[i//2], end=" ")