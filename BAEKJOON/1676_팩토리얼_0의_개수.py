# https://www.acmicpc.net/problem/1676
# 팩토리얼 0의 개수

# 문제
# N!에서 뒤에서부터 처음 0이 아닌 숫자가 나올 때까지 0의 개수를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 N이 주어진다. (0 ≤ N ≤ 500)

# 출력
# 첫째 줄에 구한 0의 개수를 출력한다.

from sys import stdin
input = stdin.readline

n = int(input().rstrip('\n'))

def factorial(num):
    if not num: return '1'
    f = 1
    for i in range(1,num+1):
        f *= i
    return str(f)

print(len(factorial(n))-len(factorial(n).rstrip('0')))

# 31256KB, 48ms, 248B