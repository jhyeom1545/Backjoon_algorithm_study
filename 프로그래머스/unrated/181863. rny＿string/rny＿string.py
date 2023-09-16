def solution(rny_string):
    result = []
    
    for i in rny_string:
        if i == "m":
            result.append("rn")
        else:
            result.append(i)
        
    return "".join(result)