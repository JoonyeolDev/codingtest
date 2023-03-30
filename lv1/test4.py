# https://school.programmers.co.kr/learn/courses/30/lessons/12928
# 약수의 합

# 문제 설명
# 정수 n을 입력받아 n의 약수를 모두 더한 값을 리턴하는 함수, 
# solution을 완성해주세요.

# 제한 사항
# n은 0 이상 3000이하인 정수입니다.

n = 12
arr = []
for i in range(1, int(n**(1/2)+1)):
    if n%i==0:
        arr.append(i)
        if i!=n//i:
            arr.append(n//i)
answer = sum(arr)
print(answer)

# 제출용 함수
def solution(n):
    arr = []
    for i in range(1, int(n**(1/2)+1)):
        if n%i==0:
            arr.append(i)
            if i!=n//i:
                arr.append(n//i)
    answer = sum(arr)
    return answer