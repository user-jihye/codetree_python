"""
@see <https://www.codetree.ai/ko/trails/complete/curated-cards/intro-the-moment-we-meet/description>
@problem <intro_the_moment_we_meet>
"""


def result(arr, cnt):
    cur = 1
    for _ in range(cnt):
        dir, time = input().split()

        if dir == 'R':
            for _ in range(int(time)):
                arr[cur] = arr[cur-1] + 1
                cur += 1
        else:
            for _ in range(int(time)):
                arr[cur] = arr[cur-1] - 1
                cur += 1

    return cur


n, m = map(int, input().split())

a = [0] * 1000001
b = [0] * 1000001

time1 = result(a, n)
time2 = result(b, m)

ans = -1
for i in range(1, time1):
    if a[i] == b[i]:
        ans = i
        break

print(ans)