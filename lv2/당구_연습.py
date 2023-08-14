# https://school.programmers.co.kr/learn/courses/30/lessons/169198
# 당구 연습

# 문제 설명
# 당구대의 가로 길이 m, 세로 길이 n과 머쓱이가 쳐야 하는 공이 놓인 위치 좌표를
# 나타내는 두 정수 startX, startY, 그리고 매 회마다 목표로 해야하는 
# 공들의 위치 좌표를 나타내는 정수 쌍들이 들어있는 2차원 정수배열 balls가 주어집니다.
# "원쿠션" 연습을 위해 머쓱이가 공을 적어도 벽에 한 번은 맞춘 후 목표 공에 맞힌다고 할 때, 
# 각 회마다 머쓱이가 친 공이 굴러간 거리의 최솟값의 제곱을 배열에 담아
# return 하도록 solution 함수를 완성해 주세요.

# 단, 머쓱이가 친 공이 벽에 부딪힐 때 진행 방향은 항상 입사각과 반사각이 동일하며, 
# 만약 꼭짓점에 부딪힐 경우 진입 방향의 반대방향으로 공이 진행됩니다. 
# 공의 크기는 무시하며, 두 공의 좌표가 정확히 일치하는 경우에만 
# 두 공이 서로 맞았다고 판단합니다. 공이 목표 공에 맞기 전에 멈추는 경우는 없으며, 
# 목표 공에 맞으면 바로 멈춘다고 가정합니다.


# 제한사항
# 3 ≤ m, n ≤ 1,000
# 0 < startX < m
# 0 < startY < n
# 2 ≤ balls의 길이 ≤ 1,000
# balls의 원소는 [a, b] 형태입니다.
# a, b는 머쓱이가 맞춰야 할 공이 놓인 좌표를 의미합니다.
# 0 < a < m, 0 < b < n
# (a, b) = ( startX, startY )인 입력은 들어오지 않습니다.

# m,n,startX,startY,balls = 10,10,3,7,[[7, 7], [2, 7], [7, 3]]
m,n,startX,startY,balls = 3, 3, 1, 1, [[1, 2]]
# result = [52, 37, 116]

# 4면 모두 찾아야함
# 가로 0, 10, 세로 0, 10
answer = []
start = [startX,startY]
start_list = [[-startX,startY],[startX,-startY],[2*m-startX,startY],[startX,2*n-startY]]
for ball in balls:
    arr=[]
    for start_ball in start_list:
        if ball[0]==start_ball[0] or ball[1]==start_ball[1]: 
            if ((ball[0]-start_ball[0])**2+(ball[1]-start_ball[1])**2) < ((start[0]-start_ball[0])**2+(start[1]-start_ball[1])**2): continue
        arr.append((ball[0]-start_ball[0])**2+(ball[1]-start_ball[1])**2)
    answer.append(min(arr))
print(answer)


def solution(m, n, startX, startY, balls):
    answer = []
    start = [startX,startY]
    start_list = [[-startX,startY],[startX,-startY],[2*m-startX,startY],[startX,2*n-startY]]
    for ball in balls:
        arr=[]
        for start_ball in start_list:
            if ball[0]==start_ball[0] or ball[1]==start_ball[1]: 
                if ((ball[0]-start_ball[0])**2+(ball[1]-start_ball[1])**2) > ((start[0]-start_ball[0])**2+(start[1]-start_ball[1])**2):
                    arr.append((ball[0]-start_ball[0])**2+(ball[1]-start_ball[1])**2)
        answer.append(min(arr))
    return answer

