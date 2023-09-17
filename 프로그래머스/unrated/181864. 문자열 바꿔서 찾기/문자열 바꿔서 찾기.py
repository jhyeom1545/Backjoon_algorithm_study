def solution(myString, pat):
    answer = ""
    
    for i in myString:
        if "A" == i:
            answer+="B"
        else:
            answer+="A"
    if pat in answer:
        return 1
    else:
        return 0