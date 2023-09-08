# https://school.programmers.co.kr/learn/courses/30/lessons/120847
# 최댓값 만들기 (1)

# 문제 설명
# 정수 배열 numbers가 매개변수로 주어집니다. 
# numbers의 원소 중 두 개를 곱해 만들 수 있는 최댓값을 
# return하도록 solution 함수를 완성해주세요.

# 제한사항
# 0 ≤ numbers의 원소 ≤ 10,000
# 2 ≤ numbers의 길이 ≤ 100

# sort로 정렬 후 뒤에서 첫번째 두번째 인덱스 곱하기

numbers = [1, 2, 3, 4, 5]

numbers.sort()
answer = numbers[-1]*numbers[-2]
print(answer)

# 제출용 함수
def solution(numbers):
    numbers.sort()
    answer = numbers[-1]*numbers[-2]
    return answer