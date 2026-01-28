"""
@see <https://www.codetree.ai/ko/trails/complete/curated-cards/intro-who-will-pay/description>
@problem <intro_who_will_pay>
"""


n, m, k = map(int, input().split())

score = [0] * (n+1)
pay = -1
for _ in range(m):
    score[int(input())] += 1

    if max(score) == k:
        pay = score.index(k)
        break

print(pay)