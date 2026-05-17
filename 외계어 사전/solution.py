def solution(spell, dic):
    for i in dic: # "sod", "eocd", "qixm", "adio", "soo"
        for ii in spell: # "p", "o", "s"
            if ii in i: # ii가 i안에 포함되어 있을 때 True
                if ii == spell[-1]: return 1 # ii의 값이 spell의 맨 뒤 인덱스와 동일할때
            else: break # i안에 포함되지 않는 ii가 나올시 반복 중단
    return 2
# spell = set(spell) spell - set(dic) 방식으로 더욱 간단하게 풀이 가능
# 주관적 난이도 최하
# https://school.programmers.co.kr/learn/courses/30/lessons/120869