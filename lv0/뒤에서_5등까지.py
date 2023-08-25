# https://school.programmers.co.kr/learn/courses/30/lessons/181853
# 뒤에서 5등까지

# 문제 설명
# 정수로 이루어진 리스트 num_list가 주어집니다. num_list에서 가장 작은 5개의 수를 오름차순으로 담은 리스트를 return하도록 solution 함수를 완성해주세요.

# 제한사항
# 6 ≤ num_list의 길이 ≤ 30
# 1 ≤ num_list의 원소 ≤ 100

num_list = [12, 4, 15, 46, 38, 1, 14]
# result = [1, 4, 12, 14, 15]

def solution(num_list):
    return sorted(num_list)[:5]