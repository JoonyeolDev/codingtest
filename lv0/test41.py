# https://school.programmers.co.kr/learn/courses/30/lessons/120876
# 겹치는 선분의 길이

# 문제 설명
# 선분 3개가 평행하게 놓여 있습니다. 세 선분의 시작과 끝 좌표가 
# [[start, end], [start, end], [start, end]] 형태로 들어있는 
# 2차원 배열 lines가 매개변수로 주어질 때, 두 개 이상의 선분이 겹치는 부분의 길이를 
# return 하도록 solution 함수를 완성해보세요.

# lines가 [[0, 2], [-3, -1], [-2, 1]]일 때 그림으로 나타내면 다음과 같습니다.

# line_2.png

# 선분이 두 개 이상 겹친 곳은 [-2, -1], [0, 1]로 길이 2만큼 겹쳐있습니다.

lines = [[0, 1], [2, 5], [3, 9]]

answer = 0
# 직선의 중심인 x.5를 지나는 선이 여러개면 겹치는 부분임
# 리스트에다가 x.5를 구해서 다 집어넣자
arr = []
for i in lines:
    for j in range(i[0],i[1]):
        arr.append(j+0.5)
print(arr)
# arr의 중복제거를 위해 set으로 만들고
# for문으로 count해서 1이 아니면 answer를 1씩 늘림
for i in set(arr):
    if arr.count(i) != 1 : answer+=1
print(answer)

# 제출용 함수
def solution(lines):
    arr = []
    for i in lines:
        for j in range(i[0],i[1]): 
            arr.append(j+0.5)
    answer = 0
    for i in set(arr):
        if arr.count(i) != 1 : answer+=1
    return answer