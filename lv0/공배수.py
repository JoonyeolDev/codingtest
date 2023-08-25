# https://school.programmers.co.kr/learn/courses/30/lessons/181936
# 공배수

# 문제 설명
# 정수 number와 n, m이 주어집니다. number가 n의 배수이면서 m의 배수이면 1을 아니라면 0을 return하도록 solution 함수를 완성해주세요.

# 제한사항
# 10 ≤ number ≤ 100
# 2 ≤ n, m < 10

number = 60
n, m = 2, 3
# result = 1

def solution(number, n, m):
    return 1 if not number % n and not number % m else 0