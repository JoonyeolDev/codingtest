# https://school.programmers.co.kr/learn/courses/30/lessons/76502
# 괄호 회전하기

# 문제 설명
# 다음 규칙을 지키는 문자열을 올바른 괄호 문자열이라고 정의합니다.

# (), [], {} 는 모두 올바른 괄호 문자열입니다.
# 만약 A가 올바른 괄호 문자열이라면, (A), [A], {A} 도 올바른 괄호 문자열입니다. 예를 들어, [] 가 올바른 괄호 문자열이므로, ([]) 도 올바른 괄호 문자열입니다.
# 만약 A, B가 올바른 괄호 문자열이라면, AB 도 올바른 괄호 문자열입니다. 
# 예를 들어, {} 와 ([]) 가 올바른 괄호 문자열이므로, {}([]) 도 올바른 괄호 문자열입니다.
# 대괄호, 중괄호, 그리고 소괄호로 이루어진 문자열 s가 매개변수로 주어집니다. 
# 이 s를 왼쪽으로 x (0 ≤ x < (s의 길이)) 칸만큼 회전시켰을 때 
# s가 올바른 괄호 문자열이 되게 하는 x의 개수를 return 하도록 solution 함수를 완성해주세요.

# 제한사항
# s의 길이는 1 이상 1,000 이하입니다.

# 판별 함수를 만들어서 정상이면 1 아니면 0
# s*2하고 len(s)만큼 잘라서 판별함수 돌리기

s = "[](){}"
# result = 3


# 1차 수정 : 가독성 개선
from collections import deque
def is_correct(string):
    stack = deque()
    bracket_dict = {'(':')','{':'}','[':']'}
    for s in string:
        if s in '({[':
            stack.append(bracket_dict[s])
        else:
            if not stack or stack.pop() != s:
                return 0
    return 0 if stack else 1

def solution(s):
    len_s = len(s)
    if len_s % 2 == 1: return 0
    s = s*2
    answer = 0
    for i in range(len_s):
        new_s = s[i:i+len_s]
        answer += is_correct(new_s)
    return answer
# 41.31ms, 10.1MB


# 초기 코드
from collections import deque
def is_correct(string):
    stack = deque()
    bracket_dict = {'(':')','{':'}','[':']'}
    for s in string:
        if s in '({[':
            stack.append(bracket_dict[s])
        else:
            if not stack:
                return 0
            peak = stack.pop()
            if peak != s:
                return 0
    if stack: return 0
    return 1

def solution(s):
    len_s = len(s)
    if len_s % 2 == 1: return 0
    s = s*2
    answer = 0
    for i in range(len_s):
        answer += is_correct(s[i:i+len_s])
    return answer
# 88.81ms, 10.2MB