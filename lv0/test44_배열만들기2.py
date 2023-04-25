# https://school.programmers.co.kr/learn/courses/30/lessons/181921?language=python3
# 배열 만들기 2

# 문제 설명
# 정수 l과 r이 주어졌을 때, l 이상 r이하의 정수 중에서 숫자 "0"과 "5"로만
# 이루어진 모든 정수를 오름차순으로 저장한 배열을 return 하는 
# solution 함수를 완성해 주세요.

# 만약 그러한 정수가 없다면, -1이 담긴 배열을 return 합니다.

l = 10
r = 20

answer = []
for i in range(l,r+1):
    if str(i).replace('5','').replace('0','')=='': answer.append(i)
if answer == []: answer.append(-1)
print(answer)