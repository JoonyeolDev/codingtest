# https://www.acmicpc.net/problem/11727
# 2×n 타일링 2

# 문제
# 2×n 직사각형을 1×2, 2×1과 2×2 타일로 채우는 방법의 수를 구하는 프로그램을 작성하시오.
# 아래 그림은 2×17 직사각형을 채운 한가지 예이다.

# 입력
# 첫째 줄에 n이 주어진다. (1 ≤ n ≤ 1,000)

# 출력
# 첫째 줄에 2×n 크기의 직사각형을 채우는 방법의 수를 10,007로 나눈 나머지를 출력한다.

from sys import stdin
input = stdin.readline

n = int(input())
dp = [0] * (n + 1)
dp[1] = 1

for i in range(2, n + 1):
    dp[i] = 2 * dp[i-1] + (1 if (i-1) % 2 else -1)

print(dp[-1] % 10007)
# 31256KB, 48ms, 192B
