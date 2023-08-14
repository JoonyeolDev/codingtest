# https://school.programmers.co.kr/learn/courses/30/lessons/120848
# 팩토리얼

# 문제 설명
# i팩토리얼 (i!)은 1부터 i까지 정수의 곱을 의미합니다. 
# 예를들어 5! = 5 * 4 * 3 * 2 * 1 = 120 입니다. 
# 정수 n이 주어질 때 다음 조건을 만족하는 가장 큰 정수 i를 
# return 하도록 solution 함수를 완성해주세요.
# i! ≤ n

# 제한사항
# 0 < n ≤ 3,628,800

# 팩토리얼을 직접 구현해보자
# for문으로 구현
factorial=1 
n=1
for i in range(1,n+1):
    factorial *= i
    if factorial > n : break
    else: answer = i
print(answer)


# 제출용 함수
def solution(n):
    factorial=1 
    for i in range(1,n+1):
        factorial *= i
        if factorial > n : break
        else: answer = i
    return answer


