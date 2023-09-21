# https://www.acmicpc.net/problem/14940
# 쉬운 최단거리

# 문제
# 지도가 주어지면 모든 지점에 대해서 목표지점까지의 거리를 구하여라.
# 문제를 쉽게 만들기 위해 오직 가로와 세로로만 움직일 수 있다고 하자.

# 입력
# 지도의 크기 n과 m이 주어진다. n은 세로의 크기, m은 가로의 크기다.(2 ≤ n ≤ 1000, 2 ≤ m ≤ 1000)
# 다음 n개의 줄에 m개의 숫자가 주어진다. 0은 갈 수 없는 땅이고 1은 갈 수 있는 땅, 2는 목표지점이다. 입력에서 2는 단 한개이다.

# 출력
# 각 지점에서 목표지점까지의 거리를 출력한다. 원래 갈 수 없는 땅인 위치는 0을 출력하고, 원래 갈 수 있는 땅인 부분 중에서 도달할 수 없는 위치는 -1을 출력한다.

from collections import deque
n, m = map(int, input().split())

arr = []
for y in range(n):
    row = list(map(int, input().split()))
    for x, ground in enumerate(row):
        if ground == 2:
            start = (x, y, 0)
    arr.append(row)

distances = [[-1 if arr[i][j] == 1 else 0 for j in range(m)] for i in range(n)]
directions = [(1,0),(-1,0),(0,1),(0,-1)]

distances[start[1]][start[0]] = 0
queue = deque([start])

while queue:
    x, y, distance = queue.popleft()
    for dx, dy in directions:
        nx, ny = x+dx, y+dy

        if 0 <= nx < m and 0 <= ny < n and distances[ny][nx] == -1:
            queue.append((nx, ny, distance+1))
            distances[ny][nx] = distance+1


for row in distances:
    print(' '.join(map(str, row)))

