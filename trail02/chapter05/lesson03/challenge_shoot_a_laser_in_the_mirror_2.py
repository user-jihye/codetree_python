"""
@see <https://www.codetree.ai/ko/trails/complete/curated-cards/challenge-shoot-a-laser-in-the-mirror-2/description>
@problem <challenge_shoot_a_laser_in_the_mirror_2>
"""

# 주어진 숫자에 따라 시작 위치와 방향 구하기
def initialize(num):
    if num <= n:
        return 0, num - 1, 0
    elif num <= 2 * n:
        return num - n - 1, n - 1, 1
    elif num <= 3 * n:
        return n - 1, n - (num - 2 * n), 2
    else:
        return n - (num - 3 * n), 0, 3


def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


# (x, y)에서 시작하여 next_dir 방향으로 이동한 이후의 위치 반환
def move(x, y, next_dir):
    # 0: ↓, 1: ←, 2: ↑, 3: ←
    dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]
    nx, ny = x + dx[next_dir], y + dy[next_dir]
    return nx, ny, next_dir


def simulate(x, y, move_dir):
    move_num = 0
    while in_range(x, y):
        # 0 <-> 1 / 2 <-> 3
        if arr[x][y] == '/':
            x, y, move_dir = move(x, y, move_dir ^ 1)
        # 0 <-> 3 \ 1 <-> 2
        else:
            x, y, move_dir = move(x, y, 3 - move_dir)

        move_num += 1

    return move_num


n = int(input())
arr = [
    input() for _ in range(n)
]
start_num = int(input())

# 시작 위치와 방향
x, y, move_dir = initialize(start_num)
# 시뮬레이션
move_num = simulate(x, y, move_dir)
print(move_num)