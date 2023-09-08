# https://school.programmers.co.kr/learn/courses/30/lessons/181849
# 문자열 정수의 합

# 문제 설명
# 한 자리 정수로 이루어진 문자열 num_str이 주어질 때, 각 자리수의 합을 return하도록 solution 함수를 완성해주세요.

# 제한사항
# 3 ≤ num_str ≤ 100

num_str = "123456789"
# result = 45

def solution(num_str):
    return sum([int(i) for i in num_str])