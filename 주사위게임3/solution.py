def solution(a, b, c, d):# lis = [ex.count(i) for i in ex]로 선언했으면 좀 더 깔끔하게 작성 가능하다는 것을 다른 사람들의 풀이를 보고 알게 됨.
    ex = [a,b,c,d]       # 주관적 난이도 : 중하
    lis = [0]*6
    for i in ex:
        lis[i-1] += 1

    if 4 in lis: answer = 1111*(lis.index(4)+1)

    elif 3 in lis: answer = (10 * (lis.index(3)+1) + (lis.index(1)+1))**2

    elif lis.count(2) == 2:
        p = lis.index(2) + 1
        lis.pop(lis.index(2))
        q = lis.index(2) + 2
        answer = (p+q)*abs(p-q)

    elif lis.count(2) == 1:
        answer = lis.index(1) + 1
        lis.pop(lis.index(1))
        answer *= (lis.index(1) + 2)

    elif max(lis) == 1: answer = lis.index(1) + 1
    return answer
