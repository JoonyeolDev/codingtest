# https://www.acmicpc.net/problem/11724
# 연결 요소의 개수

# 문제
# 방향 없는 그래프가 주어졌을 때, 연결 요소 (Connected Component)의 개수를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 정점의 개수 N과 간선의 개수 M이 주어진다. (1 ≤ N ≤ 1,000, 0 ≤ M ≤ N×(N-1)/2) 둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v가 주어진다. (1 ≤ u, v ≤ N, u ≠ v) 같은 간선은 한 번만 주어진다.

# 출력
# 첫째 줄에 연결 요소의 개수를 출력한다.

from collections import defaultdict
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

graph = defaultdict(list)

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
max_num_node = max(graph)
visited = [False] * (max_num_node + 1)
num_components = 0

for node in graph:
    if not visited[node]:
        stack = [node]
        while stack:
            current_node = stack.pop()
            if not visited[current_node]:
                visited[current_node] = True
                for neighbor in graph[current_node]:
                    if not visited[neighbor]:
                        stack.append(neighbor)
        num_components += 1

print(num_components)

# 