"""
@see <https://www.codetree.ai/ko/trails/complete/curated-cards/intro-fibonacci-using-recursive-function/description>
@problem <intro_fibonacci_using_recursive_function>
"""


def fibo(n):

    if n == 1 or n == 2:
        return 1

    return fibo(n-1) + fibo(n-2)


n = int(input())
print(fibo(n))