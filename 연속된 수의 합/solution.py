def solution(num, total):
    a = [x for x in range(-49,101)]
    for i in range(150-num):
        e = a[i:i+num]
        if sum(e) == total: return e
print(solution(4,2))