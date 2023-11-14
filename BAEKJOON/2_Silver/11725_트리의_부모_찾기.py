# https://www.acmicpc.net/problem/11725
# 트리의 부모 찾기

# 문제
# 루트 없는 트리가 주어진다. 이때, 트리의 루트를 1이라고 정했을 때, 각 노드의 부모를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 노드의 개수 N (2 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N-1개의 줄에 트리 상에서 연결된 두 정점이 주어진다.

# 출력
# 첫째 줄부터 N-1개의 줄에 각 노드의 부모 노드 번호를 2번 노드부터 순서대로 출력한다.

from collections import defaultdict
from sys import stdin
input = stdin.readline

tree = defaultdict(list)
n = int(input())

for _ in range(n - 1):
    s, e = map(int, input().split())
    tree[s].append(e)
    tree[e].append(s)

visited = [False] * (n + 1)

stack = [1]
visited[1] = True
while stack:
    node = stack.pop()
    for vertex in tree[node]:
        if not visited[vertex]:
            stack.append(vertex)
            visited[vertex] = node

print('\n'.join(map(str, visited[2:])))
# 61568KB, 304ms, 495B
