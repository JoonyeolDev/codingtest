# https://www.acmicpc.net/problem/1753
# 최단경로

# 문제
# 방향그래프가 주어지면 주어진 시작점에서 다른 모든 정점으로의 최단 경로를 구하는 프로그램을 작성하시오. 단, 모든 간선의 가중치는 10 이하의 자연수이다.

# 입력
# 첫째 줄에 정점의 개수 V와 간선의 개수 E가 주어진다. (1 ≤ V ≤ 20,000, 1 ≤ E ≤ 300,000) 모든 정점에는 1부터 V까지 번호가 매겨져 있다고 가정한다. 둘째 줄에는 시작 정점의 번호 K(1 ≤ K ≤ V)가 주어진다. 셋째 줄부터 E개의 줄에 걸쳐 각 간선을 나타내는 세 개의 정수 (u, v, w)가 순서대로 주어진다. 이는 u에서 v로 가는 가중치 w인 간선이 존재한다는 뜻이다. u와 v는 서로 다르며 w는 10 이하의 자연수이다. 서로 다른 두 정점 사이에 여러 개의 간선이 존재할 수도 있음에 유의한다.

# 출력
# 첫째 줄부터 V개의 줄에 걸쳐, i번째 줄에 i번 정점으로의 최단 경로의 경로값을 출력한다. 시작점 자신은 0으로 출력하고, 경로가 존재하지 않는 경우에는 INF를 출력하면 된다.

v, e = 5, 6
start = 1
graph = {5: [(1, 1)], 1: [(2, 2), (3, 3)], 2: [(3, 4), (4, 5)], 3: [(4, 6)]}

# 1차 개선 : 다익스트라 로직 개선
import heapq
from collections import defaultdict
from sys import stdin

def dijkstra(v, start, graph):
    fringe = []
    heapq.heappush(fringe, (0, start))
    result = [float("inf")] * (v + 1)
    result[start] = 0

    while fringe:
        distance, current_vertex = heapq.heappop(fringe)

        if result[current_vertex] < distance:
            continue

        for next_vertex, weight in graph[current_vertex]:
            new_distance = distance + weight
            if new_distance < result[next_vertex]:
                result[next_vertex] = new_distance
                heapq.heappush(fringe, (new_distance, next_vertex))
    return result

input = stdin.readline

v, e = map(int, input().split())
start = int(input())
graph = defaultdict(list)

for _ in range(e):
    s, e, w = map(int, input().split())
    graph[s].append((e, w))

result = dijkstra(v, start, graph)

for i in result[1:]:
    if i == float("inf"):
        print("INF")
    else:
        print(i)
# 70184KB, 704ms, 978B


# 초기 코드
import heapq
from collections import defaultdict
from sys import stdin


def dijkstra(start, graph):
    result = {}
    fringe = [(0, start)]
    marked = set()

    while fringe:
        distance, current_vertex = heapq.heappop(fringe)
        if current_vertex in marked:
            continue

        marked.add(current_vertex)
        result[current_vertex] = distance
        if not current_vertex in graph:
            continue

        succesors = graph[current_vertex]
        for next_vertex, weight in succesors:
            heapq.heappush(fringe, (distance + weight, next_vertex))
    return result

input = stdin.readline

v, e = map(int, input().split())
start = int(input())
graph = defaultdict(list)

for _ in range(e):
    s, e, w = map(int, input().split())
    graph[s].append((e, w))

result = dijkstra(start, graph)
print(result)
for i in range(1, v + 1):
    if i in result:
        print(result[i])
    else:
        print("INF")
# 98832KB, 1228ms,959B
