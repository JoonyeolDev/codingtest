# https://school.programmers.co.kr/learn/courses/30/lessons/154538
# 숫자 변환하기

# 문제 설명
# 자연수 x를 y로 변환하려고 합니다. 사용할 수 있는 연산은 다음과 같습니다.

# x에 n을 더합니다
# x에 2를 곱합니다.
# x에 3을 곱합니다.
# 자연수 x, y, n이 매개변수로 주어질 때, x를 y로 변환하기 위해 필요한 최소 연산 횟수를 return하도록 solution 함수를 완성해주세요. 이때 x를 y로 만들 수 없다면 -1을 return 해주세요.

# 제한사항
# 1 ≤ x ≤ y ≤ 1,000,000
# 1 ≤ n < y

x, y, n = 10, 40, 5
x, y, n = 5, 21, 2
# result = 2


# 초기 코드
from collections import deque
def solution(x, y, n):
    visited = [0] * (y + 1)
    queue = deque([x])
    while queue:
        num = queue.popleft()
        next_numbers = [num + n, num * 2, num * 3]
        if num == y:
            return visited[y]
        for next_num in next_numbers:
            if next_num <= y and not visited[next_num]:
                visited[next_num] = visited[num] + 1
                queue.append(next_num)
    return -1 
# 294.43ms, 25.8MB


print(solution(x, y, n))
