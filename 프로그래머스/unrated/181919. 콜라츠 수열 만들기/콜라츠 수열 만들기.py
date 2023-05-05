def solution(n):
    answer = []
    answer.append(n)
    while(True):
        if n % 2== 0:
            answer.append(n/2)
            n = n/2
        else:
            answer.append(3*n+1)
            n = 3*n+1
        if(n==1):
            break
    return answer