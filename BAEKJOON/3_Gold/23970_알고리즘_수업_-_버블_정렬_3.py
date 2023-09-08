# https://www.acmicpc.net/problem/23970

# 문제
# 오늘도 서준이는 버블 정렬 수업 조교를 하고 있다. 아빠가 수업한 내용을 학생들이 잘 이해했는지 문제를 통해서 확인해보자.

# N개의 서로 다른 양의 정수가 저장된 배열 A가 있다. 버블 정렬로 배열 A를 오름차순 정렬할 경우 정렬 과정에서 배열 A가 배열 B와 같은 경우가 발생하는지 확인해 보자. 초기 상태 배열 A도 정렬 과정에서 발생 가능한 경우로 생각하자.

# 크기가 N인 배열에 대한 버블 정렬 의사 코드는 다음과 같다.

# 입력
# 첫째 줄에 배열 A, B의 크기 N(5 ≤ N ≤ 10,000)이 주어진다.

# 다음 줄에 서로 다른 배열 A의 원소 A1, A2, ..., AN이 주어진다. (1 ≤ Ai ≤ 109)

# 다음 줄에 서로 다른 배열 B의 원소 B1, B2, ..., BN이 주어진다. (1 ≤ Bi ≤ 109)

# 출력
# 버블 정렬로 배열 A를 오름차순 정렬하는 과정에서 배열 A가 배열 B와 같은 경우가 발생하면 1, 아니면 0을 출력한다.

n = 6
arr = [4,6,5,1,3,2]
check_arr = [4,1,3,2,5,6]
from sys import stdin,exit
input = stdin.readline
n = int(input())
arr = list(map(int,input().split()))
check_arr = list(map(int,input().split()))


def solution(n,arr,check_arr):
    if arr==check_arr: return 1
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                if arr[j+1] == check_arr[j+1]:
                    print(arr)
                    if arr == check_arr:
                        return 1
    return 0
# 메모리, 시간, 길이
# 115380KB, 740ms, 513B, PyPy3

print(solution(n,arr,check_arr))

if arr==check_arr: 
    print(1)
    exit()
for i in range(n-1):
    for j in range(n-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            if arr[j+1] == check_arr[j+1]:
                if arr == check_arr:
                    print(1)
                    exit()
print(0)

# 초기 코드 : 답은 나오나 실패
def solution(n,arr,check_arr):
    if arr==check_arr: return 1
    sorted_arr = sorted(arr)
    for i in range(n-1,0,-1):
        if sorted_arr[i] != check_arr[i]:
            idx = i+1
            break
    else: return 1
    for i in range(idx-1):
        for j in range(n-i-1):
            if n-idx>=i>=n-idx-1:
                if arr == check_arr:
                    return 1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


