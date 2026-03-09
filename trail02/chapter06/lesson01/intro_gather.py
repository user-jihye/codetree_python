"""
@see <https://www.codetree.ai/ko/trails/complete/curated-cards/intro-gather/description>
@problem <intro_gather>
"""
import sys

n = int(input())
people = list(map(int, input().split()))

min_move = sys.maxsize
for house in range(n):
    total_move = 0
    for i in range(n):
        total_move += abs(house-i) * people[i]
    min_move = min(min_move, total_move)

print(min_move)