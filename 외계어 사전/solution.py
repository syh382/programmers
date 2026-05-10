def solution(spell, dic):
    for i in dic:
        for ii in spell:
            if ii in i:
                if spell.index(ii) == len(spell)-1:
                    return 1
            else:
                break
    return 2
# spell = set(spell) spell - set(dic) 방식으로 더욱 간단하게 풀이 가능
# 주관적 난이도 최하
# https://school.programmers.co.kr/learn/courses/30/lessons/120869