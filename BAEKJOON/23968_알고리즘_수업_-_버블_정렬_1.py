# https://www.acmicpc.net/problem/23968
# 알고리즘 수업 - 버블 정렬 1

# 문제
# 오늘도 서준이는 버블 정렬 수업 조교를 하고 있다. 아빠가 수업한 내용을 학생들이 잘 이해했는지 문제를 통해서 확인해보자.

# N개의 서로 다른 양의 정수가 저장된 배열 A가 있다. 버블 정렬로 배열 A를 오름차순 정렬할 경우 K 번째 교환되는 수를 구해서 우리 서준이를 도와주자.

# 입력
# 첫째 줄에 배열 A의 크기 N(5 ≤ N ≤ 10,000), 교환 횟수 K(1 ≤ K ≤ N2)가 주어진다.

# 다음 줄에 서로 다른 배열 A의 원소 A1, A2, ..., AN이 주어진다. (1 ≤ Ai ≤ 109)

# 출력
# K 번째 교환되는 두 개의 수를 작은 수부터 한 줄에 출력한다. 교환 횟수가 K 보다 작으면 -1을 출력한다.

n, k = 6, 10
arr = [4,6,5,1,3,2]

# from sys import stdin
# input = stdin.readline
# n, k = map(int,input().split())
# arr = list(map(int,input().split()))

def solution(n, k, arr):
    if k > n*(n+1)//2: 
        return -1
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                k -= 1
                if not k:
                    return f'{arr[j]} {arr[j+1]}'
    return -1

print(solution(n, k, arr))

# 메모리, 시간, 코드 길이
# 114976KB, 372ms, 464B, pypy3