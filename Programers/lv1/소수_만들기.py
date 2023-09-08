# https://school.programmers.co.kr/learn/courses/30/lessons/12977
# 소수 만들기

# 문제 설명
# 주어진 숫자 중 3개의 수를 더했을 때 소수가 되는 경우의 개수를 구하려고 합니다.
# 숫자들이 들어있는 배열 nums가 매개변수로 주어질 때, 
# nums에 있는 숫자들 중 서로 다른 3개를 골라 더했을 때 소수가 되는 경우의 개수를
# return 하도록 solution 함수를 완성해주세요.

# 제한사항
# nums에 들어있는 숫자의 개수는 3개 이상 50개 이하입니다.
# nums의 각 원소는 1 이상 1,000 이하의 자연수이며, 중복된 숫자가 들어있지 않습니다.

nums = [1,2,7,6,4]

# 비슷한 문제가 너무 많다
# 일단 3개 콤비네이션부터 구하고

answer = 0
for i in range(len(nums)-2):
    for j in range(i+1,len(nums)-1):
        for k in range(j+1,len(nums)):
            # number[i],number[j],number[k]가 이제 3개 수 combinations가 된다
            # 이걸 모두 더했을 때 소수가 되면 answer +1
            sum_number=nums[i]+nums[j]+nums[k]
            count = 0
            for n in range(2,int((sum_number**(1/2)))+1):
                if sum_number%n==0:
                    count+=1
                    break
            if count==0: answer+=1
print(answer)

# 제출용 함수
def solution(nums):
    answer = 0
    for i in range(len(nums)-2):
        for j in range(i+1,len(nums)-1):
            for k in range(j+1,len(nums)):
                sum_number=nums[i]+nums[j]+nums[k]
                count = 0
                for n in range(2,int((sum_number**(1/2)))+1):
                    if sum_number%n==0:
                        count+=1
                        break
                if count==0: answer+=1
    return answer