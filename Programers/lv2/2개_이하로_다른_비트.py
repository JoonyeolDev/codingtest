# https://school.programmers.co.kr/learn/courses/30/lessons/77885
# 2개 이하로 다른 비트

# 문제 설명
# 양의 정수 x에 대한 함수 f(x)를 다음과 같이 정의합니다.

# x보다 크고 x와 비트가 1~2개 다른 수들 중에서 제일 작은 수
# 예를 들어,

# f(2) = 3 입니다. 다음 표와 같이 2보다 큰 수들 중에서 비트가 다른 지점이 2개 이하이면서 제일 작은 수가 3이기 때문입니다.
# 수	비트	다른 비트의 개수
# 2	000...0010	
# 3	000...0011	1
# f(7) = 11 입니다. 다음 표와 같이 7보다 큰 수들 중에서 비트가 다른 지점이 2개 이하이면서 제일 작은 수가 11이기 때문입니다.
# 수	비트	다른 비트의 개수
# 7	000...0111	
# 8	000...1000	4
# 9	000...1001	3
# 10	000...1010	3
# 11	000...1011	2
# 정수들이 담긴 배열 numbers가 매개변수로 주어집니다. numbers의 모든 수들에 대하여 각 수의 f 값을 배열에 차례대로 담아 return 하도록 solution 함수를 완성해주세요.

# 제한사항
# 1 ≤ numbers의 길이 ≤ 100,000
# 0 ≤ numbers의 모든 수 ≤ 10**15

numbers = [2, 7]
# result = [3, 11]

# 인상깊은 풀이 수정 : 더 빠르게
def solution(numbers):
    return [num + ((num ^ (num+1)) >> 2) + 1 for num in numbers]
# 29.95ms, 25.3MB
numbers = [i for i in range(1,16)]
for i, j in zip(numbers, solution(numbers)):
    print(f'{i}: {bin(i).lstrip("0b")} > {bin(j).lstrip("0b")}')

# 인상깊은 풀이 : 원리 파악
def solution(numbers):
    answer = []
    for i in numbers:
        num = i
        cnt = 0
        while i % 2 == 1:
            cnt += 1
            i //= 2
        answer.append(num + 2**(cnt - 1) if cnt != 0 else num + 1)
    return answer
# 440.17ms, 25.3MB


# 1차 수정 : 로직 변경
def solution(numbers):
    answer = []
    num_dict = {0: 2, 1: 4, 2: 2}
    for number in numbers:
        if (number+1) % 4:
            answer.append(number + 1)
        else:
            key = (number % 16) // 4
            if key == 3:
                bin_number = bin(number).lstrip('0b')
                
                n = 2
                while True:
                    n += 1
                    temp_num =number + 2**n
                    bin_temp_num = bin(temp_num).lstrip('0b')
                    len_temp_num = len(bin_temp_num)
                    temp = bin_number.rjust(len_temp_num, '0')
                    different = 0
                    for i in range(len_temp_num):
                        if temp[i] != bin_temp_num[i]:
                            different += 1
                            if different > 2:
                                break
                    else:
                        answer.append(temp_num)
                        break
            else:
                answer.append(number + num_dict[key])
    return answer
# 5448.05ms, 25.3MB


# 초기 코드 : 시간 초과
def solution(numbers):
    answer = []
    for number in numbers:
        bin_number = bin(number).lstrip('0b')
        len_number = len(bin_number)
        
        temp_num = number
        while True:
            temp_num += 1
            bin_temp_num = bin(temp_num).lstrip('0b')
            len_temp_num = len(bin_temp_num)
            temp = '0'*(len_temp_num-len_number) + bin_number
            different = 0
            for i in range(len_temp_num):
                if temp[i] != bin_temp_num[i]:
                    different += 1
                    if different > 2:
                        break
            else:
                answer.append(temp_num)
                break
    return answer
