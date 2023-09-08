# https://school.programmers.co.kr/learn/courses/30/lessons/181920
# 카운트 업

# 문제 설명
# 정수 start_num와 end_num가 주어질 때, start_num부터 end_num까지의 숫자를 차례로 담은 리스트를 return하도록 solution 함수를 완성해주세요.

# 제한사항
# 0 ≤ start_num ≤ end_num ≤ 50

start_num, end_num = 3, 10
# result = [3, 4, 5, 6, 7, 8, 9, 10]

def solution(start_num, end_num):
    return [num for num in range(start_num, end_num+1)]