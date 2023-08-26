# https://school.programmers.co.kr/learn/courses/30/lessons/181871
# 문자열이 몇 번 등장하는지 세기

# 문제 설명
# 문자열 myString과 pat이 주어집니다. myString에서 pat이 등장하는 횟수를 return 하는 solution 함수를 완성해 주세요.

# 제한사항
# 1 ≤ myString ≤ 1000
# 1 ≤ pat ≤ 10

myString = "banana"
pat = "ana"
# result = 2

def solution(myString, pat):
    len_pat = len(pat)
    answer = 0
    for i in range(len(myString)-len_pat+1):
        if myString[i:i+len_pat] == pat:
            answer += 1
    return answer