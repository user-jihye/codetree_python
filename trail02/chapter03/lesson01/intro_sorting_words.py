"""
@see <https://www.codetree.ai/ko/trails/complete/curated-cards/intro-sorting-words/description>
@problem <intro_sorting_words>
"""


n = int(input())
words = []
for _ in range(n):
    words.append(input())

words.sort()
for i in range(n):
    print(words[i])