"""
@see <https://www.codetree.ai/ko/trails/complete/curated-cards/intro-continuous-number2/introduction>
@problem <intro_continuous_number2>
"""


n = int(input())

max_cnt = 0
cnt = 0
before = -1
for _ in range(n):
    cur = int(input())

    if cur != before:
        max_cnt = max(max_cnt, cnt)
        cnt = 1

    else:
        cnt += 1

    before = cur

print(max(max_cnt, cnt))