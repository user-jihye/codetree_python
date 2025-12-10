"""
@see <https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-guess-day-of-week/description>
@problem <challenge_guess_day_of_week>
"""


m1, d1, m2, d2 = map(int, input().split())
#           1   2   3   4   5   6   7   8   9  10  11   12
month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
week_of_day = {1: 'Mon', 2: 'Tue', 3: 'Wed', 4:'Thu', 5: 'Fri', 6:'Sat', 7: 'Sun'}
curr = 1

if (m1 > m2) or (m1 == m2 and d1 > d2):
    while True:
        if m1 == m2 and d1 == d2:
            break

        curr -= 1
        d1 -= 1

        if curr == 0:
            curr = 7
        if d1 == 0:
            m1 -= 1
            d1 = month[m1]

else:
    while True:
        if m1 == m2 and d1 == d2:
            break

        curr += 1
        d1 += 1

        if curr == 8:
            curr = 1
        if d1 == month[m1]:
            m1 += 1
            d1 = 0

print(week_of_day[curr])