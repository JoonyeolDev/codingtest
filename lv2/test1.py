# https://school.programmers.co.kr/learn/courses/30/lessons/42839
# 소수 찾기

# 문제 설명
# 한자리 숫자가 적힌 종이 조각이 흩어져있습니다. 
# 흩어진 종이 조각을 붙여 소수를 몇 개 만들 수 있는지 알아내려 합니다.
# 각 종이 조각에 적힌 숫자가 적힌 문자열 numbers가 주어졌을 때,
# 종이 조각으로 만들 수 있는 소수가 몇 개인지 return 하도록 
# solution 함수를 완성해주세요.

# 제한사항
# numbers는 길이 1 이상 7 이하인 문자열입니다.
# numbers는 0~9까지 숫자만으로 이루어져 있습니다.
# "013"은 0, 1, 3 숫자가 적힌 종이 조각이 흩어져있다는 의미입니다.

numbers = "17"
num_list = []
arr = []
# 먼저 숫자조합을 찾아야함
# 제한사항에 길이 1이상 7이하임
# 일단 하드코딩하면서 생각

# numbers를 리스트로
for i in numbers:
    num_list.append(i)

# combinations 를 이용해서 중복되지 않는 조합 구하기
from itertools import permutations

# for문으로 permutations 자리수 조합 바로 찾기 
for i in range(1,len(num_list)+1):
    a = list(permutations(num_list,i))

    # for문으로 찾은 조합들 문자열로 만들기
    for j in a:
        # 문자열 초기화
        number=""
        for k in j:
            number += k

        # 문자열 arr에 숫자로 넣기 및 0,1 거르기
        if int(number)!=0 and int(number)!=1 :
            arr.append(int(number))

# set으로 중복 제거
arr = set(arr)

answer=0
# 소수찾기
for i in arr:
    arr2 = []
    for j in range(2,int(i**(1/2)+1)):
        if i%j==0: arr2.append(j)
    if len(arr2)==0: answer+=1
print(answer)

# 제출용 함수로 만들기
def solution(numbers):
    answer = 0
    num_list = []
    arr = []
    for i in numbers:
        num_list.append(i)
    from itertools import permutations
    for i in range(1,len(num_list)+1):
        a = list(permutations(num_list,i))
        for j in a:
            number=""
            for k in j:
                number += k
            if int(number)!=0 and int(number)!=1 :
                arr.append(int(number))
    arr = set(arr)
    print(arr)
    answer=0
    for i in arr:
        arr2 = []
        for j in range(2,int(i**(1/2)+1)):
            if i%j==0: arr2.append(j)
            else: pass
        if len(arr2)==0: answer+=1
    return answer