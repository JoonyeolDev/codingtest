# https://school.programmers.co.kr/learn/courses/30/lessons/181929
# 원소들의 곱과 합

# 문제 설명
# 정수가 담긴 리스트 num_list가 주어질 때, 모든 원소들의 곱이 모든 원소들의 합의 제곱보다 작으면 1을 크면 0을 return하도록 solution 함수를 완성해주세요.

# 제한사항
# 2 ≤ num_list의 길이 ≤ 10
# 1 ≤ num_list의 원소 ≤ 9

num_list = [3, 4, 5, 2, 1]
# result = 1

def solution(num_list):
    reduce = 1
    for num in num_list:
        reduce *= num
    return 1 if sum(num_list)**2 > reduce else 0