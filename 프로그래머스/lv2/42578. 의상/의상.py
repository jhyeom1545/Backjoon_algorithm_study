def solution(clothes):
    answer = 1
    clothes_dict = {}
    for cloth, category in clothes:
        if category not in clothes_dict:
            clothes_dict[category] = 1
        else:
            clothes_dict[category] += 1
    
    for count in clothes_dict.values():
        answer *= (count + 1)
    
    return answer - 1
