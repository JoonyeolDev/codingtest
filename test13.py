# https://school.programmers.co.kr/learn/courses/30/lessons/120814
# 피자 나눠 먹기 (1)

# 문제 설명
# 머쓱이네 피자가게는 피자를 일곱 조각으로 잘라 줍니다. 
# 피자를 나눠먹을 사람의 수 n이 주어질 때, 
# 모든 사람이 피자를 한 조각 이상 먹기 위해 필요한 피자의 수를 
# return 하는 solution 함수를 완성해보세요.

# 제한사항
# 1 ≤ n ≤ 100

# 피자 한판에 7조각
# n <= pizza*7
# 즉 pazza >= n/7 을 만족하는 자연수 최소값을 찾으면 된다
n = 8
a=0
if n%7 !=0:a=1
answer = n//7 + a

# 제출용 함수
def solution(n):
    a=0
    if n%7 !=0:a=1
    answer = n//7 + a
    return answer

# for문으로 풀기
def solution2(n):
    for i in range(16):
        if i*7>=n : 
            answer = i
            break
    return answer