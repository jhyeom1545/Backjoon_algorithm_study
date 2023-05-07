def solution(left, right):
    sum = 0
    answer = []
    num = []
    result = 0
    for i in range(left, right+1):
        num.append(i)
        while(True):
            for k in range(1, i+1):
                if i % k == 0:
                    sum+=1
            break
        answer.append(sum)
        sum = 0
    for i in range(len(answer)):
        if answer[i] % 2 == 0:
            result += num[i]
        else:
            result -= num[i]
    return result

        