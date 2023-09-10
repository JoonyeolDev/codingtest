# https://www.acmicpc.net/problem/2234
# 성곽

# 문제
# 대략 위의 그림과 같이 생긴 성곽이 있다. 굵은 선은 벽을 나타내고, 점선은 벽이 없어서 지나다닐 수 있는 통로를 나타낸다. 이러한 형태의 성의 지도를 입력받아서 다음을 계산하는 프로그램을 작성하시오.

# 이 성에 있는 방의 개수
# 가장 넓은 방의 넓이
# 하나의 벽을 제거하여 얻을 수 있는 가장 넓은 방의 크기
# 위의 예에서는 방은 5개고, 가장 큰 방은 9개의 칸으로 이루어져 있으며, 위의 그림에서 화살표가 가리키는 벽을 제거하면 16인 크기의 방을 얻을 수 있다.

# 성은 M × N(1 ≤ M, N ≤ 50)개의 정사각형 칸으로 이루어진다. 성에는 최소 두 개의 방이 있어서, 항상 하나의 벽을 제거하여 두 방을 합치는 경우가 있다.

# 입력
# 첫째 줄에 두 정수 N, M이 주어진다. 다음 M개의 줄에는 N개의 정수로 벽에 대한 정보가 주어진다. 벽에 대한 정보는 한 정수로 주어지는데, 서쪽에 벽이 있을 때는 1을, 북쪽에 벽이 있을 때는 2를, 동쪽에 벽이 있을 때는 4를, 남쪽에 벽이 있을 때는 8을 더한 값이 주어진다. 참고로 이진수의 각 비트를 생각하면 쉽다. 따라서 이 값은 0부터 15까지의 범위 안에 있다.

# 출력
# 첫째 줄에 1의 답을, 둘째 줄에 2의 답을, 셋째 줄에 3의 답을 출력한다.

from collections import defaultdict, deque
from sys import stdin
input = stdin.readline

n, m = map(int, input().split())

graph = defaultdict(list)
direction = [(1,0),(0,1),(-1,0),(0,-1)]

for y in range(m):
    for x, num in enumerate(list(map(int, input().split()))):
        bin_num = bin(num).lstrip('0b')
        bin_num = '0'*(4-len(bin_num)) + bin_num
        for idx, bit in enumerate(bin_num):
            if bit == '0':
                dy, dx = direction[idx]
                ny, nx = y+dy, x+dx
                if 0 <= ny < m and 0 <= nx < n and (ny, nx) not in graph[(y, x)]:
                    graph[(y, x)].append((ny, nx))
                    graph[(ny, nx)].append((y, x))
visited = [[False for _ in range(n)] for _ in range(m)]
total_area = []
for y, x in graph:
    if visited[y][x]:
        continue
    queue = deque([(y, x)])
    area = []
    while queue:
        current_node = queue.popleft()
        y, x = current_node
        if visited[y][x]:
            continue
        area.append(current_node)
        visited[y][x] = True
        for vertex in graph[current_node]:
            ny, nx = vertex
            if not visited[ny][nx]:
                queue.append(vertex)
    total_area.append(area)
    
for y, row in enumerate(visited):
    for x, visit in enumerate(row):
        if not visit:
            total_area.append([(y, x)])
total_area.sort(key=lambda x: len(x), reverse=True)
len_total_area = len(total_area)
max_merge_room = 0
for i in range(len_total_area-1):
    for vertex in total_area[i]:
        y, x = vertex
        for dy, dx in direction:
            ny, nx = y+dy, x+dx
            if 0 <= ny < m and 0 <= nx < n:
                new_vertex = (ny, nx)
                if new_vertex in total_area[i]:
                    continue
                for j in range(i+1,len_total_area):
                    if new_vertex in total_area[j]:
                        merge_room = len(total_area[i]) + len(total_area[j])
                        max_merge_room = max(merge_room, max_merge_room)

print(len_total_area)
print(len(total_area[0]))
print(max_merge_room)

# 34288KB, 1352ms, 2107B