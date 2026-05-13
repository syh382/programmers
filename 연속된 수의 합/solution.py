def solution(num, total):
    a = 1 if num%2 == 0 else 0
    return  [x for x in range(total // num - num//2 + a, total // num + num//2 + 1)]
# 다른사람들의 풀이를 보면 등차수열로 푸는 방법이 있다.
# 주관적 난이도 중
# https://school.programmers.co.kr/learn/courses/30/lessons/120923