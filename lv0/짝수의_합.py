# https://school.programmers.co.kr/learn/courses/30/lessons/120831
# 짝수의 합

# 문제 설명
# 정수 n이 주어질 때, n이하의 짝수를 모두 더한 값을
# return 하도록 solution 함수를 작성해주세요.

# 제한사항
# 0 < n <= 1000

def solution(n):
    answer = 0
    for num in range(n+1):
        if num%2 == 0: answer += num 
    return answer
