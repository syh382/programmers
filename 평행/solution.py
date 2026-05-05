def solution(dots): #주관적 난이도 : 하
    slop = lambda a,b : (b[1]-a[1])/(b[0]-a[0])
    if slop(dots[0],dots[1]) == slop(dots[2],dots[3]): return 1
    elif slop(dots[0],dots[2]) == slop(dots[1],dots[3]): return 1
    elif slop(dots[0],dots[3]) == slop(dots[1],dots[2]): return 1
    else: return 0
#다른 사람의 풀이를 보고 [[x1, y1], [x2, y2], [x3, y3], [x4, y4]] = dots 이런식으로도 변수 선언이 가능 하다는 사실을 알게 됨
