def solution_old(n): #코드가 매우 길고 더러워 만족스럽지 않음. 주관적 난이도 : 상
    lis = [[0]*n for i in range(n)]
    x = []
    y = [0]
    ex = [i for i in range(n)]
    ey = ex[1:]
    for i in range(n):
        if i % 2 == 0:
            x.extend(ex)
            x.extend([x[-1]]*(n-1-i))
            del ex[-1]
            y.extend([y[-1]]*(n-i))
            if ey:
                y.extend(ey)
                del ey[-1]
        else:
            x.extend(ex[::-1])
            x.extend([x[-1]]*(n-1-i))
            del ex[0]
            y.extend([y[-1]]*(n-i))
            if ey:
                y.extend(ey[::-1])
                del ey[0]
    del y[0]
    for i in range(n**2):
        lis[y[i]][x[i]] = i+1
    return lis
def solution(n): # 좌표를 직접 이동하는 좀더 짧은 코드
    result = [[x for x in range(1,n+1)] for i in range(n)] # n*n 리스트 생성
    p = (1,0),(0,-1),(-1,0),(0,1) # 이동할 방향
    num,x,y,pnum = n+1,n-1,0,0 # 변수 선언  num은 n+1 ~ n * n 까지의 값
    for i in range(1,n):
        if pnum > 3: pnum=0
        for _ in range(2):
            for _ in range(n-i):
                y, x, result[y][x] = y + p[pnum][0], x + p[pnum][1], num # 반복마다 x,y에 이동하는 방향의 값을 더하고 result y,x 좌표에 값 넣어주기
                num += 1
            pnum +=1
    return result # 결과 리턴
