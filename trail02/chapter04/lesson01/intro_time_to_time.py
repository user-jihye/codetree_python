"""
@see <https://www.codetree.ai/ko/trails/complete/curated-cards/intro-time-to-time/description>
@problem <intro_time_to_time>
"""


start_h, start_m, end_h, end_m = map(int, input().split())

total = 0
while True:
    if start_h == end_h and start_m == end_m:
        break

    total += 1
    start_m += 1

    if start_m == 60:
        start_h += 1
        start_m = 0

print(total)