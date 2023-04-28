# https://school.programmers.co.kr/learn/courses/30/lessons/172928
# 공원 산책

# 문제 설명
# 지나다니는 길을 'O', 장애물을 'X'로 나타낸 직사각형 격자 모양의 
# 공원에서 로봇 강아지가 산책을 하려합니다. 
# 산책은 로봇 강아지에 미리 입력된 명령에 따라 진행하며, 
# 명령은 다음과 같은 형식으로 주어집니다.
# ["방향 거리", "방향 거리" … ]
# 예를 들어 "E 5"는 로봇 강아지가 현재 위치에서 동쪽으로 5칸 이동했다는 의미입니다.
# 로봇 강아지는 명령을 수행하기 전에 다음 두 가지를 먼저 확인합니다.

# 주어진 방향으로 이동할 때 공원을 벗어나는지 확인합니다.
# 주어진 방향으로 이동 중 장애물을 만나는지 확인합니다.
# 위 두 가지중 어느 하나라도 해당된다면, 로봇 강아지는 해당 명령을 무시하고 다음 명령을 수행합니다.
# 공원의 가로 길이가 W, 세로 길이가 H라고 할 때, 공원의 좌측 상단의 좌표는 (0, 0), 우측 하단의 좌표는 (H - 1, W - 1) 입니다.

# 공원을 나타내는 문자열 배열 park, 
# 로봇 강아지가 수행할 명령이 담긴 문자열 배열 routes가 매개변수로 주어질 때, 
# 로봇 강아지가 모든 명령을 수행 후 놓인 위치를 
# [세로 방향 좌표, 가로 방향 좌표] 순으로 배열에 담아 
# return 하도록 solution 함수를 완성해주세요.

# 제한사항
# 3 ≤ park의 길이 ≤ 50
# 3 ≤ park[i]의 길이 ≤ 50
# park[i]는 다음 문자들로 이루어져 있으며 시작지점은 하나만 주어집니다.
# S : 시작 지점
# O : 이동 가능한 통로
# X : 장애물
# park는 직사각형 모양입니다.
# 1 ≤ routes의 길이 ≤ 50
# routes의 각 원소는 로봇 강아지가 수행할 명령어를 나타냅니다.
# 로봇 강아지는 routes의 첫 번째 원소부터 순서대로 명령을 수행합니다.
# routes의 원소는 "op n"과 같은 구조로 이루어져 있으며, op는 이동할 방향, n은 이동할 칸의 수를 의미합니다.
# op는 다음 네 가지중 하나로 이루어져 있습니다.
# N : 북쪽으로 주어진 칸만큼 이동합니다.
# S : 남쪽으로 주어진 칸만큼 이동합니다.
# W : 서쪽으로 주어진 칸만큼 이동합니다.
# E : 동쪽으로 주어진 칸만큼 이동합니다.
# 1 ≤ n ≤ 9

park = ["SOO","OOO","OOO"]
routes = ["E 2","S 2","W 1"]

# 가로세로 크기 구하기
h = len(park)-1 # 세로 x
w = len(park[0])-1 # 가로 y

# "S" 위치찾기 "S"는 한개밖에 없다
for i in range(len(park)):
    for j in range(len(park[i])):
        if park[i][j]=="S":
            s = [i,j]
            break

# 모든 "X" 위치찾기
x= []
for i in range(len(park)):
    for j in range(len(park[i])):
        if park[i][j]=="X":
            x.append([i,j])

# 이동 리스트 만들기
arr=[]
for i in routes:
    if i[0]=='E': arr.append([0,int(i[2])])
    if i[0]=='W': arr.append([0,-int(i[2])])
    if i[0]=='N': arr.append([-int(i[2]),0])
    if i[0]=='S': arr.append([int(i[2]),0])

# s의 값을 따로 저장 .copy를 쓰면 깊은 복사가 가능하다
s_org = s.copy()
count = 0

# 이동리스트에서 하나씩 값을 빼고
for i in arr:
    # 한칸씩 이동할건데 몇번 반복할건지 re로 정의
    re = abs(i[0]+i[1])
    # re만큼 한칸씩 이동
    for j in range(1,re+1):
        s = [s[0]+int(i[0]/re),s[1]+int(i[1]/re)]
        # 한칸씩 이동할 때마다 x리스트와 비교해서 값이 같으면 count
        if x.count(s) != 0: count+=1
    # for문이 끝났을때 count가 0이 아니면 값 초기화
    if count != 0: 
        s = s_org.copy()
        count = 0
    else :
        # 이동 완료 후 park를 벗어났는지 확인
        if h>=s[0]>=0 and w>=s[1]>=0: s_org=s.copy()
        else: s = s_org.copy()

answer = s
print(answer)



def solution(park, routes):
    h = len(park)-1
    w = len(park[0])-1
    for i in range(len(park)):
        for j in range(len(park[i])):
            if park[i][j]=="S":
                s = [i,j]
                break
    x= []
    for i in range(len(park)):
        for j in range(len(park[i])):
            if park[i][j]=="X":
                x.append([i,j])
    arr=[]
    for i in routes:
        if i[0]=='E': arr.append([0,int(i[2])])
        if i[0]=='W': arr.append([0,-int(i[2])])
        if i[0]=='N': arr.append([-int(i[2]),0])
        if i[0]=='S': arr.append([int(i[2]),0])
    s_org = s.copy()
    count = 0
    for i in arr:
        re = abs(i[0]+i[1])
        for j in range(1,re+1):
            s = [s[0]+int(i[0]/re),s[1]+int(i[1]/re)]
            if x.count(s) != 0: count+=1
        if count != 0: 
            s = s_org.copy()
            count = 0
        else :
            if h>=s[0]>=0 and w>=s[1]>=0: s_org=s.copy()
            else: s = s_org.copy()
    answer = s
    return answer