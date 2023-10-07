# https://www.acmicpc.net/problem/13549
# 숨바꼭질 3

# 문제
# 수빈이는 동생과 숨바꼭질을 하고 있다. 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다. 수빈이는 걷거나 순간이동을 할 수 있다. 만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다. 순간이동을 하는 경우에는 0초 후에 2*X의 위치로 이동하게 된다.
# 수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램을 작성하시오.

# 입력
# 첫 번째 줄에 수빈이가 있는 위치 N과 동생이 있는 위치 K가 주어진다. N과 K는 정수이다.

# 출력
# 수빈이가 동생을 찾는 가장 빠른 시간을 출력한다.

n, k = 5, 17

import heapq
from sys import stdin

input = stdin.readline

def ucs(start, goal):
    result = {}
    fringe = []
    marked = set()

    heapq.heappush(fringe, (0, start))

    while fringe:
        time, current_vertex = heapq.heappop(fringe)
        move = [
            (1, current_vertex + 1),
            (1, current_vertex - 1),
            (0, 2 * current_vertex),
        ]

        if current_vertex == goal:
            return time

        if current_vertex in marked:
            continue

        marked.add(current_vertex)
        result[current_vertex] = time
        for weight, next_vertex in move:
            if 0 <= next_vertex <= 100000:
                heapq.heappush(fringe, (time + weight, next_vertex))

def reverse_ucs(start, goal):
    result = {}
    fringe = []
    marked = set()

    heapq.heappush(fringe, (0, goal))

    while fringe:
        time, current_vertex = heapq.heappop(fringe)
        move = [
            (1, current_vertex + 1),
            (1, current_vertex - 1),
            (current_vertex % 2, current_vertex // 2),
        ]

        if current_vertex == start:
            return time

        if current_vertex in marked:
            continue

        marked.add(current_vertex)
        result[current_vertex] = time
        for weight, next_vertex in move:
            if 0 <= next_vertex:
                heapq.heappush(fringe, (time + weight, next_vertex))

n, k = map(int, input().split())

print(ucs(n, k))
# 50232KB, 288ms, 739B

print(reverse_ucs(n, k))
# 50232KB, 220ms, 802B
