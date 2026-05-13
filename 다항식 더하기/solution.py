def solution(polynomial):
    polynomial = polynomial.split()
    x,num = 0,0
    for i in polynomial:
        if "x" in i:
            if i == "x": x += 1
            else:  x += int(i[0])
        elif i.isdigit(): num += int(i)
    if x:
        if num != 0:
            if x == 1: return "x + " + str(num)
            return str(x) + "x + " + str(num)
        if num == 0:
            if x == 1: return "x"
            return str(x) + "x"
    else: return str(num)
    
print(solution("1 + x + 5"))