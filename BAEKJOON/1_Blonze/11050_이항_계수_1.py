# https://www.acmicpc.net/problem/11050
# 이항 계수 1

# 문제
# 자연수 N과 정수 K가 주어졌을 때 이항 계수 
# (N K)를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 N과 K가 주어진다


# 출력
# (N K)를 출력한다.

from sys import stdin
input = stdin.readline
n, k = map(int ,input().split())

def factorial(num):
    if num == 0: return 1
    sum_ = 1
    for i in range(1, num+1):
        sum_ *= i
    return sum_

print(factorial(n)//(factorial(n-k)*factorial(k)))

# 31256KB, 44ms, 251B