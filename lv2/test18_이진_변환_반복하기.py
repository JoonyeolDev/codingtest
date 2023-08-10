# https://school.programmers.co.kr/learn/courses/30/lessons/70129
# 이진 변환 반복하기

# 문제 설명
# 0과 1로 이루어진 어떤 문자열 x에 대한 이진 변환을 다음과 같이 정의합니다.

# x의 모든 0을 제거합니다.
# x의 길이를 c라고 하면, x를 "c를 2진법으로 표현한 문자열"로 바꿉니다.
# 예를 들어, x = "0111010"이라면, x에 이진 변환을 가하면 
# x = "0111010" -> "1111" -> "100" 이 됩니다.

# 0과 1로 이루어진 문자열 s가 매개변수로 주어집니다. 
# s가 "1"이 될 때까지 계속해서 s에 이진 변환을 가했을 때, 
# 이진 변환의 횟수와 변환 과정에서 제거된 모든 0의 개수를 각각 배열에 담아 
# return 하도록 solution 함수를 완성해주세요.

# 제한사항
# s의 길이는 1 이상 150,000 이하입니다.
# s에는 '1'이 최소 하나 이상 포함되어 있습니다.

s = "110010101001"
# result = [3,8]


# 2차 수정 : 변수 할당
def solution(s):
    del_sum = 0
    count = 0
    while s != '1':
        len_s = len(s)
        one_count = s.count('1')
        zero_count = len_s - one_count
        del_sum += zero_count
        s = bin(one_count).lstrip('0b')
        count+=1
    return [count,del_sum]
# 0.50ms


# 1차 수정 : 가독성 개선
def solution(s):
    del_sum = 0
    count = 0
    while s != '1':
        one_count = s.count('1')
        del_sum += len(s) - one_count
        s = bin(one_count).lstrip('0b')
        count+=1
    return [count,del_sum]
# 0.59ms


# 초기 코드
def dec_to_bin(s,bin=""):
    if s==0: return bin
    return dec_to_bin(s//2,bin=str(s%2)+bin)

def solution(s):
    del_sum = 0
    count = 0
    while True:
        new_s = s.replace("0","")
        del_sum += len(s)-len(new_s)
        new_s = dec_to_bin(len(new_s))
        count+=1
        if new_s == "1": break
        s = new_s
    answer = [count,del_sum]
    return answer
# 2.02ms