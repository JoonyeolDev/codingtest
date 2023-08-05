# https://school.programmers.co.kr/learn/courses/30/lessons/87377

# 교점에 별 만들기
# 문제 설명
# Ax + By + C = 0으로 표현할 수 있는 n개의 직선이 주어질 때, 
# 이 직선의 교점 중 정수 좌표에 별을 그리려 합니다.

# 직선 A, B, C에 대한 정보가 담긴 배열 line이 매개변수로 주어집니다. 
# 이때 모든 별을 포함하는 최소 사각형을 return 하도록 
# solution 함수를 완성해주세요.

# 제한사항
# line의 세로(행) 길이는 2 이상 1,000 이하인 자연수입니다.
# line의 가로(열) 길이는 3입니다.
# line의 각 원소는 [A, B, C] 형태입니다.
# A, B, C는 -100,000 이상 100,000 이하인 정수입니다.
# 무수히 많은 교점이 생기는 직선 쌍은 주어지지 않습니다.
# A = 0이면서 B = 0인 경우는 주어지지 않습니다.
# 정답은 1,000 * 1,000 크기 이내에서 표현됩니다.
# 별이 한 개 이상 그려지는 입력만 주어집니다.

line = [[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]
# result = ["....*....", ".........", ".........", "*.......*", ".........", ".........", ".........", ".........", "*.......*"]

import itertools
arr=[]
for i in itertools.combinations(line,2):
    try:
        x = (i[0][1]*i[1][2]-i[0][2]*i[1][1])/(i[0][0]*i[1][1]-i[0][1]*i[1][0])
        y = (i[0][2]*i[1][0]-i[0][0]*i[1][2])/(i[0][0]*i[1][1]-i[0][1]*i[1][0])
        if x==int(x) and y==int(y):
            arr.append([int(x),int(y)])
    except: pass
width = [sorted(arr,key=lambda x:x[0])[0][0],sorted(arr,key=lambda x:x[0])[-1][0]]
hight = [sorted(arr,key=lambda x:x[1])[0][1],sorted(arr,key=lambda x:x[1])[-1][1]]
width_ = width[1]-width[0]+1
hight_ = hight[1]-hight[0]+1

answer =[['.' for i in range(width_)] for j in range(hight_)]
for i in arr:
    answer[abs(hight[0]+i[1])][-width[0]+i[0]] = '*'

def solution(line):
    arr=[]
    for i in itertools.combinations(line,2):
        try:
            x = (i[0][1]*i[1][2]-i[0][2]*i[1][1])/(i[0][0]*i[1][1]-i[0][1]*i[1][0])
            y = (i[0][2]*i[1][0]-i[0][0]*i[1][2])/(i[0][0]*i[1][1]-i[0][1]*i[1][0])
            if x==int(x) and y==int(y):
                arr.append([int(x),int(y)])
        except: pass
    width = [sorted(arr,key=lambda x:x[0])[0][0],sorted(arr,key=lambda x:x[0])[-1][0]]
    hight = [sorted(arr,key=lambda x:x[1])[0][1],sorted(arr,key=lambda x:x[1])[-1][1]]
    width_ = width[1]-width[0]+1
    hight_ = hight[1]-hight[0]+1

    answer =[['.' for i in range(width_)] for j in range(hight_)]
    for i in arr:
        answer[-hight[0]+i[1]][-width[0]+i[0]] = '*'
    answer = [''.join(i) for i in answer[::-1]]
    return answer 

print(solution([[0, 1, -1], [1, 0, -1], [1, 0, 1]]))
print(solution(line))



