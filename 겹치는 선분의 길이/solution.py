from itertools import combinations
def solution(lines):
    lis = [0] * 201 # index 0 ~ 200 == -100 ~ 100
    for line1,line2 in combinations(lines, 2):
        ma, mi = max(line1[0], line2[0]), min(line1[1], line2[1])# 공식 min(x2,x4) - max(x1,x3) 이 0보다 클때 값이 겹치는 길이
        if mi - ma > 0:
            for i in range(ma, mi+1):
                lis[i+100] = 1
            lis[i+100] = 2
    return lis.count(1)
# 구현 실패_정답률 90% (논리 구조 오류 미해결, 정답 확인)
# 재도전 예정 (선을 [0,1] 각 칸에 쌓는 방식으로 구현할것)