"""
@see <https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-divide-and-subtract-and-add-up/description>
"""

# 홀수 -> -1
# 짝수 -> /2

def div_diff_sum(m):
    sumVal = 0

    while m:
        sumVal += lst[m]

        if m % 2 == 1:
            m -= 1
        else:
            m //= 2

    return sumVal


n, m = map(int, input().split())
lst = [0] + list(map(int, input().split()))
print(div_diff_sum(m))


