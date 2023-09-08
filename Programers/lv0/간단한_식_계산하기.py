# https://school.programmers.co.kr/learn/courses/30/lessons/181865
# 간단한 식 계산하기

# 문제 설명
# 문자열 binomial이 매개변수로 주어집니다. binomial은 "a op b" 형태의 이항식이고 a와 b는 음이 아닌 정수, op는 '+', '-', '*' 중 하나입니다. 주어진 식을 계산한 정수를 return 하는 solution 함수를 작성해 주세요.

# 제한사항
# 0 ≤ a, b ≤ 40,000
# 0을 제외하고 a, b는 0으로 시작하지 않습니다.

binomial = "43 + 12"
# result = 55

def solution(binomial):
    a, op, b = binomial.split()
    op_map = {'+': int(a)+int(b), '-': int(a)-int(b), '*': int(a)*int(b)}
    return op_map[op]