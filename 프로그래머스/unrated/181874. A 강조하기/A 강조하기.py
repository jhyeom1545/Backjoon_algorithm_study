def solution(myString):
    result = []
    for i in myString:
        if i == "a" or i == "A":
            result.append("A")
        else:
            result.append(i.lower())
    return "".join(result)