def solution(arr1, arr2):
    answer = 0
    num1 = 0
    num2 = 0
    
    if len(arr1) > len(arr2):
        answer = 1
        return answer
    elif len(arr1) < len(arr2):
        answer = -1
        return answer
    else:
        for i in range(len(arr1)):
            num1 += arr1[i]
            num2 += arr2[i]
        if num1 > num2:
            answer = 1
            return answer
        elif num2 > num1:
            answer = -1
            return answer
        else:
            answer = 0
            return answer