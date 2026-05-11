from collections import deque
def solution(priorities, location):
    a = 0
    priorities[location] = float(priorities[location])
    while len(priorities) > 0:
        if priorities[0] >= max(priorities):
            a += 1
            if type(priorities.pop(0)) == float: return a
        else: priorities.append(priorities.pop(0))
# 주관적 난이도 하
# https://school.programmers.co.kr/learn/courses/30/lessons/42587
def solution2(p, location):
    a = 0
    p = deque(p)
    p[location] = float(p[location])
    while len(p) > 0:
        if any(p[0] < i for i in p): p.rotate(-1)
        else: 
            a += 1
            if isinstance(p.popleft(),float): return a
# collections의 deque 사용코드

