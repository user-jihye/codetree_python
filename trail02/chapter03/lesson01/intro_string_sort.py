"""
@see <https://www.codetree.ai/ko/trails/complete/curated-cards/intro-string-sort/description>
@problem <intro_string_sort>
"""


str = input()

# 문자열은 str.sort() 불가능 -> 에러
# sorted(str) 가능 -> 리스트로 반환
sorted_arr = sorted(str)

# 리스트 -> 문자열로 합치기
sorted_str = "".join(sorted_arr)
print(sorted_str)