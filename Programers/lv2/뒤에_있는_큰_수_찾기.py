# https://school.programmers.co.kr/learn/courses/30/lessons/154539
# 뒤에 있는 큰 수 찾기

# 문제 설명
# 정수로 이루어진 배열 numbers가 있습니다. 배열 의 각 원소들에 대해 자신보다 뒤에 있는 숫자 중에서 자신보다 크면서 가장 가까이 있는 수를 뒷 큰수라고 합니다.
# 정수 배열 numbers가 매개변수로 주어질 때, 모든 원소에 대한 뒷 큰수들을 차례로 담은 배열을 return 하도록 solution 함수를 완성해주세요. 단, 뒷 큰수가 존재하지 않는 원소는 -1을 담습니다.

# 제한사항
# 4 ≤ numbers의 길이 ≤ 1,000,000
# 1 ≤ numbers[i] ≤ 1,000,000

numbers = [2, 3, 3, 5]
# result = [3, 5, 5, -1]
numbers = 	[9, 1, 5, 3, 6, 2]


# 1차 수정 : 시간복잡도 개선
def solution(numbers):
    answer = [-1] * len(numbers)
    stack = []
    for idx, num in enumerate(numbers):
        while stack and numbers[stack[-1]] < num:
            last = stack.pop()
            answer[last] = num
        stack.append(idx)
    return answer
# 339.21ms, 75.4MB


# 초기 코드 : 시간 초과
def solution(numbers):
    len_numbers = len(numbers)
    answer = []
    for idx, number in enumerate(numbers):
        for i in range(idx+1, len_numbers):
            if number < numbers[i]:
                answer.append(numbers[i])
                break
        else: answer.append(-1)
    return answer

