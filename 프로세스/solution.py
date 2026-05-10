def solution(priorities, location):
    a = 0
    priorities[location] = float(priorities[location])
    while len(priorities) > 0:
        if priorities[0] >= max(priorities):
            a += 1
            if type(priorities.pop(0)) == float: return a
        else: priorities.append(priorities.pop(0))
# 다른사람의 풀이는 다음에 봃예정
# 주관적 난이도 하
# https://school.programmers.co.kr/learn/courses/30/lessons/42587
