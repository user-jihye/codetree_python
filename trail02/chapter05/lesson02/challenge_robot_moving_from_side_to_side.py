"""
@see <https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-robot-moving-from-side-to-side/description>
@problem <challenge_robot_moving_from_side_to_side>
"""
def simulate(cnt):
    arr = [0]
    for _ in range(cnt):
        t, d = input().split()
        t = int(t)
        if d == 'R':
            for _ in range(t):
                arr.append(arr[-1] + 1)

        elif d == 'L':
            for _ in range(t):
                arr.append(arr[-1] - 1)

    return arr


n, m = map(int, input().split())
a = simulate(n)
b = simulate(m)

last = max(len(a), len(b))
while len(a) < last:
    a.append(a[-1])
while len(b) < last:
    b.append(b[-1])

cnt = 0
for i in range(1, last):
    if a[i] == b[i] and a[i-1] != b[i-1]:
        cnt += 1

print(cnt)