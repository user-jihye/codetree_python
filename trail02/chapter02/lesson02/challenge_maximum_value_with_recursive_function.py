"""
@see <https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-maximum-value-with-recursive-function/description>
@problem <challenge_maximum_value_with_recursive_function>
"""


def find_max(n, idx, arr, max_val):
    if idx == n:
        return max_val

    if arr[idx] > max_val:
        max_val = arr[idx]

    return find_max(n, idx + 1, arr, max_val)


n = int(input())
arr = list(map(int, input().split()))
print(find_max(n, 0, arr, 0))
