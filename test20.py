# https://school.programmers.co.kr/learn/courses/30/lessons/120585
# 머쓱이보다 키 큰 사람

# 문제 설명
# 머쓱이는 학교에서 키 순으로 줄을 설 때 몇 번째로 서야 하는지 궁금해졌습니다. 
# 머쓱이네 반 친구들의 키가 담긴 정수 배열 array와 머쓱이의 키 height가 
# 매개변수로 주어질 때, 머쓱이보다 키 큰 사람 수를 
# return 하도록 solution 함수를 완성해보세요.

# 제한사항
# 1 ≤ array의 길이 ≤ 100
# 1 ≤ height ≤ 200
# 1 ≤ array의 원소 ≤ 200

array = [149, 180, 192, 170]
n = 167

answer = 0
answer = ((1 if n < i else 0) for i in array)
print (answer)

# 제출용 함수
def solution(array,n):
    answer = sum((1 if n < i else 0) for i in array)
    return answer

# for문 이용해서 풀어보기
def solution2(array,n):
    answer=0
    for i in array :
        if n<i : answer=answer+1
    return answer
