# https://www.acmicpc.net/problem/1697
# 숨바꼭질

# 문제
# 수빈이는 동생과 숨바꼭질을 하고 있다. 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다. 수빈이는 걷거나 순간이동을 할 수 있다. 만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다. 순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동하게 된다.
# 수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램을 작성하시오.

# 입력
# 첫 번째 줄에 수빈이가 있는 위치 N과 동생이 있는 위치 K가 주어진다. N과 K는 정수이다.

# 출력
# 수빈이가 동생을 찾는 가장 빠른 시간을 출력한다.

import sys
input = sys.stdin.readline
n, k = map(int, input().split())


# 초기 코드 : dp로 풀기
def dp(n, k):
    dp = [0] * 100001
    num = 0
    for i in range(n,-1,-1):
        dp[i] = num
        num += 1

    for i in range(n+1, 100001):
        dp[i] = dp[i-1] + 1
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i//2] + 1)
        if i>0:
            dp[i-1] = min(dp[i-1],dp[i]+1)
    return dp[k]
print(dp(n, k))
# 35108KB, 132ms, 327B


# 1차 수정 : BFS로 풀기
from collections import deque
def bfs(n, k):
    MAX = 100001
    visited = [0] * MAX 
    q = deque()
    q.append(n)
    visited[n] = 1
    while q:
        current = q.popleft()
        if current == k:
            return visited[current] - 1
        for next_pos in [current - 1, current + 1, current * 2]:
            if 0 <= next_pos < MAX and visited[next_pos] == 0:
                visited[next_pos] = visited[current] + 1
                q.append(next_pos)
print(bfs(n, k))
# 35108KB, 96ms, 577B

