# https://school.programmers.co.kr/learn/courses/30/lessons/17681
# [1차] 비밀지도

# 네오는 평소 프로도가 비상금을 숨겨놓는 장소를 알려줄 비밀지도를 손에 넣었다. 
# 그런데 이 비밀지도는 숫자로 암호화되어 있어 위치를 확인하기 위해서는 암호를 해독해야 한다. 
# 다행히 지도 암호를 해독할 방법을 적어놓은 메모도 함께 발견했다.

# 지도는 한 변의 길이가 n인 정사각형 배열 형태로, 
# 각 칸은 "공백"(" ") 또는 "벽"("#") 두 종류로 이루어져 있다.
# 전체 지도는 두 장의 지도를 겹쳐서 얻을 수 있다. 
# 각각 "지도 1"과 "지도 2"라고 하자. 
# 지도 1 또는 지도 2 중 어느 하나라도 벽인 부분은 전체 지도에서도 벽이다. 
# 지도 1과 지도 2에서 모두 공백인 부분은 전체 지도에서도 공백이다.
# "지도 1"과 "지도 2"는 각각 정수 배열로 암호화되어 있다.
# 암호화된 배열은 지도의 각 가로줄에서 벽 부분을 1, 
# 공백 부분을 0으로 부호화했을 때 얻어지는 이진수에 해당하는 값의 배열이다.

# 입력 형식
# 입력으로 지도의 한 변 크기 n 과 2개의 정수 배열 arr1, arr2가 들어온다.

# 1 ≦ n ≦ 16
# arr1, arr2는 길이 n인 정수 배열로 주어진다.
# 정수 배열의 각 원소 x를 이진수로 변환했을 때의 길이는 n 이하이다. 
# 즉, 0 ≦ x ≦ 2n - 1을 만족한다.

# 출력 형식
# 원래의 비밀지도를 해독하여 '#', 공백으로 구성된 문자열 배열로 출력하라.

n = 5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]
# result = ["#####","# # #", "### #", "#  ##", "#####"]

answer = []

# 이진법으로 먼저 만들자
def dec_to_bin(number, n, sum=''):
    if number==0:
        # 근데 무조건 n자리는 만들어야함
        if len(sum) < n:
            sum += '0'*(n-len(sum))
        return sum[::-1]
    return dec_to_bin(number//2, n, sum+str(number%2))

# map_list만들기
map_list1 = [ dec_to_bin(i, n) for i in arr1]
map_list2 = [ dec_to_bin(i, n) for i in arr2]

for i in range(n):
    s = ''
    for j in range(n):
        wall = int(map_list1[i][j])+int(map_list2[i][j])
        if wall == 0: s += ' '
        else: s += '#'
    answer.append(s)

print(answer)

# 제출용 함수
def dec_to_bin(number, n, sum=''):
    if number==0:
        if len(sum) < n:
            sum += '0'*(n-len(sum))
        return sum[::-1]
    return dec_to_bin(number//2, n, sum+str(number%2))

def solution(n, arr1, arr2):
    answer = []
    map_list1 = [ dec_to_bin(i, n) for i in arr1]
    map_list2 = [ dec_to_bin(i, n) for i in arr2]

    for i in range(n):
        s = ''
        for j in range(n):
            wall = int(map_list1[i][j])+int(map_list2[i][j])
            if wall == 0: s += ' '
            else: s += '#'
        answer.append(s)
    return answer