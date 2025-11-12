"""
@see <https://www.codetree.ai/ko/trails/complete/curated-cards/test-least-common-multiple-using-recursive-function/description>
@problem <test_least_common_multiple_using_recursive_function>
"""
# 두 수 간의 최소공배수 구하기
def lcm(a, b):
    x = 1  # 공약수
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            x = i

    return a * b // x
    # return (a // x) * (b // x) * x


def get_lcm_all(n):
    if n == 1:
        return arr[1]

    return lcm(get_lcm_all(n-1), arr[n])


n = int(input())
arr = [0] + list(map(int, input().split()))

print(get_lcm_all(n))