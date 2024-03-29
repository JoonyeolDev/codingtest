# https://www.acmicpc.net/problem/18111
# 마인크래프트

# 문제
# lvalue는 세로 N, 가로 M 크기의 집터를 골랐다. 집터 맨 왼쪽 위의 좌표는 (0, 0)이다. 우리의 목적은 이 집터 내의 땅의 높이를 일정하게 바꾸는 것이다. 우리는 다음과 같은 두 종류의 작업을 할 수 있다.
# 좌표 (i, j)의 가장 위에 있는 블록을 제거하여 인벤토리에 넣는다.
# 인벤토리에서 블록 하나를 꺼내어 좌표 (i, j)의 가장 위에 있는 블록 위에 놓는다.
# 1번 작업은 2초가 걸리며, 2번 작업은 1초가 걸린다. 밤에는 무서운 몬스터들이 나오기 때문에 최대한 빨리 땅 고르기 작업을 마쳐야 한다. ‘땅 고르기’ 작업에 걸리는 최소 시간과 그 경우 땅의 높이를 출력하시오.
# 단, 집터 아래에 동굴 등 빈 공간은 존재하지 않으며, 집터 바깥에서 블록을 가져올 수 없다. 또한, 작업을 시작할 때 인벤토리에는 B개의 블록이 들어 있다. 땅의 높이는 256블록을 초과할 수 없으며, 음수가 될 수 없다.

# 입력
# 첫째 줄에 N, M, B가 주어진다. (1 ≤ M, N ≤ 500, 0 ≤ B ≤ 6.4 × 107)
# 둘째 줄부터 N개의 줄에 각각 M개의 정수로 땅의 높이가 주어진다. (i + 2)번째 줄의 (j + 1)번째 수는 좌표 (i, j)에서의 땅의 높이를 나타낸다. 땅의 높이는 256보다 작거나 같은 자연수 또는 0이다.

# 출력
# 첫째 줄에 땅을 고르는 데 걸리는 시간과 땅의 높이를 출력하시오. 답이 여러 개 있다면 그중에서 땅의 높이가 가장 높은 것을 출력하시오.

# 1차 수정 : 로직 변경
import sys
input = sys.stdin.readline
row, col, b = map(int, input().split())
min_num = 256
max_num = 0
arr = {}
for _ in range(row):
    temp_arr = list(map(int, input().split()))
    min_num = min(min(temp_arr),min_num)
    max_num = max(max(temp_arr),max_num)
    for num in temp_arr:
        arr[num] = arr.get(num, 0) + 1

times = []

for i in range(min_num, max_num+1):
    time = 0
    b_ = b
    for num, cnt in arr.items():
        gap = (num - i) * cnt
        if gap >= 0:
            time += gap * 2
            b_ += gap
        else:
            time -= gap
            b_ += gap
    if b_ >= 0:
        times.append((time, -i))
times.sort()
print(f'{times[0][0]} {-times[0][1]}')

# 31256KB, 148m, 692B


# 초기 코드 : 시간초과
import sys
input = sys.stdin.readline
row, col, b = map(int, input().split())
arr = []
min_num = 256
max_num = 0
for _ in range(row):
    temp_arr = list(map(int, input().split()))
    min_num = min(min(temp_arr),min_num)
    max_num = max(max(temp_arr),max_num)
    arr.extend(temp_arr)
left = min_num
right = max_num
times = []
for num in range(min_num, max_num+1):
    b_ = b
    sum_ = 0
    for i in arr:
        gap = i - num
        if gap >= 0:
            sum_ += gap*2
            b_ += gap
        else:
            sum_ -= gap
            b_ += gap
    if b_ >= 0:
        times.append((sum_, -num))
times.sort()
print(f'{times[0][0]} {-times[0][1]}')