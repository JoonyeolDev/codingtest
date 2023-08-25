# https://school.programmers.co.kr/learn/courses/30/lessons/17684
# [3차] 압축

# 문제 설명
# 어피치는 여러 압축 알고리즘 중에서 성능이 좋고 구현이 간단한 LZW(Lempel–Ziv–Welch) 압축을 구현하기로 했다. 
# LZW 압축은 다음 과정을 거친다.

# 길이가 1인 모든 단어를 포함하도록 사전을 초기화한다.
# 사전에서 현재 입력과 일치하는 가장 긴 문자열 w를 찾는다.
# w에 해당하는 사전의 색인 번호를 출력하고, 입력에서 w를 제거한다.
# 입력에서 처리되지 않은 다음 글자가 남아있다면(c), w+c에 해당하는 단어를 사전에 등록한다.
# 단계 2로 돌아간다.
# 압축 알고리즘이 영문 대문자만 처리한다고 할 때, 사전은 다음과 같이 초기화된다. 사전의 색인 번호는 정수값으로 주어지며, 1부터 시작한다고 하자.

# 색인 번호	1	2	3	...	24	25	26
#     단어	A	B	C	...	X	Y	Z

# 입력 형식
# 입력으로 영문 대문자로만 이뤄진 문자열 msg가 주어진다. msg의 길이는 1 글자 이상, 1000 글자 이하이다.

# 출력 형식
# 주어진 문자열을 압축한 후의 사전 색인 번호를 배열로 출력하라.

# A-Z > 1-26  딕셔너리 만들기
# 문자 길이별로 딕셔너리에 넣어서 값이 있다면 갱신, 없다면 break

msg = 'TOBEORNOTTOBEORTOBEORNOT'
# result = [20, 15, 2, 5, 15, 18, 14, 15, 20, 27, 29, 31, 36, 30, 32, 34]


# 1차 수정 : 가독성 개선
def solution(msg):
    alpha_dict = {chr(i): i - 64 for i in range(65, 91)}
    value = 27
    answer = []
    idx = 0
    while idx < len(msg):
        i = 1
        while idx + i <= len(msg) and msg[idx:idx + i] in alpha_dict:
            i += 1
        if idx + i <= len(msg):
            alpha_dict[msg[idx:idx + i]] = value
            value += 1
        answer.append(alpha_dict[msg[idx:idx + i - 1]])
        idx += i - 1
    return answer
# 0.74ms, 10.2MB


# 초기 코드
def solution(msg):
    idx = 0
    value = 27
    answer = []
    alpha_dict = {}
    for i in range(65,91):
        alpha_dict[chr(i)] = i-64

    while idx < len(msg):
        i = 1
        while idx+i <= len(msg):
            s = msg[idx:idx+i]
            if not alpha_dict.get(s, 0):
                answer.append(alpha_dict[s[:-1]])
                alpha_dict[s] = value
                value += 1
                i -= 1
                break
            i += 1
        else: answer.append(alpha_dict[s])
        idx += i
    return answer
# 1.12ms, 10.3MB



