def solution(babbling):
    result = 0
    for i in babbling:
        for ii in ["aya","ye","woo","ma"]:
            if ii in i: i = i.replace(ii, " ") # 일치하는 부분을 공백으로 대체
        if i.strip(): continue # a 안에 값이 남아있으면 발음할수 없는것으로 간주
        result+=1 # 문자열 a에 값이 없을때 결과 + 1
    return result
# 주관적 난이도 하 
# 공백 제거를 replace(" ", "")가 아닌 strip()으로 더 깔끔(?) 하게 하기
# https://school.programmers.co.kr/learn/courses/30/lessons/120956