# https://school.programmers.co.kr/learn/courses/30/lessons/42577
# 전화번호 목록

# 문제 설명
# 전화번호부에 적힌 전화번호 중, 한 번호가 다른 번호의 접두어인 경우가 있는지 확인하려 합니다.
# 전화번호가 다음과 같을 경우, 구조대 전화번호는 영석이의 전화번호의 접두사입니다.

# 구조대 : 119
# 박준영 : 97 674 223
# 지영석 : 11 9552 4421
# 전화번호부에 적힌 전화번호를 담은 배열 phone_book 이 solution 함수의 매개변수로 주어질 때, 어떤 번호가 다른 번호의 접두어인 경우가 있으면 false를 그렇지 않으면 true를 return 하도록 solution 함수를 작성해주세요.

# 제한 사항
# phone_book의 길이는 1 이상 1,000,000 이하입니다.
# 각 전화번호의 길이는 1 이상 20 이하입니다.
# 같은 전화번호가 중복해서 들어있지 않습니다.

# 각 전화번호의 길이를 확인, 가장 짧은 길이의 값을 기준으로 시작
# 각 전화번호의 순서는 그대로이고 길이만 다른 부분함수들을 key로 가지는 dict 생성
# dict에 key값이 있으면 1 없으면 0 리턴

phone_book = ["119", "97674223", "1195524421"]
# result = False


# 3차 수정 : 로직 변경, 필요한 정보만 저장
def solution(phone_book):
    length = set()
    for number in phone_book:
        length.add(len(number))
    phone_dict = {}
    for number in phone_book:
        for i in length:
            num = number[:i]
            if  num==number:
                phone_dict[num] = phone_dict.get(num,0) + 1 
    for number in phone_book:
        if phone_dict.get(number, 0):
                return False
    return True
# 107.89ms, 48MB


# 2차 수정 : 딕셔너리 
def solution(phone_book):
    min_length = 20
    for number in phone_book:
        min_length = min(min_length, len(number))
    phone_dict = {}
    for number in phone_book:
        for i in range(min_length, len(number)):
            num = number[:i]
            phone_dict[num] = phone_dict.get(num,0) + 1 
    for number in phone_book:
        if phone_dict.get(number, 0):
                return False
    return True
# 155.92ms, 47.9MB


# 1차 수정 : 시간초과
def solution(phone_book):
    for num in phone_book:
        len_num = len(num)
        for check_num in phone_book:
            if num == check_num: continue
            elif num == check_num[:len_num]:
                return False
    return True



# 초기 코드 : 답은 나오지만 시간초과
def solution(phone_book):
    min_length = 20
    for number in phone_book:
        min_length = min(min_length, len(number))

    phone_dict = {}
    for number in phone_book:
        temp_dict = {}
        for i in range(min_length, len(number)):
            temp_dict[number[:i]] = True
        phone_dict[number] = temp_dict

    for number in phone_book:
        for key in phone_dict:
            if number == key: continue
            if phone_dict[key].get(number, 0):
                return False
    return True