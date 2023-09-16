def solution(n):
    limit = 0
    answer = 0
    
    while True:
        if answer % 3 == 0 or '3' in str(answer):
            answer+=1
        else:
            answer+=1
            limit+=1
            if limit == n:
                break
    return answer-1