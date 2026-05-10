def solution(priorities, location):
    a = 0
    priorities[location] = float(priorities[location])
    while len(priorities) > 0:
        if priorities[0] >= max(priorities):
            a += 1
            if type(priorities.pop(0)) == float: return a
        else: priorities.append(priorities.pop(0))
