# https://school.programmers.co.kr/learn/courses/30/lessons/12953

# 문제 설명
# 두 수의 최소공배수(Least Common Multiple)란 
# 입력된 두 수의 배수 중 공통이 되는 가장 작은 숫자를 의미합니다. 
# 예를 들어 2와 7의 최소공배수는 14가 됩니다. 
# 정의를 확장해서, n개의 수의 최소공배수는 n 개의 수들의 배수 중 공통이 되는 가장 작은 숫자가 됩니다. 
# n개의 숫자를 담은 배열 arr이 입력되었을 때 이 수들의 최소공배수를 반환하는 함수, solution을 완성해 주세요.

# 제한 사항
# arr은 길이 1이상, 15이하인 배열입니다.
# arr의 원소는 100 이하인 자연수입니다.

# 1~100까지 소수를 먼저 찾고
# 주어진 arr에서 각 수를 인수분해하고 각 인수가 높은것만 모아서 
# N개의 수의 최대공약수를 구하고 arr안의 모든 요소를 곱한 뒤 최대공약수**(n-1)로 나눠주면 될 듯
# 제한 조건에서 100이하인 자연수니깐 다 나눌 필요없이 100 이하 소수로만 나눠서 최대 공약수 판단하면 될 듯

arr = [2,6,8,14]
# result = 168


# 2차 수정 : gcd, reduce 사용해 풀기
import math
from functools import reduce
def lcm(x, y):
    return (x * y) // math.gcd(x, y)
def solution(numbers):
    return reduce(lcm, numbers)
# 0.01ms 


# 1차 수정 : 가독성 및 로직 개선
def is_prime(num):
    for i in range(2, int(num**(0.5))+1):
        if not num % i: return False
    return True

def solution(arr):
    answer = 1
    primes = [i for i in range(2, 101) if is_prime(i)]
    prime_counts = {prime: 0 for prime in primes}
    for num in arr:
        if num == 1: continue
        for prime in prime_counts.keys():
            if num < prime: break
            count = 0
            while num % prime == 0:
                count += 1
                num = num // prime
            prime_counts[prime] = max(prime_counts[prime], count)
    for key, value in prime_counts.items():
        answer *= key**value
    return answer
# 0.10ms


# 초기 코드
def is_prime(num):
    for i in range(2, int(num**(0.5))+1):
        if not num % i: return False
    return True
def solution(arr):
    prime_counts = {}
    for i in range(2,101):
        if is_prime(i): prime_counts[i]=0
    divisor = []
    for num in arr:
        if num == 1: continue
        num_dict = {}
        for prime in prime_counts.keys():
            prime = int(prime)
            while num % prime == 0:
                num_dict[prime] = num_dict.get(prime,0) + 1
                num = num // prime
        divisor.append(num_dict)
    for divisor_dict in divisor:
        for key,value in divisor_dict.items():
            prime_counts[key] = max(prime_counts[key], value)
    answer = 1
    for key, value in prime_counts.items():
        answer *= key**value
    return answer
# 0.18ms

