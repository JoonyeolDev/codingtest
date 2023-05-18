# https://school.programmers.co.kr/learn/courses/30/lessons/12945
# 피보나치 수

# 문제 설명
# 피보나치 수는 F(0) = 0, F(1) = 1일 때, 
# 1 이상의 n에 대하여 F(n) = F(n-1) + F(n-2) 가 적용되는 수 입니다.

# 예를들어

# F(2) = F(0) + F(1) = 0 + 1 = 1
# F(3) = F(1) + F(2) = 1 + 1 = 2
# F(4) = F(2) + F(3) = 1 + 2 = 3
# F(5) = F(3) + F(4) = 2 + 3 = 5
# 와 같이 이어집니다.

# 2 이상의 n이 입력되었을 때, n번째 피보나치 수를 1234567으로 나눈 나머지를 리턴하는 함수, 
# solution을 완성해 주세요.

# 제한 사항
# n은 2 이상 100,000 이하인 자연수입니다.

# 재귀함수 사용하기
# def fibonacci(n, k=1, f_prepre=0, f_pre=1, f=1):
#     if k>n: return f
#     return fibonacci(n, k+1, f_pre, f, f_prepre+f_pre)
def fibonacci(n,a=0,b=1,k=1):
    if k == n: return b
    return fibonacci(n,b,a+b,k+1)

def solution(n):
    answer = fibonacci(n) % 1234567
    return answer

def solution2(n):
    count = 1
    f_prepre = 0
    f_pre = 1
    while True:
        f= f_prepre + f_pre
        count += 1
        if count == n:
            break
        f_prepre,f_pre = f_pre,f
    answer = f%1234567
    return answer

