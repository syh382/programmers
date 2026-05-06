def solution(lines):
    a = 0
    [[x1, x2], [x3, x4], [x5, x6]] = lines
    print(min(x2,x4) - max(x1,x3))
    
print(solution([[0, 2], [-3, -1], [-2, 1]]))
# 공식 min(x2,x4) - max(x1,x3) 이 0보다 클때 값이 겹치는 길이