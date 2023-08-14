# https://school.programmers.co.kr/learn/courses/30/lessons/12941
# 최솟값 만들기

# 문제 설명
# 길이가 같은 배열 A, B 두개가 있습니다. 각 배열은 자연수로 이루어져 있습니다.
# 배열 A, B에서 각각 한 개의 숫자를 뽑아 두 수를 곱합니다. 
# 이러한 과정을 배열의 길이만큼 반복하며, 두 수를 곱한 값을 누적하여 더합니다. 
# 이때 최종적으로 누적된 값이 최소가 되도록 만드는 것이 목표입니다. 
# (단, 각 배열에서 k번째 숫자를 뽑았다면 다음에 k번째 숫자는 다시 뽑을 수 없습니다.)

# 배열 A, B가 주어질 때 최종적으로 누적된 최솟값을 
# return 하는 solution 함수를 완성해 주세요.

# 제한사항
# 배열 A, B의 크기 : 1,000 이하의 자연수
# 배열 A, B의 원소의 크기 : 1,000 이하의 자연수

A=[1,4,2]
B=[5,4,4]
# answer = 29


# 1차 수정 : 변수 할당
def solution(A,B):
    answer = 0
    A.sort()
    B.sort(reverse=True)
    len_a = len(A)
    for i in range(len_a):
        ab = A[i]*B[i]
        answer += ab
    return answer
# 0.38ms


# 초기 코드
def solution(A,B):
    answer = 0
    A.sort()
    B.sort(reverse=True)
    for i in range(len(A)):
        answer += A[i]*B[i]
    return answer
# 0.50ms