# https://school.programmers.co.kr/learn/courses/30/lessons/86052
# 빛의 경로 사이클

# 문제 설명
# 빛이 "S"가 써진 칸에 도달한 경우, 직진합니다.
# 빛이 "L"이 써진 칸에 도달한 경우, 좌회전을 합니다.
# 빛이 "R"이 써진 칸에 도달한 경우, 우회전을 합니다.
# 빛이 격자의 끝을 넘어갈 경우, 반대쪽 끝으로 다시 돌아옵니다. 
# 예를 들어, 빛이 1행에서 행이 줄어드는 방향으로 이동할 경우, 같은 열의 반대쪽 끝 행으로 다시 돌아옵니다.
# 당신은 이 격자 내에서 빛이 이동할 수 있는 경로 사이클이 몇 개 있고, 
# 각 사이클의 길이가 얼마인지 알고 싶습니다. 
# 경로 사이클이란, 빛이 이동하는 순환 경로를 의미합니다.

# 격자의 정보를 나타내는 1차원 문자열 배열 grid가 매개변수로 주어집니다. 
# 주어진 격자를 통해 만들어지는 빛의 경로 사이클의 모든 길이들을 배열에 담아 
# 오름차순으로 정렬하여 return 하도록 solution 함수를 완성해주세요.

# 제한사항
# 1 ≤ grid의 길이 ≤ 500
# 1 ≤ grid의 각 문자열의 길이 ≤ 500
# grid의 모든 문자열의 길이는 서로 같습니다.
# grid의 모든 문자열은 'L', 'R', 'S'로 이루어져 있습니다.

grid = ["S", "S"]


answer = []
vector = [[1,0],[0,1],[-1,0],[0,-1]]
box = [len(grid),len(grid[0])]

def logic(point, vec):
    # point 이동
    point = [point[0]+vec[0], point[1]+vec[1]]
    if point[0] == box[0]:
        point[0] = 0
    elif point[0] == -1:
        point[0] = box[0]-1
    if point[1] == box[1]:
        point[1] = 0
    elif point[1] == -1:
        point[1] = box[1]-1
    # 방향 지정
    vec = vector.index(vec)
    s = {"S": vec,"R": vec-1,"L": vec+1}
    idx = s[grid[point[0]][point[1]]]
    if idx == 4: idx=0
    vec = vector[idx]
    return point, vec

arr = set()
for i in range(box[0]):
    for j in range(box[1]):
        start = [i,j]
        for vec in vector:
            point = start
            v = vec
            count = 0
            while tuple(point+v) not in arr:
                arr.add(tuple(point+v))
                point,v = logic(point,v)
                count+=1
                if point==start and v==vec:
                    break
            if count != 0: answer.append(count)
answer.sort()
print(answer)

def solution(grid):
    answer = []
    vector = [[1,0],[0,1],[-1,0],[0,-1]]
    box = [len(grid),len(grid[0])]

    def logic(point, vec):
        point = [point[0]+vec[0], point[1]+vec[1]]
        if point[0] == box[0]:
            point[0] = 0
        elif point[0] == -1:
            point[0] = box[0]-1
        if point[1] == box[1]:
            point[1] = 0
        elif point[1] == -1:
            point[1] = box[1]-1
        vec = vector.index(vec)
        s = {"S": vec,"R": vec-1,"L": vec+1}
        idx = s[grid[point[0]][point[1]]]
        if idx == 4: idx=0
        vec = vector[idx]
        return point, vec

    arr = set()
    for i in range(box[0]):
        for j in range(box[1]):
            start = [i,j]
            for vec in vector:
                point = start
                v = vec
                count = 0
                while tuple(point+v) not in arr:
                    arr.add(tuple(point+v))
                    point,v = logic(point,v)
                    count+=1
                    if point==start and v==vec:
                        break
                if count != 0: answer.append(count)
    answer.sort()
    return answer