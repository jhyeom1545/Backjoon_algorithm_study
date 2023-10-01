def solution(num_list, n):
    answer = []
    tmp_list = []
    num = 0
    for i, v in enumerate(num_list):
        num+=1
        tmp_list.append(v)
        if num == n:
            answer.append(tmp_list)
            tmp_list = []
            num=0
    return answer