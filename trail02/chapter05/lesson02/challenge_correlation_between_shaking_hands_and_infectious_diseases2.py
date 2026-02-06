"""
@see <https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-correlation-between-shaking-hands-and-infectious-diseases2/description>
@problem <challenge_correlation_between_shaking_hands_and_infectious_diseases2>
"""


# N: 개발자 수
# K: 감염 후 K번 동안만 전염병 옮김
# P: 처음 병걸린 사람 번호
# T: 악수 횟수
# t초에 x와 y가 악수
# 최종 감염여부 출력

N, K, P, T = map(int, input().split())
handshakes = [tuple(map(int, input().split())) for _ in range(T)]
handshakes.sort()

shake_num = [0] * (N+1)
infected = [False] * (N+1)

infected[P] = True

for t, x, y in handshakes:
    # 감염되어 있을 경우 -> 악수 횟수 증가
    if infected[x]:
        shake_num[x] += 1
    if infected[y]:
        shake_num[y] += 1

    # x가 감염되어 있고, k번 이하로 악수했다면 -> y전염
    if infected[x] and shake_num[x] <= K:
        infected[y] = True

    # y가 감염되어 있고, k번 이하로 악수했다면 -> x전염
    if infected[y] and shake_num[y] <= K:
        infected[x] = True


for i in range(1, N+1):
    if infected[i]:
        print(1, end='')
    else:
        print(0, end='')