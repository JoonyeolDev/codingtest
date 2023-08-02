# https://school.programmers.co.kr/learn/courses/30/lessons/17682
# [1차] 다트 게임

# 문제 설명
#  다트 게임의 점수 계산 로직은 아래와 같다.

# 다트 게임은 총 3번의 기회로 구성된다.
# 각 기회마다 얻을 수 있는 점수는 0점에서 10점까지이다.
# 점수와 함께 Single(S), Double(D), Triple(T) 영역이 존재하고 각 영역 당첨 시 
# 점수에서 1제곱, 2제곱, 3제곱 (점수1 , 점수2 , 점수3 )으로 계산된다.
# 옵션으로 스타상(*) , 아차상(#)이 존재하며 스타상(*) 당첨 시 해당 점수와 바로 
# 전에 얻은 점수를 각 2배로 만든다. 아차상(#) 당첨 시 해당 점수는 마이너스된다.
# 스타상(*)은 첫 번째 기회에서도 나올 수 있다. 
# 이 경우 첫 번째 스타상(*)의 점수만 2배가 된다. (예제 4번 참고)
# 스타상(*)의 효과는 다른 스타상(*)의 효과와 중첩될 수 있다. 
# 이 경우 중첩된 스타상(*) 점수는 4배가 된다. (예제 4번 참고)
# 스타상(*)의 효과는 아차상(#)의 효과와 중첩될 수 있다. 
#  이 경우 중첩된 아차상(#)의 점수는 -2배가 된다. (예제 5번 참고)
# Single(S), Double(D), Triple(T)은 점수마다 하나씩 존재한다.
# 스타상(*), 아차상(#)은 점수마다 둘 중 하나만 존재할 수 있으며, 존재하지 않을 수도 있다.
# 0~10의 정수와 문자 S, D, T, *, #로 구성된 문자열이 입력될 시 
# 총점수를 반환하는 함수를 작성하라.

# 입력 형식
# "점수|보너스|[옵션]"으로 이루어진 문자열 3세트.
# 예) 1S2D*3T

# 점수는 0에서 10 사이의 정수이다.
# 보너스는 S, D, T 중 하나이다.
# 옵선은 *이나 # 중 하나이며, 없을 수도 있다.
# 출력 형식
# 3번의 기회에서 얻은 점수 합계에 해당하는 정수값을 출력한다.
# 예) 37


# score = []
# for i in dartResult:
#     num = 0
#     if i.isnumeric():
#         num = int(i)
#     elif i == 'D':
#         num **= 2
#     elif i == 'T':
#         num **= 3
#     elif i == '#':
#         num *= -1
#     score.append(num)
# print(score)


# replace랑 eval 써서 풀어보기

# for idx,value in enumerate(dartResult):
#     if value == '#' or value == '*':
        # option.append(idx)

# 첫숫자**첫문자*(가중치)+ 이런형태임
def score(num, string):
    if string=='S': string = 1
    elif string=='D': string = 2
    elif string =='T': string = 3
    answer = int(num)**string
    return answer

# 앞에서 3개를 검색하고 옵션 확인
# 10일때 처리 해야함
# while len(dartResult) >= 2:
#     if len(dartResult) == 2:
#         arr.append(dartResult[:2])
#         arr.append('')
#         break
#     if dartResult[2] == '*' or dartResult[2] == '#':
#         arr.append(dartResult[:2])
#         arr.append(dartResult[2])
#         dartResult = dartResult[3:]
#     else :
#         arr.append(dartResult[:2])
#         arr.append('')
#         dartResult = dartResult[2:]

dartResult = '1S*2T*3S'
arr = []
while len(dartResult) != 0:
    if dartResult[0:2] == '10':
        arr.append(dartResult[0:2])
        dartResult = dartResult[2:]
    else: 
        arr.append(dartResult[0:1])
        dartResult = dartResult[1:]
    if dartResult[0] == 'S':
        arr.append('**1')
    elif dartResult[0] == 'D':
        arr.append('**2')
    elif dartResult[0] == 'T':
        arr.append('**3')
    dartResult = dartResult[1:]
    if len(dartResult)==0: break
    if dartResult[0] == '*' or dartResult[0] == '#':
        arr.append(dartResult[0])
        dartResult = dartResult[1:]
    else:
        arr.append('+')
for idx,value in enumerate(arr[::]):
    if value == '*':
        arr[idx] = '*2+'
        if idx != 2:
            arr[idx-3] = '*2'+arr[idx-3]
    elif value == '#':
        arr[idx] = '*(-1)+'
sum_str = ''.join(arr)
if sum_str[-1] =='+': sum_str=sum_str[:-1]
answer = eval(sum_str)

# answer = arr[0]+arr[3]+arr[6]
# print(arr)
# print(answer)

dartResult = '1D#2S*3S'
arr = []
temp = 0
dartResult = dartResult.replace('10','a')
for i,v in enumerate(dartResult[1:]):
    if v.isnumeric():
        arr.append(dartResult[temp:i+1])
        temp=i+1
    if v=='a':
        arr.append(dartResult[temp:i+1])
        temp=i+1
arr.append(dartResult[temp:])
print(arr)
for i in range(3):
    if '*' in arr[i] :
        arr[i]=arr[i].replace('*','*2')
        if i != 0:
            arr[i-1]+='*2'
s = '+'.join(arr).replace('S','**1').replace('D','**2').replace('T','**3').replace('#','*(-1)').replace('a','10')
answer = eval(s)
print(s)

def solution(dartResult):
    arr = []
    temp = 0
    dartResult = dartResult.replace('10','a')
    for i,v in enumerate(dartResult[1:]):
        if v.isnumeric():
            arr.append(dartResult[temp:i+1])
            temp=i
        if v=='a':
            arr.append(dartResult[temp:i+1])
            temp=i
    arr.append(dartResult[temp:])
    for i in range(3):
        if '*' in arr[i] :
            arr[i]=arr[i].replace('*','*2')
            if i != 0:
                arr[i-1]+='*2'
    s = '+'.join(arr).replace('S','**1').replace('D','**2').replace('T','**3').replace('#','*(-1)').replace('a','10')
    answer = eval(s)
    return answer