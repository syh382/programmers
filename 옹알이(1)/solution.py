def solution(babbling): # 주관적 난이도 : 하
    result = 0
    for i,s in enumerate(babbling):
        for ii in ["aya","ye","woo","ma"]:
            if ii in s:
                babbling[i] = babbling[i].replace(ii, " ") # babbling[i].replace(ii, "")를 하면 양끝에 있던 문자가 붙어 결과값이 늘어나 틀리는 상황 발생
                                                           # babbling[i].replace(ii, " ")로 변경후 for문 다음에 babbling[i] = babbling[i].replace(" ", "") 추가
        babbling[i] = babbling[i].strip() # 맞춘후에 확인한 다른사람의 풀이에서 strip을 사용해 공백을 제거함 replace(" ", "") -> strip()으로 변경
        if len(babbling[i]):
            continue
        else:
            result+=1
    return result

