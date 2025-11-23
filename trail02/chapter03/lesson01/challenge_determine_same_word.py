"""
@see <https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-determine-same-word/description>
@problem <challenge_determine_same_word>
"""


str1 = input()
str2 = input()

# 문자열은 sort() 사용 불가
# 1. 리스트로 만든 후 -> 리스트.sort()
# 2. sorted(문자열) -> 리스트로 반환
sorted_str1 = sorted(str1)
sorted_str2 = sorted(str2)

if sorted_str1 == sorted_str2:
    print("Yes")
else:
    print("No")