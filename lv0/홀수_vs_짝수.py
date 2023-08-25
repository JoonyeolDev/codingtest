# https://school.programmers.co.kr/learn/courses/30/lessons/181887
# 홀수 vs 짝수

# 문제 설명
# 정수 리스트 num_list가 주어집니다. 가장 첫 번째 원소를 1번 원소라고 할 때, 홀수 번째 원소들의 합과 짝수 번째 원소들의 합 중 큰 값을 return 하도록 solution 함수를 완성해주세요. 두 값이 같을 경우 그 값을 return합니다.

# 제한사항
# 5 ≤ num_list의 길이 ≤ 50
# -9 ≤ num_list의 원소 ≤ 9

num_list = [4, 2, 6, 1, 7, 6]
# result = 17

def solution(num_list):
    return max(sum(num for idx,num in enumerate(num_list,1) if idx%2),sum(num for idx,num in enumerate(num_list,1) if not idx%2))