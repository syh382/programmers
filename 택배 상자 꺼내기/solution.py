def solution(n, w, num): 
    lis = [[0]*w for i in range(n//w + 1)]
    a,y,x = 0,0,0
    for i in range(n//w + 1):
        for ii in range(w):
            a+=1
            if a > n: continue
            elif i % 2 == 1:
                lis[i][-ii-1] = a
                if a == num:y,x = i,-ii-1
            else:
                lis[i][ii] = a
                if a == num: y,x = i,ii
    if lis[-1][x]: return len(lis) - y
    else: return len(lis) - y - 1
# 다른사람의 풀이에 패턴을 분석해 반복문 없이 짧게 푸는 방법이 있음..
# 주관적 난이도 : 하
# https://school.programmers.co.kr/learn/courses/30/lessons/389478