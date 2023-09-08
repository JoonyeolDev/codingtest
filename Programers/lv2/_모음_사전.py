# https://school.programmers.co.kr/learn/courses/30/lessons/84512
# 모음 사전

# 문제 설명
# 사전에 알파벳 모음 'A', 'E', 'I', 'O', 'U'만을 사용하여 만들 수 있는, 길이 5 이하의 모든 단어가 수록되어 있습니다. 사전에서 첫 번째 단어는 "A"이고, 그다음은 "AA"이며, 마지막 단어는 "UUUUU"입니다.

# 단어 하나 word가 매개변수로 주어질 때, 이 단어가 사전에서 몇 번째 단어인지 return 하도록 solution 함수를 완성해주세요.

# 제한사항
# word의 길이는 1 이상 5 이하입니다.
# word는 알파벳 대문자 'A', 'E', 'I', 'O', 'U'로만 이루어져 있습니다.

word = "AAAAE"
# result = 6

# 5자리 : vowel[char]
# 4자리 : (6(n-1)+4)*vowel[char]
# 3자리 : (31(n-1)+3)*vowel[char]
# 2자리 : (156(n-1)+2)*vowel[char]
# 1자리 : (781(n-1)+1)*vowel[char]


# 1차 수정 : 수학적 일반화
def solution(word):
    vowels = {'A':0, 'E':1, 'I':2, 'O':3, 'U':4}
    answer = 0
    for idx, char in enumerate(word):
        answer += vowels[char] * ((5**5-1)//4) // (5**idx) + 1
    return answer
# 0.01ms, 10.3MB


# 초기 코드
def solution(word):
    vowel = ['A', 'E', 'I', 'O', 'U']
    answer = 0
    for i in vowel:
        answer += 1
        if i == word: 
            return answer
        for j in vowel:
            answer += 1
            if i+j == word: 
                return answer
            for k in vowel:
                answer += 1
                if i+j+k == word: 
                    return answer
                for l in vowel:
                    answer += 1
                    if i+j+k+l == word: 
                        return answer
                    for n in vowel:
                        answer += 1
                        if i+j+k+l+n == word: 
                            return answer
# 1.12ms, 10.2MB