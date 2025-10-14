"""
@see <https://www.codetree.ai/ko/trails/complete/curated-cards/intro-find-the-location-of-a-substring-using-a-function/description>
"""

def find_start_idx(text, pattern):
    n = len(text)
    m = len(pattern)

    for i in range(n - m + 1):
        if text[i] == pattern[0]:
            is_find = True
            for j in range(m):
                if text[i + j] != pattern[j]:
                    is_find = False
                    break

            if is_find:
                return i

    return -1


text = input()
pattern = input()
print(find_start_idx(text, pattern))


