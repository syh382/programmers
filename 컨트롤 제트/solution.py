def solution(s):
    lis = s.split()
    sum = 0
    for i,d in enumerate(lis):
        if d == 'Z': sum -= int(lis[i-1])
        else: sum += int(d)
    return sum
# 1점 주는 문제...
# 주관적 난이도 최하
# https://school.programmers.co.kr/learn/courses/30/lessons/120853