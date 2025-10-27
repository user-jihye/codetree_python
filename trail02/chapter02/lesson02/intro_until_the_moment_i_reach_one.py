"""
@see <https://www.codetree.ai/ko/trails/complete/curated-cards/intro-until-the-moment-I-reach-one/description>
@problem <intro_until_the_moment_i_reach_one>
"""


def func(n, cnt):
    if n == 1:
        return cnt

    cnt += 1
    if n % 2 == 0:
        return func(n//2, cnt)
    else:
        return func(n//3, cnt)


n = int(input())
print(func(n, 0))