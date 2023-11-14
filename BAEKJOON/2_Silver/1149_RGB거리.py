# https://www.acmicpc.net/problem/1149
# RGB거리

# 문제
# RGB거리에는 집이 N개 있다. 거리는 선분으로 나타낼 수 있고, 1번 집부터 N번 집이 순서대로 있다.
# 집은 빨강, 초록, 파랑 중 하나의 색으로 칠해야 한다. 각각의 집을 빨강, 초록, 파랑으로 칠하는 비용이 주어졌을 때, 아래 규칙을 만족하면서 모든 집을 칠하는 비용의 최솟값을 구해보자.
# 1번 집의 색은 2번 집의 색과 같지 않아야 한다.
# N번 집의 색은 N-1번 집의 색과 같지 않아야 한다.
# i(2 ≤ i ≤ N-1)번 집의 색은 i-1번, i+1번 집의 색과 같지 않아야 한다.

# 입력
# 첫째 줄에 집의 수 N(2 ≤ N ≤ 1,000)이 주어진다. 둘째 줄부터 N개의 줄에는 각 집을 빨강, 초록, 파랑으로 칠하는 비용이 1번 집부터 한 줄에 하나씩 주어진다. 집을 칠하는 비용은 1,000보다 작거나 같은 자연수이다.

# 출력
# 첫째 줄에 모든 집을 칠하는 비용의 최솟값을 출력한다.


# 1차 수정 : dp
from sys import stdin
input = stdin.readline

n = int(input())
dp = [[float('inf') for _ in range(3)] for _ in range((n + 1))]
dp[1] = list(map(int, input().split()))

for i in range(2, n + 1):
    rgb = list(map(int, input().split()))
    for j in range(3):
        dp[i][j] = min(k for idx, k in enumerate(dp[i-1]) if j != idx) + rgb[j]

print(min(dp[-1]))
# 31120KB, 40ms, 358B


# 초기 코드 : DFS, 시간초과
from sys import stdin
input = stdin.readline

n = int(input())
street = [0] * (n + 1)
min_sum = float('inf')

for i in range(1, n + 1):
    street[i] = tuple(map(int, input().split()))

for i in range(3):
    stack = [(i, 1, street[1][i])]
    while stack:
        last_color, cnt, temp_sum = stack.pop()

        if cnt == n:
            min_sum = min(min_sum, temp_sum)
            continue

        for color in range(3):
            if last_color != color and min_sum > temp_sum + street[cnt + 1][color]:
                stack.append((color, cnt + 1, temp_sum + street[cnt + 1][color]))

print(min_sum)