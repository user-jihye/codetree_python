"""
@see <https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-awkward-digits-2/description>
@problem <challenge_awkward_digits_2>
"""


a = list(map(int, input()))
l = len(a)

ans = 0
for i in range(l):
    # i번째 자리 바꾸기
    a[i] = 1 - a[i]

    # 십진수 변환
    num = 0
    for j in range(l):
        num = num * 2 + a[j]

    ans = max(ans, num)

    # i번째 자리 원래대로 돌려놓기
    a[i] = 1 - a[i]

print(ans)