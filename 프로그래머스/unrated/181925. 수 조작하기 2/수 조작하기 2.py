def solution(numLog):
    answer= []
    for i in range(len(numLog)-1):
        if True:
            if numLog[i] + 1 == numLog[i+1]:
                answer.append('w')
            elif numLog[i] -1 == numLog[i+1]:
                answer.append('s')
            elif numLog[i] + 10 == numLog[i+1]:
                answer.append('d')
            else:
                answer.append('a')      
    return "".join(answer)