"""
@see <https://www.codetree.ai/ko/trails/complete/curated-cards/intro-pair-parentheses-3/description>
@problem <intro_pair_parentheses_3>
"""


a = input()
cnt = 0
for l in range(len(a)):
    if a[l] == '(':
        for r in range(l, len(a)):
            if a[r] == ')':
                cnt += 1

print(cnt)