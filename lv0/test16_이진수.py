# https://school.programmers.co.kr/learn/courses/30/lessons/120885
# 이진수 더하기

# 문제 설명
# 이진수를 의미하는 두 개의 문자열 bin1과 bin2가 매개변수로 주어질 때, 
# 두 이진수의 합을 return하도록 solution 함수를 완성해주세요.

# 제한사항
# return 값은 이진수를 의미하는 문자열입니다.
# 1 ≤ bin1, bin2의 길이 ≤ 10
# bin1과 bin2는 0과 1로만 이루어져 있습니다.
# bin1과 bin2는 "0"을 제외하고 0으로 시작하지 않습니다.

# 이진수를 십진수로 변환
def bin_to_dec(bin):
    sum = 0
    bin = [int(i) for i in bin]
    bin.reverse()
    for i in range(len(bin)):
        if bin[i]==1: sum += 2**(i)
    return sum

# 십진수를 이진수로 변환
def dec_to_bin(dec):
    sum = ""
    if dec == 0: sum = "0"
    while True:
        if dec==0: break
        if dec%2 ==0:
            dec /= 2
            sum = "0" + sum
        else:
            dec = dec//2
            sum = "1" + sum
    return sum

def solution(bin1, bin2):
    answer = dec_to_bin(bin_to_dec(bin1)+bin_to_dec(bin2))
    return answer



def tr_b(arr,x):
    arr.append(x%2)
    if x/2<1: 
        arr.reverse()
        return arr,x
    else : tr_b(arr,int(x/2))

def tr_s(bin):
    arr=[]
    ex=0
    x=0
    for i in bin:
        arr.append(int(i))
    arr.reverse()
    for i in arr:
        if i==1 : x+=2**ex
        ex+=1
    return x

def solution2(bin1, bin2):
    answer = ''
    arr=[]
    a=tr_s(bin1)+tr_s(bin2)
    tr_b(arr,a)
    for i in arr:
        answer+=str(i)
    return answer