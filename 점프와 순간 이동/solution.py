def solution(n):
    energy = 0
    while n != 0:
        if n % 2 :
            n -= 1
            energy += 1
        else : n //= 2
    return energy
# 논리가 2진수 변환과 똑같아 return bin(n).count('1') 한줄로 된다는 것을 알았다
# 주관적 난이도 하
# https://school.programmers.co.kr/learn/courses/30/lessons/12980