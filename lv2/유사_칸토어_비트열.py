# https://school.programmers.co.kr/learn/courses/30/lessons/148652
# 유사 칸토어 비트열

# 문제 설명
# 수학에서 칸토어 집합은 0과 1 사이의 실수로 이루어진 집합으로, [0, 1]부터 시작하여 각 구간을 3등분하여 가운데 구간을 반복적으로 제외하는 방식으로 만들어집니다.

# 남아는 칸토어 집합을 조금 변형하여 유사 칸토어 비트열을 만들었습니다. 유사 칸토어 비트열은 다음과 같이 정의됩니다.

# 0 번째 유사 칸토어 비트열은 "1" 입니다.
# n(1 ≤ n) 번째 유사 칸토어 비트열은 n - 1 번째 유사 칸토어 비트열에서의 1을 11011로 치환하고 0을 00000로 치환하여 만듭니다.
# 남아는 n 번째 유사 칸토어 비트열에서 특정 구간 내의 1의 개수가 몇 개인지 궁금해졌습니다.
# n과 1의 개수가 몇 개인지 알고 싶은 구간을 나타내는 l, r이 주어졌을 때 그 구간 내의 1의 개수를 return 하도록 solution 함수를 완성해주세요.

# 제한사항
# 1 ≤ n ≤ 20
# 1 ≤ l, r ≤ 5n
# l ≤ r < l + 10,000,000
# l과 r은 비트열에서의 인덱스(1-base)이며 폐구간 [l, r]을 나타냅니다.

n,l,r = 2,5,17 
# result = 8

def cantor(n):
    s = '1'
    count = 0
    while count<n:
        answer = ''
        for i in s:
            if i=='1':
                answer+='11011'
            else:
                answer+='00000'
        s = answer
        count+=1
    return s
answer = []
for i in range(4):
    arr=[]
    cantor_list = [j for j in cantor(i)]
    for idx,v in enumerate(cantor_list):
        if v=='0': arr.append(idx)
    answer.append(arr)
print(answer)

def sol(i):
    if i%5==2:
        return 0
    if i<=4:
        return 1
    return sol(i//5)

def solution(n, l, r):
    answer=0
    for i in range(l-1,r):
        answer+= sol(i)
    return answer

0,l-1,r,5**n
a,b,c = l-2, r-l, 5**n-l

# def cantor_arr(n,l,r,s="1",counter=0):
#     if counter==n: return s[l-1:r].count("1")
#     s=s.replace("1","a").replace("0","b")
#     s=s.replace("a","11011").replace("b","00000")
#     return cantor_arr(n,l,r,s,counter+1)

# def solution(n,l,r,s=[1],counter=0):
#     if counter==n: return s[l-1:r].count(1)
#     arr = []
#     for i in s:
#         if i==1: arr+=[1,1,0,1,1]
#         else: arr+=[0,0,0,0,0]
#     s = arr
#     return solution(n,l,r,s,counter+1)

# answer=0
# def cantor_arr(l):
#     if l < 5**(n-1)*2 : answer = 1 + l - ((l-2)//5+1)
#     elif l>=5**(n-1)*2 and l< 5**(n-1)*3-1 : answer=4**(n-1)*2
#     else : answer = 4**(n-1)*2 + (l-5**(n-1)*3) - (((l-5**(n-1)*3)-2)//5)
#     return answer


