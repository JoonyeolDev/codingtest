# https://school.programmers.co.kr/learn/courses/30/lessons/87390

# n^2 배열 자르기

# 문제 설명
# 정수 n, left, right가 주어집니다. 다음 과정을 거쳐서 1차원 배열을 만들고자 합니다.

# n행 n열 크기의 비어있는 2차원 배열을 만듭니다.
# i = 1, 2, 3, ..., n에 대해서, 다음 과정을 반복합니다.
# 1행 1열부터 i행 i열까지의 영역 내의 모든 빈 칸을 숫자 i로 채웁니다.
# 1행, 2행, ..., n행을 잘라내어 모두 이어붙인 새로운 1차원 배열을 만듭니다.
# 새로운 1차원 배열을 arr이라 할 때, arr[left], arr[left+1], ..., arr[right]만 남기고 나머지는 지웁니다.
# 정수 n, left, right가 매개변수로 주어집니다. 
# 주어진 과정대로 만들어진 1차원 배열을 return 하도록 solution 함수를 완성해주세요.

# 제한사항
# 1 ≤ n ≤ 10**7
# 0 ≤ left ≤ right < n**2
# right - left < 10**5

n, left, right = 3, 2, 5
# result = [3,2,2,3]


# 2차 수정 : 로직 변경
def solution(n, left, right):
    answer = [max(i//n+1, i%n+1) for i in range(left, right+1)]
    return answer


# 2차 수정 : 로직 변경
def solution(n, left, right):
    return [max(i//n+1, i%n+1) for i in range(left, right+1)]
# 45.57ms, 18.1MB


# 1차 수정 : 필요한 부분만 계산
def solution(n, left, right):
    left_div, left_mod = divmod(left, n)
    right_div, _ = divmod(right, n)
    arr = []
    for i in range(left_div+1, right_div+2):
        arr += [i if j <= i else j for j in range(1,n+1)]
    answer = arr[left_mod:left_mod+right-left+1]
    return answer
# 871.15ms, 430MB


# 초기 코드 : 시간 초과
def solution(n, left, right):
    arr = []
    for i in range(1,n+1):
        arr += [i if j <= i else j for j in range(1,n+1)]
    return arr[left:right+1]