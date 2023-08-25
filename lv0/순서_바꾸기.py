# https://school.programmers.co.kr/learn/courses/30/lessons/181891
# 순서 바꾸기

# 문제 설명
# 정수 리스트 num_list와 정수 n이 주어질 때, num_list를 n 번째 원소 이후의 원소들과 n 번째까지의 원소들로 나눠 n 번째 원소 이후의 원소들을 n 번째까지의 원소들 앞에 붙인 리스트를 return하도록 solution 함수를 완성해주세요.

# 제한사항
# 2 ≤ num_list의 길이 ≤ 30
# 1 ≤ num_list의 원소 ≤ 9
# 1 ≤ n ≤ num_list의 길이

num_list = [2, 1, 6]
n = 1
# result = [1, 6, 2]

def solution(num_list, n):
    return num_list[n:]+num_list[:n]