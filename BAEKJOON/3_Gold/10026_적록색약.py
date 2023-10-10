# https://www.acmicpc.net/problem/10026
# 적록색약

# 문제
# 적록색약은 빨간색과 초록색의 차이를 거의 느끼지 못한다. 따라서, 적록색약인 사람이 보는 그림은 아닌 사람이 보는 그림과는 좀 다를 수 있다.
# 크기가 N×N인 그리드의 각 칸에 R(빨강), G(초록), B(파랑) 중 하나를 색칠한 그림이 있다. 그림은 몇 개의 구역으로 나뉘어져 있는데, 구역은 같은 색으로 이루어져 있다. 또, 같은 색상이 상하좌우로 인접해 있는 경우에 두 글자는 같은 구역에 속한다. (색상의 차이를 거의 느끼지 못하는 경우도 같은 색상이라 한다)
# 예를 들어, 그림이 아래와 같은 경우에
# RRRBB
# GGBBB
# BBBRR
# BBRRR
# RRRRR
# 적록색약이 아닌 사람이 봤을 때 구역의 수는 총 4개이다. (빨강 2, 파랑 1, 초록 1) 하지만, 적록색약인 사람은 구역을 3개 볼 수 있다. (빨강-초록 2, 파랑 1)
# 그림이 입력으로 주어졌을 때, 적록색약인 사람이 봤을 때와 아닌 사람이 봤을 때 구역의 수를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 N이 주어진다. (1 ≤ N ≤ 100)
# 둘째 줄부터 N개 줄에는 그림이 주어진다.

# 출력
# 적록색약이 아닌 사람이 봤을 때의 구역의 개수와 적록색약인 사람이 봤을 때의 구역의 수를 공백으로 구분해 출력한다.


from collections import deque
from sys import stdin
input = stdin.readline

n = int(input())

painting = [input().rstrip('\n') for _ in range(n)]
visited = [[False for _ in range(n)] for _ in range(n)]
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def bfs(is_blind):
    area = 0
    cnt = 0
    for y in range(n):
        for x in range(n):
            if visited[y][x] == is_blind:
                queue = deque([(y, x)])
                color = painting[y][x]
                area += 1
                if is_blind:
                    color = 'RG' if painting[y][x] in 'RG' else 'B'
                visited[y][x] = not is_blind
                while queue:
                    current_y, current_x = queue.popleft()

                    for dy, dx in directions:
                        ny, nx = current_y + dy, current_x + dx
                        if 0 <= ny < n and 0 <= nx < n and visited[ny][nx] == is_blind and painting[ny][nx] in color:
                            queue.append((ny, nx))
                            visited[ny][nx] = not is_blind
                            cnt += 1
            if area + cnt == n ** 2:
                return area

print(bfs(False), bfs(True))
# 34096KB, 76ms, 1192B


# 초기 코드 : 메모리 초과
from collections import deque
from sys import stdin
input = stdin.readline

n = int(input())

painting = [input().rstrip('\n') for _ in range(n)]
visited = [[0 for _ in range(n)] for _ in range(n)]
blind_visited = [[0 for _ in range(n)] for _ in range(n)]
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
area = 0
blind_area = 0
for y in range(n):
    for x in range(n):
        if not visited[y][x]:
            queue = deque([(y, x)])
            
            color = painting[y][x]
            while queue:
                current_y, current_x = queue.popleft()
                visited[current_y][current_x] = 1
                for dy, dx in directions:
                    ny, nx = current_y + dy, current_x + dx
                    if 0 <= ny < n and 0 <= nx < n and not visited[ny][nx] and painting[ny][nx] == color:
                        queue.append((ny, nx))
            area += 1
        if not blind_visited[y][x]:
            queue = deque([(y, x)])
            
            color = 'RG' if painting[y][x] in 'RG' else 'B'
            while queue:
                current_y, current_x = queue.popleft()
                blind_visited[current_y][current_x] = 1
                for dy, dx in directions:
                    ny, nx = current_y + dy, current_x + dx
                    if 0 <= ny < n and 0 <= nx < n and not blind_visited[ny][nx] and painting[ny][nx] in color:
                        queue.append((ny, nx))
            blind_area += 1

print(area, blind_area)
