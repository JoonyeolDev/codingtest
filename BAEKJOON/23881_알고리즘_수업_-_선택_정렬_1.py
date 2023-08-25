# https://www.acmicpc.net/problem/23881
# 알고리즘 수업 - 선택 정렬 1

# 문제
# 오늘도 서준이는 선택 정렬 수업 조교를 하고 있다. 아빠가 수업한 내용을 학생들이 잘 이해했는지 문제를 통해서 확인해보자.

# N개의 서로 다른 양의 정수가 저장된 배열 A가 있다. 선택 정렬로 배열 A를 오름차순 정렬할 경우 K 번째 교환되는 수를 구해서 우리 서준이를 도와주자.

# 입력
# 첫째 줄에 배열 A의 크기 N(5 ≤ N ≤ 10,000), 교환 횟수 K(1 ≤ K ≤ N)가 주어진다.

# 다음 줄에 서로 다른 배열 A의 원소 A1, A2, ..., AN이 주어진다. (1 ≤ Ai ≤ 109)

# 출력
# K 번째 교환되는 두 개의 수를 작은 수부터 한 줄에 출력한다. 교환 횟수가 K 보다 작으면 -1을 출력한다.

n, k = 5, 2
arr = [3,1,2,5,4]
arr = [1]*5
from sys import stdin, exit
# input = stdin.readline
# n, k = map(int,input().split())
# arr = list(map(int,input().split()))


# for idx in range(n-1,1,-1):
#     max_idx = idx
#     for i in range(0,idx):
#         if arr[i] > arr[max_idx]:
#             max_idx = i
#     if max_idx != idx:
#         arr[idx], arr[max_idx] = arr[max_idx], arr[idx]
#         k -= 1
#         if not k:
#             print(f'{min(arr[max_idx], arr[idx])} {max(arr[max_idx], arr[idx])}')
#             exit()
# print(-1)

def solution(n, k, arr):
    if k > n:
        return -1
    for idx in range(n-1,0,-1):
        max_idx = idx
        for i in range(idx):
            if arr[i] > arr[max_idx]:
                max_idx = i
        if max_idx != idx:
            arr[idx], arr[max_idx] = arr[max_idx], arr[idx]
            k -= 1
            if not k:
                return f'{min(arr[max_idx], arr[idx])} {max(arr[max_idx], arr[idx])}'
    return -1

print(solution(n, k, arr))

# 메모리, 시간, 코드 길이
# 32276KB, 2032ms, 578B, python3
# 115152KB, 200ms, 578B, pypy3