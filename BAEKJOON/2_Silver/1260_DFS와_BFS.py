# https://www.acmicpc.net/problem/1260
# DFS와 BFS

# 문제
# 그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

# 입력
# 첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.

# 출력
# 첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.

from collections import defaultdict, deque
from sys import stdin
input = stdin.readline

graph = defaultdict(list)
n, m, v = map(int, input().split())

vertices = []
for _ in range(m):
    vertex1, vertex2 = map(int, input().split())
    graph[vertex1].append(vertex2)
    graph[vertex2].append(vertex1)

for key in graph:
    graph[key].sort()

stack = [v]
dfs_visited = [False]*(n+1)
dfs = []
while stack:
    current_node = stack.pop()
    if not dfs_visited[current_node]:
        dfs_visited[current_node] = True
        dfs.append(str(current_node))
        for vertex in graph[current_node][::-1]:
            if not dfs_visited[vertex]:
                stack.append(vertex)
print(' '.join(dfs))

queue = deque([v])
bfs_visited = [False]*(n+1)
bfs = []
while queue:
    current_node = queue.popleft()
    if not bfs_visited[current_node]:
        bfs_visited[current_node] = True
        bfs.append(str(current_node))
        for vertex in graph[current_node]:
            if not bfs_visited[vertex]:
                queue.append(vertex)

print(' '.join(bfs))

# 34184KB, 84ms, 1066B