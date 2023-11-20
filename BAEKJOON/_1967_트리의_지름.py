# https://www.acmicpc.net/problem/1967
# 트리의 지름

# 문제
# 트리(tree)는 사이클이 없는 무방향 그래프이다. 트리에서는 어떤 두 노드를 선택해도 둘 사이에 경로가 항상 하나만 존재하게 된다. 트리에서 어떤 두 노드를 선택해서 양쪽으로 쫙 당길 때, 가장 길게 늘어나는 경우가 있을 것이다. 이럴 때 트리의 모든 노드들은 이 두 노드를 지름의 끝 점으로 하는 원 안에 들어가게 된다.
# 이런 두 노드 사이의 경로의 길이를 트리의 지름이라고 한다. 정확히 정의하자면 트리에 존재하는 모든 경로들 중에서 가장 긴 것의 길이를 말한다.
# 입력으로 루트가 있는 트리를 가중치가 있는 간선들로 줄 때, 트리의 지름을 구해서 출력하는 프로그램을 작성하시오. 아래와 같은 트리가 주어진다면 트리의 지름은 45가 된다.
# 트리의 노드는 1부터 n까지 번호가 매겨져 있다.

# 입력
# 파일의 첫 번째 줄은 노드의 개수 n(1 ≤ n ≤ 10,000)이다. 둘째 줄부터 n-1개의 줄에 각 간선에 대한 정보가 들어온다. 간선에 대한 정보는 세 개의 정수로 이루어져 있다. 첫 번째 정수는 간선이 연결하는 두 노드 중 부모 노드의 번호를 나타내고, 두 번째 정수는 자식 노드를, 세 번째 정수는 간선의 가중치를 나타낸다. 간선에 대한 정보는 부모 노드의 번호가 작은 것이 먼저 입력되고, 부모 노드의 번호가 같으면 자식 노드의 번호가 작은 것이 먼저 입력된다. 루트 노드의 번호는 항상 1이라고 가정하며, 간선의 가중치는 100보다 크지 않은 양의 정수이다.

# 출력
# 첫째 줄에 트리의 지름을 출력한다.

tree = {
    1: [(2, 3), (3, 2)],
    2: [(1, 3), (4, 5)],
    3: [(1, 2), (5, 11), (6, 9)],
    4: [(2, 5), (7, 1), (8, 7)],
    5: [(3, 11), (9, 15), (10, 4)],
    6: [(3, 9), (11, 6), (12, 10)],
    7: [(4, 1)],
    8: [(4, 7)],
    9: [(5, 15)],
    10: [(5, 4)],
    11: [(6, 6)],
    12: [(6, 10)],
}
n = 12

# 1차 수정: 트리의 지름 구하기
from collections import defaultdict
from sys import stdin
input = stdin.readline

def dfs(tree, n, start):
    stack = [(start, 0)]
    visited = [False] * (n + 1)
    max_weight, farthest_node = -1, -1

    while stack:
        node, weight = stack.pop()

        if visited[node]:
            continue
        visited[node] = True

        if weight > max_weight:
            farthest_node, max_weight = node, weight

        for next_node, w in tree[node]:
            if not visited[next_node]:
                stack.append((next_node, weight + w))
    return farthest_node, max_weight

tree = defaultdict(list)
n = int(input())

for _ in range(n - 1):
    parent, child, weight = map(int, input().split())
    tree[parent].append((child, weight))
    tree[child].append((parent, weight))

farthest_node, _ = dfs(tree, n, 1)
_, max_weight = dfs(tree, n, farthest_node)

print(max_weight)
# 35320KB, 84ms, 891B


# 초기 코드
from collections import defaultdict
from sys import stdin
input = stdin.readline

tree = defaultdict(list)
max_len = 0
n = int(input())

for _ in range(n - 1):
    parent, child, weight = map(int, input().split())
    tree[parent].append((child, weight))
    tree[child].append((parent, weight))

for i in range(1, n + 1):
    dp = [-1 for _ in range(n + 1)]
    stack = [(i, 0)]
    dp[i] = 0

    while stack:
        node, weight = stack.pop()

        for next_node, w in tree[node]:
            if dp[next_node] == -1:
                next_weight = weight + w
                dp[next_node] = next_weight
                stack.append((next_node, next_weight))
                max_len = max(max_len, next_weight)

print(max_len)
# 210692KB, 6508ms, 731B, pypy3
