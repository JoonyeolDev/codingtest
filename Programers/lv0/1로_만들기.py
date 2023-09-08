# https://school.programmers.co.kr/learn/courses/30/lessons/181880
# 1로 만들기

# 문제 설명
# 정수가 있을 때, 짝수라면 반으로 나누고, 홀수라면 1을 뺀 뒤 반으로 나누면, 마지막엔 1이 됩니다. 예를 들어 10이 있다면 다음과 같은 과정으로 1이 됩니다.

# 10 / 2 = 5
# (5 - 1) / 2 = 4
# 4 / 2 = 2
# 2 / 2 = 1
# 위와 같이 4번의 나누기 연산으로 1이 되었습니다.

# 정수들이 담긴 리스트 num_list가 주어질 때, num_list의 모든 원소를 1로 만들기 위해서 필요한 나누기 연산의 횟수를 return하도록 solution 함수를 완성해주세요.

# 제한사항
# 3 ≤ num_list의 길이 ≤ 15
# 1 ≤ num_list의 원소 ≤ 30

num_list = [12, 4, 15, 1, 14]
# result = 11

def change_1(num):
    cnt = 0
    while num > 1:
        num = (num-1)//2 if num % 2 else num//2
        cnt += 1
    return cnt

def solution(num_list):
    answer = 0
    for num in num_list:
        answer += change_1(num)
    return answer