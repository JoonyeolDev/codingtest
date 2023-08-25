# https://school.programmers.co.kr/learn/courses/30/lessons/181896
# 첫 번째로 나오는 음수

# 문제 설명
# 정수 리스트 num_list가 주어질 때, 첫 번째로 나오는 음수의 인덱스를 return하도록 solution 함수를 완성해주세요. 음수가 없다면 -1을 return합니다.

# 제한사항
# 5 ≤ num_list의 길이 ≤ 100
# -10 ≤ num_list의 원소 ≤ 100

num_list = [12, 4, 15, 46, 38, -2, 15]
#  result = 5

def solution(num_list):
    for idx, value in enumerate(num_list):
        if value < 0:
            return idx
    return -1


print(solution(num_list))