# https://www.acmicpc.net/problem/11400
# 단절선

# 문제
# 그래프가 주어졌을 때, 단절선을 모두 구해 출력하는 프로그램을 작성하시오.
# 단절선이란 그 간선을 제거했을 때, 그래프가 두 개 또는 그 이상으로 나누어지는 간선을 말한다. 즉, 제거했을 때 그래프의 connected component의 개수가 증가하는 간선을 말한다.

# 입력
# 첫째 줄에 두 정수 V(1≤V≤100,000), E(1≤E≤1,000,000)가 주어진다. 이는 그래프가 V개의 정점과 E개의 간선으로 이루어져 있다는 의미이다. 다음 E개의 줄에는 간선에 대한 정보를 나타내는 두 정수 A, B가 주어진다. 이는 A번 정점과 B번 정점이 연결되어 있다는 의미이며, 방향은 양방향이다.
# 그래프는 항상 연결되어 있으며, 같은 간선이 두 번 이상 들어오는 경우는 없다. 또, A와 B가 같은 경우도 없다.
# 그래프의 정점은 1부터 V까지 자연수이다.

# 출력
# 첫째 줄에 단절선의 개수 K를 출력한다.
# 둘째 줄부터 K개 줄에는 단절선을 사전순으로 한 줄에 하나씩 출력한다. 간선은 "A B" 형식으로 출력해야 하고, A < B를 만족해야 한다. 같은 간선은 한 번만 출력하면 된다. 즉, "A B"를 출력한 경우에 "B A"는 출력할 필요가 없다.

from collections import defaultdict
from sys import stdin
input = stdin.readline

v, e = map(int, input().split())
graph = defaultdict(list)
edges = set()

for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
#     if a > b:
#         a, b = b, a
#     edges.add((a,b))

# # 지금까지 방문한 정점 저장
# # 순환하면 지금까지 방문한 정점 반환
# # 순환안하면 방문한 정점 초기화

# for vertex in graph:
#     stack = [vertex]
#     visited = []
#     while stack:
#         current_node, visited = stack.pop()
#         for vertex in graph[current_node]:
#             if 

# print(graph)



from collections import defaultdict

visited = [False] * (v + 1)
disc = [float('inf')] * (v + 1)
low = [float('inf')] * (v + 1)
parent = [-1] * (v + 1)
cut_edges = set()

time = 0

for start_vertex in range(1, v + 1):
    if not visited[start_vertex]:
        stack = [(start_vertex, iter(graph[start_vertex]))]
        while stack:
            vertex, children = stack[-1]
            if not visited[vertex]:
                visited[vertex] = True
                disc[vertex] = time
                low[vertex] = time
                time += 1
            next_child = next(children, None)
            if next_child is not None:
                if not visited[next_child]:
                    parent[next_child] = vertex
                    stack.append((next_child, iter(graph[next_child])))
                elif parent[vertex] != next_child:
                    low[vertex] = min(low[vertex], disc[next_child])
            else:
                stack.pop()
                if parent[vertex] != -1:
                    low[parent[vertex]] = min(low[parent[vertex]], low[vertex])
                    if low[vertex] > disc[parent[vertex]]:
                        cut_edges.add((min(vertex, parent[vertex]), max(vertex, parent[vertex])))

print(len(cut_edges))

for a, b in sorted(cut_edges):
    print(f'{a} {b}')

