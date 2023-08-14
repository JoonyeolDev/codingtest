# https://school.programmers.co.kr/learn/courses/30/lessons/12921
# 소수 찾기

# 문제 설명
# 1부터 입력받은 숫자 n 사이에 있는 소수의 개수를 반환하는 함수, 
# solution을 만들어 보세요.

# 소수는 1과 자기 자신으로만 나누어지는 수를 의미합니다.
# (1은 소수가 아닙니다.)

# 제한 조건
# n은 2이상 1000000이하의 자연수입니다.

n = 1000000

answer = 0
# 소수를 찾으면 answer +1
for i in range(2,n+1):
    count=0
    for j in range(1, int(i**(1/2))+1):
        if i%j == 0: count+=1
    if count ==1: answer+=1

print(answer)

# 시간초과로 실패, 더 효율적인 방법을 찾아야 한다
for i in range(2,n+1):
    count=0
    for j in range(2, int(i**(1/2))+1):
        if i%j == 0: 
            count+=1
            break
    if count ==0: answer+=1