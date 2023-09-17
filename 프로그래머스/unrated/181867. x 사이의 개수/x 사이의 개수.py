def solution(myString):
    answer = []
    num = 0
    last_num = 0
    for i in range(len(myString)):
        if myString[i] == "x": 
            answer.append(num)
            num = 0
            last_num = len(myString[i:])
        else:
            num+=1
    answer.append(last_num-1)
    return answer