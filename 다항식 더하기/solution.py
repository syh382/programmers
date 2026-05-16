def solution(polynomial):
    x,n = 0,0
    for i in polynomial.split(" + "):
        if "x" in i:
            if i[:-1].isdigit(): x+=int(i[:-1])
            else: x+=1
        else: n+=int(i)
    if x:
        if x == 1: x = ''
        if n: return f"{x}x + {n}"
        else: return f"{x}x"
    else: return str(n)
# 케이스 분류가 약간 헷갈리는 부분이 있었음
# 주관적 난이도 중하
# https://school.programmers.co.kr/learn/courses/30/lessons/120863