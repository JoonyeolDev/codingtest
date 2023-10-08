# https://www.acmicpc.net/problem/11779
# 최소비용 구하기 2

# 문제
# n(1≤n≤1,000)개의 도시가 있다. 그리고 한 도시에서 출발하여 다른 도시에 도착하는 m(1≤m≤100,000)개의 버스가 있다. 우리는 A번째 도시에서 B번째 도시까지 가는데 드는 버스 비용을 최소화 시키려고 한다. 그러면 A번째 도시에서 B번째 도시 까지 가는데 드는 최소비용과 경로를 출력하여라. 항상 시작점에서 도착점으로의 경로가 존재한다.

# 입력
# 첫째 줄에 도시의 개수 n(1≤n≤1,000)이 주어지고 둘째 줄에는 버스의 개수 m(1≤m≤100,000)이 주어진다. 그리고 셋째 줄부터 m+2줄까지 다음과 같은 버스의 정보가 주어진다. 먼저 처음에는 그 버스의 출발 도시의 번호가 주어진다. 그리고 그 다음에는 도착지의 도시 번호가 주어지고 또 그 버스 비용이 주어진다. 버스 비용은 0보다 크거나 같고, 100,000보다 작은 정수이다.
# 그리고 m+3째 줄에는 우리가 구하고자 하는 구간 출발점의 도시번호와 도착점의 도시번호가 주어진다.

# 출력
# 첫째 줄에 출발 도시에서 도착 도시까지 가는데 드는 최소 비용을 출력한다.
# 둘째 줄에는 그러한 최소 비용을 갖는 경로에 포함되어있는 도시의 개수를 출력한다. 출발 도시와 도착 도시도 포함한다.
# 셋째 줄에는 최소 비용을 갖는 경로를 방문하는 도시 순서대로 출력한다.

import heapq
from collections import defaultdict
from sys import stdin
input = stdin.readline

def ucs(n, start, goal, graph):
    fringe = []
    heapq.heappush(fringe, (0, start, [start]))
    result = [float("inf")] * (n + 1)
    result[start] = 0

    while fringe:
        cost, current_vertex, route = heapq.heappop(fringe)
        if current_vertex == goal:
            return cost, route

        if result[current_vertex] < cost:
            continue

        for next_vertex, weight in graph[current_vertex]:
            new_cost = cost + weight
            if new_cost < result[next_vertex]:
                result[next_vertex] = new_cost
                heapq.heappush(fringe, (new_cost, next_vertex, route + [next_vertex]))
    return result

n = int(input())
m = int(input())

graph = defaultdict(list)
for _ in range(m):
    s, e, w = map(int, input().split())
    graph[s].append((e, w))

start, goal = map(int, input().split())

cost, route = ucs(n, start, goal, graph)

print(cost)
print(len(route))
print(' '.join(list(map(str, route))))
# 66008KB, 292ms, 1056B
