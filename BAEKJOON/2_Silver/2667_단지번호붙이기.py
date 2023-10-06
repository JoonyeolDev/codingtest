# https://www.acmicpc.net/problem/2667
# 단지번호붙이기

# 문제
# <그림 1>과 같이 정사각형 모양의 지도가 있다. 1은 집이 있는 곳을, 0은 집이 없는 곳을 나타낸다.
# 철수는 이 지도를 가지고 연결된 집의 모임인 단지를 정의하고, 단지에 번호를 붙이려 한다.
# 여기서 연결되었다는 것은 어떤 집이 좌우, 혹은 아래위로 다른 집이 있는 경우를 말한다.
# 대각선상에 집이 있는 경우는 연결된 것이 아니다. <그림 2>는 <그림 1>을 단지별로 번호를 붙인 것이다.
# 지도를 입력하여 단지수를 출력하고, 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력하는 프로그램을 작성하시오.

# 입력
# 첫 번째 줄에는 지도의 크기 N(정사각형이므로 가로와 세로의 크기는 같으며 5≤N≤25)이 입력되고, 그 다음 N줄에는 각각 N개의 자료(0혹은 1)가 입력된다.

# 출력
# 첫 번째 줄에는 총 단지수를 출력하시오. 그리고 각 단지내 집의 수를 오름차순으로 정렬하여 한 줄에 하나씩 출력하시오.

from collections import deque
from sys import stdin
input = stdin.readline

n = int(input())
map_ = []

for _ in range(n):
    map_.append(list(map(int, input().rstrip())))

visited = [[0 for _ in range(n)] for _ in range(n)]
direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
group = []

for y in range(n):
    for x in range(n):
        if not visited[y][x] and map_[y][x]:
            queue = deque([(y, x)])
            visited[y][x] = 1
            cnt = 1
            while queue:
                current = queue.popleft()
                cy, cx = current

                for dy, dx in direction:
                    ny, nx = cy + dy, cx + dx
                    if 0 <= ny < n and 0 <= nx < n and map_[ny][nx] and not visited[ny][nx]:
                        cnt += 1
                        queue.append((ny, nx))
                        visited[ny][nx] = 1
            if cnt:
                group.append(cnt)
                if cnt == 2:
                    print(y, x)
group.sort()

print(len(group))
for i in group:
    print(i)
# 34192KB, 64ms, 977B
