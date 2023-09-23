def solution(strArr):
    answer = []
    print(strArr)
    not_ad = ''
    for i in strArr:
        if 'ad' in i:
            pass
        else:
            answer.append(i)
    print(not_ad)
    return answer