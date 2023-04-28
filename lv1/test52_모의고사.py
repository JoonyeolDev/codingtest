# https://school.programmers.co.kr/learn/courses/30/lessons/42840
# 모의고사

# 문제 설명
# 수포자는 수학을 포기한 사람의 준말입니다. 수포자 삼인방은 모의고사에 수학 문제를
# 전부 찍으려 합니다. 수포자는 1번 문제부터 마지막 문제까지 다음과 같이 찍습니다.

# 1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
# 2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
# 3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...

# 1번 문제부터 마지막 문제까지의 정답이 순서대로 들은 배열 answers가 주어졌을 때,
# 가장 많은 문제를 맞힌 사람이 누구인지 배열에 담아 return 하도록 
# solution 함수를 작성해주세요.

# 제한 조건
# 시험은 최대 10,000 문제로 구성되어있습니다.
# 문제의 정답은 1, 2, 3, 4, 5중 하나입니다.
# 가장 높은 점수를 받은 사람이 여럿일 경우, return하는 값을 오름차순 정렬해주세요.

answers = [1,3,2,4,2]

answer = []
arr = []
# 일단 수포자들 찍는 패턴 일반화
supoja_1 = [1, 2, 3, 4, 5]
supoja_2 = [2, 1, 2, 3, 2, 4, 2, 5]
supoja_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
# 이거 걍 한수열에 넣어서 for문 돌리자
supojas = [supoja_1, supoja_2, supoja_3]
# answers가 몇개 주어지든 인덱스를 len(수포자)로 나눈 나머지를 구하면 쉬울듯
for supoja in supojas:
    count = 0
    for idx,value in enumerate(answers):
        if value==supoja[idx%len(supoja)]: count+=1
    arr.append(count)
# max값 찾아서 arr값과 비교, 같으면 answer에 추가 
# 근데 max가 0이면 공백 ㄱ
if max(arr) != 0:
    for idx,value in enumerate(arr):
        if max(arr)==value: answer.append(idx+1)

print(answer)