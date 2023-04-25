# https://school.programmers.co.kr/learn/courses/30/lessons/120815
# 피자 나눠 먹기 (2)

# 문제 설명
# 머쓱이네 피자가게는 피자를 여섯 조각으로 잘라 줍니다. 
# 피자를 나눠먹을 사람의 수 n이 매개변수로 주어질 때, 
# n명이 주문한 피자를 남기지 않고 모두 같은 수의 피자 조각을 먹어야 한다면 
# 최소 몇 판을 시켜야 하는지를 return 하도록 solution 함수를 완성해보세요.

# 제한사항
# 1 ≤ n ≤ 100

# 최소공배수 물어보는건가?
pizza = [6,3,2,1]
n = 4
for i in pizza:
    if n%i==0: 
        answer = n//i
        break
print(answer)

# 제출용 함수
def solution(n):
    pizza = [6,3,2,1]
    for i in pizza:
        if n%i==0: 
            answer = n//i
            break
    return answer

# 하드코딩
def solution2(n):
    answer = 0
    if n%6==0: answer=n//6
    elif n%2==0: answer=n//2
    elif n%3==0: answer=n//3
    else : answer=n
    return answer