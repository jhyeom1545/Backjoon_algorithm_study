def solution(t, p):
    p_num = len(p)
    answer = 0
    for i in range(len(t)+1-p_num):
        if t[i:i+p_num] <= p:
            answer+=1
    return answer