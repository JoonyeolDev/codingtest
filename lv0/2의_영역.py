# https://school.programmers.co.kr/learn/courses/30/lessons/181894
# 2의 영역

# 문제 설명
# 정수 배열 arr가 주어집니다. 배열 안의 2가 모두 포함된 가장 작은 연속된 부분 배열을 return 하는 solution 함수를 완성해 주세요.

# 단, arr에 2가 없는 경우 [-1]을 return 합니다.

# 제한사항
# 1 ≤ arr의 길이 ≤ 100,000
# 1 ≤ arr의 원소 ≤ 10

arr = [1, 2, 1, 4, 5, 2, 9]
# result = [2, 1, 4, 5, 2]

def solution(arr):
    min_idx = len(arr)
    max_idx = 0
    for idx, num in enumerate(arr):
        if num == 2:
            min_idx = min(min_idx,idx)
            max_idx = max(max_idx,idx)
    if min_idx==len(arr) and max_idx == 0:
        return [-1]
    return arr[min_idx:max_idx+1]