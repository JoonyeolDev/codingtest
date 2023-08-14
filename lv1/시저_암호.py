# https://school.programmers.co.kr/learn/courses/30/lessons/12926
# 시저 암호

# 문제 설명
# 어떤 문장의 각 알파벳을 일정한 거리만큼 밀어서 다른 알파벳으로 바꾸는 
# 암호화 방식을 시저 암호라고 합니다. 예를 들어 "AB"는 1만큼 밀면 "BC"가 되고, 
# 3만큼 밀면 "DE"가 됩니다. "z"는 1만큼 밀면 "a"가 됩니다. 
# 문자열 s와 거리 n을 입력받아 s를 n만큼 민 암호문을 만드는 함수, 
# solution을 완성해 보세요.

# 제한 조건
# 공백은 아무리 밀어도 공백입니다.
# s는 알파벳 소문자, 대문자, 공백으로만 이루어져 있습니다.
# s의 길이는 8000이하입니다.
# n은 1 이상, 25이하인 자연수입니다.

s = "z z"
n = 1

answer = ''
# n만큼 밀어서 알파벳 교환, ord랑 chr 쓰면 될듯?
for i in s:
    # 공백은 밀어도 공백
    if i == ' ': answer+=i
    # z 다음엔 a로 돌아감 ord(z) = 122
    elif ord(i.lower())+n > 122:
        answer += chr(ord(i)+n-26)
    else: answer += chr(ord(i)+n)
print(answer)

