"""
@see <https://www.codetree.ai/ko/trails/complete/curated-cards/test-the-day-of-the-day/description>
@problem <test_the_day_of_the_day>
"""


m1, d1, m2, d2 = map(int, input().split())
A = input()
#           1   2   3   4   5   6   7   8   9  10  11   12
month = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def num_of_days(m, d):
    total_days = 0

    # 1월 ~ (m-1)월 까지 몇일 있는지 더하기
    for i in range(1, m):
        total_days += month[i]

    # m월 몇일 있는지 더하기
    total_days += d

    return total_days


num_of_day = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
cur_day = 0
cnt = 0

start_date = num_of_days(m1, d1)
end_date = num_of_days(m2, d2)

for date in range(start_date, end_date + 1):
    if cur_day == num_of_day.index(A):
        cnt += 1

    cur_day = (cur_day + 1) % 7

print(cnt)