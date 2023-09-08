# https://school.programmers.co.kr/learn/courses/30/lessons/181866

# 문자열 잘라서 정렬하기

# 문제 설명
# 문자열 myString이 주어집니다. "x"를 기준으로 해당 문자열을 잘라내 배열을 만든 후 사전순으로 정렬한 배열을 return 하는 solution 함수를 완성해 주세요.

# 단, 빈 문자열은 반환할 배열에 넣지 않습니다.

# 제한사항
# 1 ≤ myString ≤ 100,000
# myString은 알파벳 소문자로 이루어진 문자열입니다.


# 2차 수정 : 숏코딩
def solution(myString):
    return sorted([i for i in myString.split('x') if i])
# 6.23ms, 12.6MB


# 1차 수정 : 가독성 개선
def solution(myString):
    answer = myString.split('x')
    answer = sorted([i for i in answer if i])
    return answer
# 6.86ms, 12.4MB


# 초기 코드
def solution(myString):
    answer=[]
    s = ''
    for string in myString:
        if string != 'x':
            s += string
        else:
            if s != '':
                answer.append(s)
                s =''
    if s != '': answer.append(s)
    answer.sort()
    return answer
# 16.31ms, 12.3MB