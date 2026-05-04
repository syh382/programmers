def solution(n): #코드가 좀 길고 더러워 만족스럽지 않음.
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
"""
a = solution(5)
for i in range(a):
    print(i)
"""
