from collections import deque
def solution(priorities, location):
    a = 0
    priorities[location] = float(priorities[location])
    while len(priorities) > 0:
        if priorities[0] >= max(priorities):
            a += 1
            if type(priorities.pop(0)) == float: return a
        else: priorities.append(priorities.pop(0))
print(solution([2, 1, 3, 2],2),time.time()-start)
# 다른사람의 풀이는 다음에 봃예정
# 주관적 난이도 하
# https://school.programmers.co.kr/learn/courses/30/lessons/42587
def solution2(p, location):
    a = 0
    p = deque(p)
    p[location] = float(p[location])
    while len(p) > 0:
        if p[0] >= max(p):
            a += 1
            if isinstance(p.popleft(),float): return a
        else: p.rotate(-1)
# collections의 deque를 사용한 코드.
# 시간복잡도를 n^2에서 n으로 줄임
