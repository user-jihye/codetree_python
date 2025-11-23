"""
@see <https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-kth-special-string/description>
@problem <challenge_kth_special_string>
"""


n, k, t = input().split()
n, k = int(n), int(k)

t_len = len(t)
words = []
for _ in range(n):
    word = input()
    if word[0:t_len] == t:
        words.append(word)

words.sort()
print(words[k-1])