# https://www.acmicpc.net/problem/14495
# 피보나치 비스무리한 수열

# 문제
# 피보나치 비스무리한 수열은 f(n) = f(n-1) + f(n-3)인 수열이다. f(1) = f(2) = f(3) = 1이며 피보나치 비스무리한 수열을 나열하면 다음과 같다.
# 1, 1, 1, 2, 3, 4, 6, 9, 13, 19, ...
# 자연수 n을 입력받아 n번째 피보나치 비스무리한 수열을 구해보자!

# 입력
# 자연수 n(1 ≤ n ≤ 116)이 주어진다.

# 출력
# n번째 피보나치 비스무리한 수를 출력한다.

from sys import stdin
input = stdin.readline

n = int(input())

dp = [1] * (n + 1)
if n >= 4:
    idx = 4

    while idx <= n:
        dp[idx] = dp[idx-1] + dp[idx-3]
        idx += 1
print(dp[-1])
# 31256KB, 44ms, 194B
