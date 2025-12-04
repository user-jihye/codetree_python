"""
@see <https://www.codetree.ai/ko/trails/complete/curated-cards/intro-date-to-date/description>
@problem <intro_date_to_date>
"""


start_month, start_day, end_month, end_day = map(int, input().split())
#                 1   2   3   4   5   6   7   8   9   10   11   12
num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

total = 0
while True:
    if start_month == end_month and start_day == end_day:
        break

    total += 1
    start_day += 1

    if start_day > num_of_days[start_month]:
        start_month += 1
        start_day = 1

print(total + 1)