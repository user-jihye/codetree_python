"""
@see <https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-keep-the-lead/description>
@problem <challenge_keep_the_lead>
"""
def result(arr, cnt):
    cur_t = 0
    for _ in range(cnt):
        v, t = map(int, input().split())
        for _ in range(t):
            cur_t += 1
            arr[cur_t] = arr[cur_t - 1] + v


n, m = map(int, input().split())
a = [0] * 1000001
result(a, n)
b = [0] * 1000001
result(b, m)

start = 1
leader = 0
cnt = 0
while a[start] != 0:
    if a[start] > b[start]:
        if leader == 2:
            cnt += 1

        leader = 1

    elif a[start] < b[start]:
        if leader == 1:
            cnt += 1

        leader = 2

    start += 1

print(cnt)