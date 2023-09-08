# https://school.programmers.co.kr/learn/courses/30/lessons/181840
# 정수 찾기

# 문제 설명
# 정수 리스트 num_list와 찾으려는 정수 n이 주어질 때, num_list안에 n이 있으면 1을 없으면 0을 return하도록 solution 함수를 완성해주세요.

# 제한사항
# 3 ≤ num_list의 길이 ≤ 100
# 1 ≤ num_list의 원소 ≤ 100
# 1 ≤ n ≤ 100

num_list = [1, 2, 3, 4, 5]
n = 3
# result = 1

def solution(num_list, n):
    return 1 if n in num_list else 0