# https://school.programmers.co.kr/learn/courses/30/lessons/12940
# 최대공약수와 최소공배수

# 문제 설명
# 두 수를 입력받아 두 수의 최대공약수와 최소공배수를 반환하는 함수, 
# solution을 완성해 보세요. 배열의 맨 앞에 최대공약수, 
# 그다음 최소공배수를 넣어 반환하면 됩니다. 
# 예를 들어 두 수 3, 12의 최대공약수는 3, 최소공배수는 12이므로 
# solution(3, 12)는 [3, 12]를 반환해야 합니다.

# 제한 사항
# 두 수는 1이상 1000000이하의 자연수입니다.

n = 3
m = 12
# return [3, 12]

answer = []
# 최대공약수 구하기
# 내림차순으로 range를 정해주고 두 수 다 나누어떨어지면
# 최대공약수
for i in range(min(n,m),0,-1):
    if n%i == 0 and m%i ==0 : 
        answer.append(i)
        break

# 최소공배수 구하기
# 오름차순으로 range를 정해주고 두 수로 나누어 떨어지면 최소공배수
for i in range(max(n,m),n*m+1):
    if i%n == 0 and i%m == 0 :
        answer.append(i)
        break

print(answer)

# 제출용 함수
def solution(n, m):
    answer = []
    for i in range(min(n,m),0,-1):
        if n%i == 0 and m%i ==0 : 
            answer.append(i)
            break
    for i in range(max(n,m),n*m+1):
        if i%n == 0 and i%m == 0 :
            answer.append(i)
            break
    return answer