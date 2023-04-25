# https://school.programmers.co.kr/learn/courses/30/lessons/120888
# 중복된 문자 제거

# 문제 설명
# 문자열 my_string이 매개변수로 주어집니다. 
# my_string에서 중복된 문자를 제거하고 하나의 문자만 남긴 문자열을 
# return하도록 solution 함수를 완성해주세요.

# 제한사항
# 1 ≤ my_string ≤ 110
# my_string은 대문자, 소문자, 공백으로 구성되어 있습니다.
# 대문자와 소문자를 구분합니다.
# 공백(" ")도 하나의 문자로 구분합니다.
# 중복된 문자 중 가장 앞에 있는 문자를 남깁니다.

my_string = "We are the world"
answer=''
# set?
set_str = set(my_string)
# set을 쓰면 순서가 바뀜
print(set_str)


# for?
for i in my_string:
    if answer.count(i) == 0: answer+=i
print(answer)

# 제출용 함수
def solution(my_string):
    answer=''
    for i in my_string:
        if answer.count(i) == 0: answer+=i
    return answer

# count함수 안쓰고
def solution2(my_string):
    answer = ''
    for i in my_string:
        count=0
        for j in answer:
            if j==i:count+=1
        if count>0:continue
        else:answer+=i
    return answer