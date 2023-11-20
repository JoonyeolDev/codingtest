# https://www.acmicpc.net/problem/11444
# 피보나치 수 6

# 문제
# 피보나치 수는 0과 1로 시작한다. 0번째 피보나치 수는 0이고, 1번째 피보나치 수는 1이다. 그 다음 2번째 부터는 바로 앞 두 피보나치 수의 합이 된다.
# 이를 식으로 써보면 Fn = Fn-1 + Fn-2 (n ≥ 2)가 된다.
# n=17일때 까지 피보나치 수를 써보면 다음과 같다.
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597
# n이 주어졌을 때, n번째 피보나치 수를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 n이 주어진다. n은 1,000,000,000,000,000,000보다 작거나 같은 자연수이다.

# 출력
# 첫째 줄에 n번째 피보나치 수를 1,000,000,007으로 나눈 나머지를 출력한다.

from sys import stdin

input = stdin.readline

n = int(input())

dp = [0] * (1001)
dp[1] = 1
for i in range(2, 1001):
    dp[i] = dp[i - 1] + dp[i - 2]
    if dp[i] >= 1000000007:
        dp[i] = dp[i] % 1000000007

# a = dp[100] * (dp[100] + dp[99]) + dp[99] * dp[100]
# a %= 1000000007
# print(a)
# a10 = 55 a1 + 34 a0
# a20 = 55 a11 + 34 a10 = 89 a10 + 55 a9
# a[i] = a[n+1] * a[i - n] + a[n] * a[i - (n+1)]

# i % 2 == 0 and n == i/2
# a[i] = a[i/2 + 1] * a[i/2] + a[i/2] * a[i/2 - 1]
# a[i] = a[i/2] * (a[i/2 + 1] + a[i/2 - 1])

# i % 2 == 1
# a[i] = a[n+1] * a[i - n] + a[n] * a[i - (n+1)]
# a[i] = a[(i-1)/2+1] * a[i - (i-1)/2] + a[(i-1)/2] * a[i - ((i-1)/2+1)]
# a[i] = a[(i+1)/2] * a[(i+1)/2] + a[(i-1)/2] * a[(i-1)/2]
# a[i] = a[(i+1)/2] ** 2 + a[(i-1)/2] ** 2

# a[100] = a[99] + a[98] = a[50] * (a[51] + a[49]) = 687995182
# a[100] = a[50] ** 2 + a[49] ** 2 + a[49] * (a[48] + a[50])
#           (a[50] + a[49])**2 + a[49](a[48] - a[50])


def fibonacci(n):
    if n <= 1000:
        return dp[n]
    n //= 2
    if n % 2:
        answer = fibonacci(n) * (fibonacci(n+1) + fibonacci(n-1))
    else:
        answer = fibonacci(n + 1) ** 2 + fibonacci(n) ** 2
    return answer % 1000000007

def matrix_mult(a, b):
    result = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                result[i][j] += a[i][k] * b[k][j]
                result[i][j] %= 1000000007
    return result

def matrix_pow(exponent):
    base = [[1, 1], [1, 0]]
    result = [[1, 0], [0, 1]]
    while exponent > 0:
        if exponent % 2:
            result = matrix_mult(result, base)
        base = matrix_mult(base, base)
        exponent //= 2
    return result

def fibonacci(n):
    if n == 0:
        return 0
    return matrix_pow(n - 1)[0][0]

print(fibonacci(n))
# 31120KB, 44ms, 669B
