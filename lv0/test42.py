# https://school.programmers.co.kr/learn/courses/30/lessons/120883
# 로그인 성공?

# 문제 설명
# 아이디와 비밀번호가 모두 일치하는 회원정보가 있으면 "login"을 return합니다.
# 로그인이 실패했을 때 아이디가 일치하는 회원이 없다면 “fail”를, 
# 아이디는 일치하지만 비밀번호가 일치하는 회원이 없다면 “wrong pw”를 return 합니다.

# 제한사항
# 회원들의 아이디는 문자열입니다.
# 회원들의 아이디는 알파벳 소문자와 숫자로만 이루어져 있습니다.
# 회원들의 패스워드는 숫자로 구성된 문자열입니다.
# 회원들의 비밀번호는 같을 수 있지만 아이디는 같을 수 없습니다.
# id_pw의 길이는 2입니다.
# id_pw와 db의 원소는 [아이디, 패스워드] 형태입니다.
# 1 ≤ 아이디의 길이 ≤ 15
# 1 ≤ 비밀번호의 길이 ≤ 6
# 1 ≤ db의 길이 ≤ 10
# db의 원소의 길이는 2입니다.

id_pw = ["programmer01", "15789"]
db = [["programmer02", "111111"], ["programmer00", "134"], ["programmer01", "1145"]]

# 기본값을 fail로 주면 좋을듯
answer = 'fail'
# for 문으로 db안의 요소들을 검사
for i in db:
    if i[0]==id_pw[0]: 
        if i[1]==id_pw[1]: 
            answer = 'login'
            break
        else: 
            answer = 'wrong pw'
            break
