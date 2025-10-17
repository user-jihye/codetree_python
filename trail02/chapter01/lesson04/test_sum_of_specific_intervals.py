"""
@see <https://www.codetree.ai/ko/trails/complete/curated-cards/test-sum-of-specific-intervals/description>
"""

def result(a, b):
    sumVal = 0

    for i in range(a, b+1):
        sumVal += lst[i]

    return sumVal


n, m = map(int, input().split())
lst = [0] + list(map(int, input().split()))

for _ in range(m):
    a1, a2 = map(int, input().split())
    print(result(a1, a2))