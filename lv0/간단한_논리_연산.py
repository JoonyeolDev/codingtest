# https://school.programmers.co.kr/learn/courses/30/lessons/181917
# 간단한 논리 연산

# 문제 설명
# boolean 변수 x1, x2, x3, x4가 매개변수로 주어질 때, 다음의 식의 true/false를 return 하는 solution 함수를 작성해 주세요.

# (x1 ∨ x2) ∧ (x3 ∨ x4)

x1, x2, x3, x4 = False, True, True, True
# result = True

def solution(x1, x2, x3, x4):
    return (x1 or x2) and (x3 or x4)