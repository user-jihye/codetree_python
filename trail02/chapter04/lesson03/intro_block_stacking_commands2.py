"""
@see <https://www.codetree.ai/ko/trails/complete/curated-cards/intro-block-stacking-commands2/description>
@problem <intro_block_stacking_commands2>
"""

n, k = map(int, input().split())
blocks = [0] * (n + 1)
for _ in range(k):
    a, b = map(int, input().split())

    for i in range(a, b + 1):
        blocks[i] += 1

print(max(blocks))
