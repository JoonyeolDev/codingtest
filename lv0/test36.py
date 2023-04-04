# https://school.programmers.co.kr/learn/courses/30/lessons/120905
# n의 배수 고르기

# 문제 설명
# 정수 n과 정수 배열 numlist가 매개변수로 주어질 때, 
# numlist에서 n의 배수가 아닌 수들을 제거한 배열을 return하도록 
# solution 함수를 완성해주세요.

# 제한사항
# 1 ≤ n ≤ 10,000
# 1 ≤ numlist의 크기 ≤ 100
# 1 ≤ numlist의 원소 ≤ 100,000

n = 3
numlist = [4, 5, 6, 7, 8, 9, 10, 11, 12]

answer = []
for num in numlist:
    if num%n ==0: answer.append(num)

print(answer)

# 제출용 함수
def solution(n, numlist):
    answer=[]
    for i in numlist:
        if i%n==0: answer.append(i)
    return answer