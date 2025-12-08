"""
@see <https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-datetime-to-datetime/description>
@problem <challenge_datetime_to_datetime>
"""


day, hour, minute = map(int, input().split())

cur_day, cur_hour, cur_minute = 11, 11, 11

if (day < 11) or (day == 11 and hour < 11) or (day == 11 and hour == 11 and minute < 11):
    print(-1)
    exit()

total = 0
while True:
    if cur_day == day and cur_hour == hour and cur_minute == minute:
        break

    cur_minute += 1
    total += 1
    if cur_minute == 60:
        cur_hour += 1
        cur_minute = 0
        if cur_hour == 24:
            cur_day += 1
            cur_hour = 0

print(total)