def solution(name, yearning, photo):
    answer = []
    num=0
    my_dict = dict(zip(name, yearning))
    for i in range(len(photo)):
        
        for j in range(len(photo[i])):
            for k in range(len(my_dict)):
                if photo[i][j] == name[k]:
                    num+=(my_dict[name[k]])
        answer.append(num)
        num = 0
    return answer