# https://school.programmers.co.kr/learn/courses/30/lessons/181935
# 홀짝에 따라 다른 값 반환하기

# 문제 설명
# 양의 정수 n이 매개변수로 주어질 때, n이 홀수라면 n 이하의 홀수인 모든 양의 정수의 합을 return 하고 n이 짝수라면 n 이하의 짝수인 모든 양의 정수의 제곱의 합을 return 하는 solution 함수를 작성해 주세요.

# 제한사항
# 1 ≤ n ≤ 100

n = 7
# result = 16

def solution(n):
    return ((n+1)//2)**2 if n % 2 else sum(i**2 for i in range(2, n+1) if not i % 2)