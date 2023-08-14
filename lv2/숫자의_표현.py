# https://school.programmers.co.kr/learn/courses/30/lessons/12924
# 숫자의 표현

# 문제 설명
# Finn은 요즘 수학공부에 빠져 있습니다. 
# 수학 공부를 하던 Finn은 자연수 n을 연속한 자연수들로 표현 하는 방법이 
# 여러개라는 사실을 알게 되었습니다. 
# 예를들어 15는 다음과 같이 4가지로 표현 할 수 있습니다.

# 1 + 2 + 3 + 4 + 5 = 15
# 4 + 5 + 6 = 15
# 7 + 8 = 15
# 15 = 15
# 자연수 n이 매개변수로 주어질 때, 연속된 자연수들로 n을 표현하는 방법의 수를 
# return하는 solution를 완성해주세요.

# 제한사항
# n은 10,000 이하의 자연수 입니다.

n = 15
# result = 4

# 규칙찾기
# 3 > 1 3 > 1+2, 3 > 2
# 4 > 1 2 4 > 4 > 1
# 5 > 1 5 > 2+3, 5 > 2
# 6 > 1 2 3 6 > 1+2+3, 6 > 2
# 7 > 1 7 > 3+4, 7 > 2
# 8 > 1 2 4 8 > 8 > 1
# 9 > 1 3 9 > 2+3+4, 4+5 ,9 > 3
# 10 > 1 2 5 10 > 1+2+3+4, 10 > 2
# 11 > 1 11 > 2
# 12 > 1 2 3 4 6 12 > 3+4+5, 12 > 2
# >> 홀수인 약수 개수

# 약수찾기
answer=0
for i in range(1,int(n**(1/2))+1):
    if i**2==n: 
        if i%2==1: answer+=1
    elif n%i==0: 
        if i%2==1: answer+=1
        if n//i%2==1: answer+=1
print(answer)

# 제출용 함수
def solution(n):
    answer=0
    for i in range(1,int(n**(1/2))+1):
        if i**2==n: 
            if i%2==1: answer+=1
        elif n%i==0: 
            if i%2==1: answer+=1
            if n//i%2==1: answer+=1
    return answer