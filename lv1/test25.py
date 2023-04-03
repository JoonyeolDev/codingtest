# https://school.programmers.co.kr/learn/courses/30/lessons/12903
# 가운데 글자 가져오기

# 문제 설명
# 단어 s의 가운데 글자를 반환하는 함수, solution을 만들어 보세요. 
# 단어의 길이가 짝수라면 가운데 두글자를 반환하면 됩니다.

# 제한사항
# s는 길이가 1 이상, 100이하인 스트링입니다.

s = "qwer"

if len(s)%2 == 0: answer = s[len(s)-1:len(s)]

answer = s[len(s)//2-1:len(s)//2+1] if len(s)%2 == 0 else s[len(s)//2]

print(answer)

# 제출용 함수
def solution(s):
    answer = s[len(s)//2-1:len(s)//2+1] if len(s)%2 == 0 else s[len(s)//2]
    return answer