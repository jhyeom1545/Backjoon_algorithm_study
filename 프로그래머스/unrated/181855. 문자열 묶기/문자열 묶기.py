def solution(strArr):
    answer = 0
    arr_dic = {}
    result = []
    for i in strArr:
        num = len(i)
        if num not in arr_dic:
            arr_dic[num] = 1
        else: 
            arr_dic[num] +=1
    for k, v in arr_dic.items():
        result.append(v)
    return max(result)