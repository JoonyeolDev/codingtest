# https://school.programmers.co.kr/learn/courses/30/lessons/132265
# 롤케이크 자르기

# 문제 설명
# 철수는 롤케이크를 두 조각으로 잘라서 동생과 한 조각씩 나눠 먹으려고 합니다. 이 롤케이크에는 여러가지 토핑들이 일렬로 올려져 있습니다. 철수와 동생은 롤케이크를 공평하게 나눠먹으려 하는데, 그들은 롤케이크의 크기보다 롤케이크 위에 올려진 토핑들의 종류에 더 관심이 많습니다. 그래서 잘린 조각들의 크기와 올려진 토핑의 개수에 상관없이 각 조각에 동일한 가짓수의 토핑이 올라가면 공평하게 롤케이크가 나누어진 것으로 생각합니다.
# 롤케이크에 올려진 토핑들의 번호를 저장한 정수 배열 topping이 매개변수로 주어질 때, 롤케이크를 공평하게 자르는 방법의 수를 return 하도록 solution 함수를 완성해주세요.

# 제한사항
# 1 ≤ topping의 길이 ≤ 1,000,000
# 1 ≤ topping의 원소 ≤ 10,000

topping = [4, 3, 2, 3, 4, 1, 2]
# result = 2


# 1차 수정 : 자료구조 변경
def solution(arr):
    cnt = 0
    forward_count = 0
    reverse_count = 0
    len_arr = len(arr)
    forward_list = [0] * len_arr
    reverse_list = [0] * len_arr
    forward_seen = set()
    reverse_seen = set()
    
    for i in range(len_arr - 1):
        if arr[i] not in forward_seen:
            forward_count += 1
            forward_seen.add(arr[i])
        forward_list[i] = forward_count

        if arr[len_arr - 1 - i] not in reverse_seen:
            reverse_count += 1
            reverse_seen.add(arr[len_arr - 1 - i])
        reverse_list[len_arr - 1 - i] = reverse_count
    
    for i in range(1, len_arr - 1):
        if forward_list[i] == reverse_list[i + 1]:
            cnt += 1

    return cnt
# 560.25ms, 64.9MB


# 초기 코드
def solution(arr):
    forward_set = set()
    reverse_set = set()
    forward_dict = {}
    reverse_dict = {}
    cnt = 0
    len_arr = len(arr)
    for i in range(len_arr-1):
        forward_set.add(arr[i])
        reverse_set.add(arr[len_arr-1-i])
        forward_dict[i] = len(forward_set)
        reverse_dict[len_arr-1-i] = len(reverse_set)
    for i in range(1, len_arr-1):
        if forward_dict[i] == reverse_dict[i+1]:
            cnt += 1
    return cnt
# 1034.62ms, 262MB
print(solution(topping))