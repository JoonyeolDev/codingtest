# https://www.acmicpc.net/problem/11403
# 경로 찾기

# 문제
# 가중치 없는 방향 그래프 G가 주어졌을 때, 모든 정점 (i, j)에 대해서, i에서 j로 가는 길이가 양수인 경로가 있는지 없는지 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 정점의 개수 N (1 ≤ N ≤ 100)이 주어진다. 둘째 줄부터 N개 줄에는 그래프의 인접 행렬이 주어진다. i번째 줄의 j번째 숫자가 1인 경우에는 i에서 j로 가는 간선이 존재한다는 뜻이고, 0인 경우는 없다는 뜻이다. i번째 줄의 i번째 숫자는 항상 0이다.

# 출력
# 총 N개의 줄에 걸쳐서 문제의 정답을 인접행렬 형식으로 출력한다. 정점 i에서 j로 가는 길이가 양수인 경로가 있으면 i번째 줄의 j번째 숫자를 1로, 없으면 0으로 출력해야 한다.

# n = 3
# graph = {0: [1], 1: [2], 2: [0]}

from collections import deque
from sys import stdin

input = stdin.readline

n = int(input())
graph = {}
connnection = []

for i in range(n):
    row = list(map(int, input().split()))
    graph[i] = [num for num, exist in enumerate(row) if exist]

for key in graph:
    queue = deque([key])
    visited = [0 for _ in range(n)]
    while queue:
        current = queue.popleft()
        for vertex in graph[current]:
            if not visited[vertex]:
                visited[vertex] = 1
                queue.append(vertex)
    connnection.append(visited)

for i in connnection:
    print(" ".join(list(map(str, i))))
# 34140KB, 76ms, 618B
