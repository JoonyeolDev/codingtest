# https://school.programmers.co.kr/learn/courses/30/lessons/12911
# 다음 큰 숫자

# 문제 설명
# 자연수 n이 주어졌을 때, n의 다음 큰 숫자는 다음과 같이 정의 합니다.

# 조건 1. n의 다음 큰 숫자는 n보다 큰 자연수 입니다.
# 조건 2. n의 다음 큰 숫자와 n은 2진수로 변환했을 때 1의 갯수가 같습니다.
# 조건 3. n의 다음 큰 숫자는 조건 1, 2를 만족하는 수 중 가장 작은 수 입니다.
# 예를 들어서 78(1001110)의 다음 큰 숫자는 83(1010011)입니다.

# 자연수 n이 매개변수로 주어질 때, n의 다음 큰 숫자를 return 하는 solution 함수를 완성해주세요.

# 제한 사항
# n은 1,000,000 이하의 자연수 입니다.

n = 78
# result = 83

def dec_to_bin(s,bin=""):
    if s==0: return bin
    return dec_to_bin(s//2,bin=str(s%2)+bin)

n_bin = dec_to_bin(n)

n_bin = n_bin[::-1]
try:
    idx = n_bin.index("10")
    n_ = n_bin.replace("10","01",1)
    n_ = "".join(sorted(n_bin[:idx],reverse=True))+n_[idx:]
    answer = int(n_[::-1],2)
except:
    n_bin = n_bin[::-1]
    answer = int("10"+ "".join(sorted(n_bin[1:])),2)
    
print(answer)


def solution(n):
    def dec_to_bin(s,bin=""):
        if s==0: return bin
        return dec_to_bin(s//2,bin=str(s%2)+bin)
    n_bin = dec_to_bin(n)
    n_bin = n_bin[::-1]
    try:
        idx = n_bin.index("10")
        n_ = n_bin.replace("10","01",1)
        n_ = "".join(sorted(n_bin[:idx],reverse=True))+n_[idx:]
        answer = int(n_[::-1],2)
    except:
        n_bin = n_bin[::-1]
        answer = int("10"+ "".join(sorted(n_bin[1:])),2)
    return answer






# n_lists = itertools.permutations([i for i in n_bin[1:]],len(n_bin)-1)
# n_set = set()
# for i in n_lists:
#     i= "1"+"".join(i)
#     n_set.add(i)
# answer = 1000000
# for i in n_set:
#     if answer>int(i,2) and int(i,2)>n: answer = int(i,2)
# if answer == 1000000:
#     answer = int("10"+ "".join(sorted(n_bin[1:])),2)
# print(answer)








# i = 0
# if len(n_bin)==n_bin.count("1"):
#     answer = "10"+n_bin[1:]
# for idx,value in enumerate(n_bin):
#     if idx == 0: continue
#     if n_bin[idx-1]=="0" and n_bin[idx]=="1":
#         max_idx = idx
#         answer = n_bin[:idx-1]+"10"
#         answer += ("0"*(len(n_bin)-n_bin.count("1")-answer.count("0")))+("1"*(len(n_bin)-n_bin.count("0")-answer.count("1")))
#         break
# answer = int(answer,2)
# print(answer)



