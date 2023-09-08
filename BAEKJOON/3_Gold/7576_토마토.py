# https://www.acmicpc.net/problem/7576
# 토마토

# 문제
# 철수의 토마토 농장에서는 토마토를 보관하는 큰 창고를 가지고 있다. 토마토는 아래의 그림과 같이 격자 모양 상자의 칸에 하나씩 넣어서 창고에 보관한다. 
# 창고에 보관되는 토마토들 중에는 잘 익은 것도 있지만, 아직 익지 않은 토마토들도 있을 수 있다. 보관 후 하루가 지나면, 익은 토마토들의 인접한 곳에 있는 익지 않은 토마토들은 익은 토마토의 영향을 받아 익게 된다. 하나의 토마토의 인접한 곳은 왼쪽, 오른쪽, 앞, 뒤 네 방향에 있는 토마토를 의미한다. 대각선 방향에 있는 토마토들에게는 영향을 주지 못하며, 토마토가 혼자 저절로 익는 경우는 없다고 가정한다. 철수는 창고에 보관된 토마토들이 며칠이 지나면 다 익게 되는지, 그 최소 일수를 알고 싶어 한다.
# 토마토를 창고에 보관하는 격자모양의 상자들의 크기와 익은 토마토들과 익지 않은 토마토들의 정보가 주어졌을 때, 며칠이 지나면 토마토들이 모두 익는지, 그 최소 일수를 구하는 프로그램을 작성하라. 단, 상자의 일부 칸에는 토마토가 들어있지 않을 수도 있다.

# 입력
# 첫 줄에는 상자의 크기를 나타내는 두 정수 M,N이 주어진다. M은 상자의 가로 칸의 수, N은 상자의 세로 칸의 수를 나타낸다. 단, 2 ≤ M,N ≤ 1,000 이다. 둘째 줄부터는 하나의 상자에 저장된 토마토들의 정보가 주어진다. 즉, 둘째 줄부터 N개의 줄에는 상자에 담긴 토마토의 정보가 주어진다. 하나의 줄에는 상자 가로줄에 들어있는 토마토의 상태가 M개의 정수로 주어진다. 정수 1은 익은 토마토, 정수 0은 익지 않은 토마토, 정수 -1은 토마토가 들어있지 않은 칸을 나타낸다.
# 토마토가 하나 이상 있는 경우만 입력으로 주어진다.

# 출력
# 여러분은 토마토가 모두 익을 때까지의 최소 날짜를 출력해야 한다. 만약, 저장될 때부터 모든 토마토가 익어있는 상태이면 0을 출력해야 하고, 토마토가 모두 익지는 못하는 상황이면 -1을 출력해야 한다.


# 1차 수정 : 변수명 변경 및 로직 변경
from collections import deque
from sys import stdin

input = stdin.readline

m, n = map(int, input().split())
tomatoes = deque()
arr = []
unripe_tomatoes = 0

for y in range(n):
    row = list(map(int, input().split()))
    arr.append(row)
    for x, value in enumerate(row):
        if value == 1:
            tomatoes.append((x, y, 0))
        elif value == 0:
            unripe_tomatoes += 1

directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
day_cnt = 0
while tomatoes:
    x, y, day_cnt = tomatoes.popleft()
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < m and 0 <= ny < n and arr[ny][nx] == 0:
            arr[ny][nx] = 1
            tomatoes.append((nx, ny, day_cnt + 1))
            unripe_tomatoes -= 1

print(day_cnt if unripe_tomatoes == 0 else -1)
# 98664KB, 2080ms, 789B


# 초기 코드
from collections import deque
from sys import stdin
input = stdin.readline

m, n = map(int, input().split())
tomatoes = deque()
arr = []
unripe_tomatoes = 0
day_cnt = 0
for y in range(n):
    temp_arr = list(map(int, input().split()))
    arr.append(temp_arr)
    for x, box in enumerate(temp_arr):
        if box == 1:
            tomatoes.append((x, y))
        elif box == 0:
            unripe_tomatoes += 1

dir = [(1,0),(-1,0),(0,1),(0,-1)]
temp_tomatoes = deque()
while tomatoes:
    x, y = tomatoes.popleft()
    for dx, dy in dir:
        nx, ny = x+dx, y+dy
        if 0 <= nx < m and 0 <= ny < n and arr[ny][nx] == 0:
            arr[ny][nx] = 1
            temp_tomatoes.append((nx, ny))
            unripe_tomatoes -= 1
    if not tomatoes and temp_tomatoes:
        tomatoes.extend(temp_tomatoes)
        temp_tomatoes.clear()
        day_cnt += 1

print(day_cnt if not unripe_tomatoes else -1)

# 102840KB, 1932ms, 905B

