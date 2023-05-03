# https://school.programmers.co.kr/learn/courses/30/lessons/118666
# 성격 유형 검사하기

# 문제 설명

# 지표 번호	성격 유형
# 1번 지표	라이언형(R), 튜브형(T)
# 2번 지표	콘형(C), 프로도형(F)
# 3번 지표	제이지형(J), 무지형(M)
# 4번 지표	어피치형(A), 네오형(N)

# 각 질문은 1가지 지표로 성격 유형 점수를 판단합니다.

# 하지만 각 선택지는 고정적인 크기의 점수를 가지고 있습니다.

# 검사 결과는 모든 질문의 성격 유형 점수를 더하여 각 지표에서 
# 더 높은 점수를 받은 성격 유형이 검사자의 성격 유형이라고 판단합니다. 
# 단, 하나의 지표에서 각 성격 유형 점수가 같으면, 두 성격 유형 중 
# 사전 순으로 빠른 성격 유형을 검사자의 성격 유형이라고 판단합니다.

# 질문마다 판단하는 지표를 담은 1차원 문자열 배열 survey와 검사자가 
# 각 질문마다 선택한 선택지를 담은 1차원 정수 배열 choices가 
# 매개변수로 주어집니다. 이때, 검사자의 성격 유형 검사 결과를 
# 지표 번호 순서대로 return 하도록 solution 함수를 완성해주세요.

# 제한사항
# 1 ≤ survey의 길이 ( = n) ≤ 1,000
# survey의 원소는 "RT", "TR", "FC", "CF", "MJ", "JM", "AN", "NA" 중 하나입니다.
# survey[i]의 첫 번째 캐릭터는 i+1번 질문의 비동의 관련 선택지를 선택하면 받는 성격 유형을 의미합니다.
# survey[i]의 두 번째 캐릭터는 i+1번 질문의 동의 관련 선택지를 선택하면 받는 성격 유형을 의미합니다.
# choices의 길이 = survey의 길이

# choices[i]는 검사자가 선택한 i+1번째 질문의 선택지를 의미합니다.
# 1 ≤ choices의 원소 ≤ 7
# choices	뜻
# 1	매우 비동의
# 2	비동의
# 3	약간 비동의
# 4	모르겠음
# 5	약간 동의
# 6	동의
# 7	매우 동의

survey = ["AN", "CF", "MJ", "RT", "NA"]
choices = [5, 3, 2, 7, 5]
result = [5, 3, 2, 7, 5]

answer = ''
dic = {'R':0,'T':0,'C':0,'F':0,'J':0,'M':0,'A':0,'N':0}
for i in range(0,len(survey)):
    if choices[i] < 4:
        dic[survey[i][0]] += 4-choices[i]
    elif choices[i] > 4:
        dic[survey[i][1]] += choices[i]-4

dic2 = ['RT','CF','JM','AN']
for i in dic2:
    if dic[i[0]]>=dic[i[1]]: answer+=i[0]
    else: answer+=i[1]

print(answer)