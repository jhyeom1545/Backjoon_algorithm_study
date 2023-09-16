def solution(myString):
    result = []
    
    for i in myString:
        if ord(i) < ord("l"):
            result.append("l")
        else:
            result.append(i)
    return "".join(result)