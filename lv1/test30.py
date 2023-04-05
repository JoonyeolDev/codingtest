# https://school.programmers.co.kr/learn/courses/30/lessons/77884
# 약수의 개수와 덧셈

# 문제 설명
# 두 정수 left와 right가 매개변수로 주어집니다. 
# left부터 right까지의 모든 수들 중에서, 약수의 개수가 짝수인 수는 더하고, 
# 약수의 개수가 홀수인 수는 뺀 수를 return 하도록 solution 함수를 완성해주세요.

# 제한사항
# 1 ≤ left ≤ right ≤ 1,000

left = 13
right = 17
# result = 43

# 약수의 갯수 구하기
def find_divisor(number):
    count = 0
    # 시간복잡도 낮추기 위해 제곱근까지만 실행
    for i in range(1,int(number**(1/2))+1):
        # i가 제곱근이면 count+1
        if number == i**2: count+=1
        elif number%i==0: count+=2
    return count

answer = 0
for i in range(left,right+1):
    if find_divisor(i)%2 == 0: answer+=i
    else: answer-=i
print(answer)

# 제출용 함수
def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        if find_divisor(i)%2 == 0: answer+=i
        else: answer-=i
    return answer