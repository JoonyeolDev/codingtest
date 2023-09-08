# https://www.acmicpc.net/problem/24061

# 문제
# 오늘도 서준이는 병합 정렬 수업 조교를 하고 있다. 아빠가 수업한 내용을 학생들이 잘 이해했는지 문제를 통해서 확인해보자.

# N개의 서로 다른 양의 정수가 저장된 배열 A가 있다. 병합 정렬로 배열 A를 오름차순 정렬할 경우 배열 A의 원소가 K 번 변경된 직후의 배열 A를 출력해 보자.

# 입력
# 첫째 줄에 배열 A의 크기 N(5 ≤ N ≤ 500,000), 변경 횟수 K(1 ≤ K ≤ 108)가 주어진다.

# 다음 줄에 서로 다른 배열 A의 원소 A1, A2, ..., AN이 주어진다. (1 ≤ Ai ≤ 109)

# 출력
# 배열 A에 K 번 변경이 발생한 직후의 배열 A를 한 줄에 출력한다. 변경 횟수가 K 보다 작으면 -1을 출력한다.



def merge(A, k, p, q, r, count):
    if count[0] == k:
        return A.copy()
    i = j = 0
    t = p
    L = A[p:q+1]
    R = A[q+1:r+1]
    result = None
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            A[t] = L[i]
            i += 1
        else:
            A[t] = R[j]
            j += 1
        t += 1
        count += 1
        if count == k:
            return A.copy()
    while i < len(L) and result is None:
        A[t] = L[i]
        i += 1
        t += 1
        count += 1
        if count == k:
            return A.copy()
    while j < len(R) and result is None:
        A[t] = R[j]
        j += 1
        t += 1
        count += 1
        if count == k:
            return A.copy()
    return result

def merge_sort(A, k, p=0, r=None, count=0):
    if r is None:
        r = len(A) - 1
    result = None
    if p < r and count[0] < k:
        q = (p + r) // 2
        result = merge_sort(A, k, p, q, count)
        if result is None:
            result = merge_sort(A, k, q+1, r, count)
        if result is None:
            result = merge(A, k, p, q, r, count)
    return result


# n, k = map(int,input().split())
# arr = list(map(int,input().split()))
n, k = 5, 7
arr = [4,5,1,3,2]
result = merge_sort(arr, k)
result = result if result is not None else -1
print(result)