# https://www.acmicpc.net/problem/23900

# 알고리즘 수업 - 선택 정렬 6

# 문제
# 오늘도 서준이는 선택 정렬 수업 조교를 하고 있다. 아빠가 수업한 내용을 학생들이 잘 이해했는지 문제를 통해서 확인해보자.

# N개의 서로 다른 양의 정수가 저장된 배열 A가 있다. 선택 정렬로 배열 A를 오름차순 정렬할 경우 정렬 과정에서 배열 A가 배열 B와 같은 경우가 발생하는지 확인해 보자. 초기 상태 배열 A도 정렬 과정에서 발생 가능한 경우로 생각하자.

# N이 매우 커서 시간 초과를 고민하고 있는 우리 서준이를 도와주자.

# 크기가 N인 배열에 대한 선택 정렬 의사 코드는 다음과 같다.

# 입력
# 첫째 줄에 배열 A, B의 크기 N(5 ≤ N ≤ 500,000)이 주어진다.

# 다음 줄에 서로 다른 배열 A의 원소 A1, A2, ..., AN이 주어진다. (1 ≤ Ai ≤ 109)

# 다음 줄에 서로 다른 배열 B의 원소 B1, B2, ..., BN이 주어진다. (1 ≤ Bi ≤ 109)

# 출력
# 선택 정렬로 배열 A를 오름차순 정렬하는 과정에서 배열 A가 배열 B와 같은 경우가 발생하면 1, 아니면 0을 출력한다.

# arr = [3,1,2,5,4]
# check_arr = [2, 1, 3, 4, 5]

from sys import stdin, exit
input = stdin.readline


n = 5
arr = [3,1,2,5,4]
# arr = [3,1,2,5,4,6]
# check_arr = [1,3,2,4,5]
check_arr = [2,1,3,4,5]
# check_arr = [4,1,2,3,5,6]
# check_arr = [1,2,3,4,5]

n = int(input())
arr = list(map(int,input().split()))
check_arr = list(map(int,input().split()))


# 압축
def solution(n,arr,check_arr):
    if arr == check_arr: 
        return 1
    sorted_arr = sorted(arr)
    sorted_check_arr = sorted(check_arr)
    if sorted_arr != sorted_check_arr:
        return 0
    rank = {value: idx for idx, value in enumerate(sorted_arr)}
    comp_arr = [rank[value] for value in arr]
    comp_check_arr = [rank[value] for value in check_arr]
    for idx in range(n-1,1,-1):
        max_idx = idx
        for i in range(0,idx):
            if comp_arr[i] > comp_arr[max_idx]:
                max_idx = i
        if max_idx != idx:
            comp_arr[idx], comp_arr[max_idx] = comp_arr[max_idx], comp_arr[idx]
        if comp_arr[idx] != comp_check_arr[idx]:
            break
    if comp_arr == comp_check_arr:
        return 1
    return 0



if arr == check_arr: 
    print(1)
    exit()
sorted_arr = sorted(arr)
rank = {value: idx for idx, value in enumerate(sorted_arr)}
comp_arr = [rank[value] for value in arr]
comp_check_arr = [rank[value] for value in check_arr]
for idx in range(n-1,1,-1):
    max_idx = idx
    for i in range(0,idx):
        if comp_arr[i] > comp_arr[max_idx]:
            max_idx = i
    if max_idx != idx:
        comp_arr[idx], comp_arr[max_idx] = comp_arr[max_idx], comp_arr[idx]
    if comp_arr[idx] != comp_check_arr[idx]:
        break
print(1 if comp_arr == comp_check_arr else 0)






# print(solution(n,arr,check_arr))


# print(solution(n,arr,check_arr))

# def solution(n,arr,check_arr):
#     if arr == check_arr: 
#         return 1
#     for idx in range(n-1,0,-1):
        # max_idx = idx
        # for i in range(0,idx):
        #     if arr[i] > arr[max_idx]:
        #         max_idx = i
#         if max_idx != idx:
#             arr[idx], arr[max_idx] = arr[max_idx], arr[idx]
#             if arr == check_arr:
#                 return 1
#     return 0

# def solution(n,arr,check_arr):
#     if arr==check_arr:
#         return 1
#     sorted_arr = sorted(arr)
#     for idx in range(n-1,0,-1):
#         if sorted_arr[idx] != check_arr[idx]:
#             last_idx = idx
#             break
#     else: return 1
#     for idx in range(n-1,last_idx,-1):
#         max_idx = idx
#         for i in range(0,idx):
#             if arr[i] > arr[max_idx]:
#                 max_idx = i
#         if arr[idx] < arr[max_idx]:
#             arr[idx], arr[max_idx] = arr[max_idx], arr[idx]
            
#     return 1 if arr == check_arr else 0
#     # return arr



# def solution(n, arr, check_arr):
#     if arr == check_arr:
#         return 1
#     for idx in range(n-1, 0, -1):
#         max_idx = idx
#         for i in range(idx):
#             if arr[i] > arr[max_idx]:
#                 max_idx = i
#         if arr[max_idx] != check_arr[idx]: break
#         arr[idx], arr[max_idx] = arr[max_idx], arr[idx]
#     return 1 if arr == check_arr else 0
    # return arr

# print(solution(n,arr,check_arr))

# def solution(n, arr, check_arr):
#     if arr == check_arr:
#         return 1
#     sorted_arr = sorted(arr)
#     for idx in range(n-1, -1, -1):
#         if sorted_arr[idx] != check_arr[idx]:
#             last_idx = idx
#             break
#     else:
#         return 1
#     for idx in range(n-1, last_idx, -1):
#         max_idx = idx
#         for i in range(idx):
#             if arr[i] > arr[max_idx]:
#                 max_idx = i
#         if arr[max_idx] != check_arr[idx]: 
#             break
#         arr[idx], arr[max_idx] = arr[max_idx], arr[idx]
#     return 1 if arr == check_arr else 0
    # return arr


# if arr == check_arr:
#     print(1)
#     exit()
# sorted_arr = sorted(arr)
# for idx in range(n-1, -1, -1):
#     if sorted_arr[idx] != check_arr[idx]:
#         last_idx = idx
#         break
# else:
#     print(1)
#     exit()
# for idx in range(n-1, last_idx, -1):
#     max_idx = idx
#     for i in range(idx):
#         if arr[i] > arr[max_idx]:
#             max_idx = i
#     if arr[max_idx] != check_arr[idx]: 
#         break
#     arr[idx], arr[max_idx] = arr[max_idx], arr[idx]

# print(1 if arr == check_arr else 0)


# print(solution(n,arr,check_arr))
