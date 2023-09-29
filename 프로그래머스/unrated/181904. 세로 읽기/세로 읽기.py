def solution(my_string, m, c):
    answer_arr = []
    answer=''
    start = 0
    end = m
    for i in my_string:
        answer_arr.append(my_string[start:end])
        start+=m
        end+=m
        if end> len(my_string):
            break
        
    for i in answer_arr:
        answer+=i[c-1]
    return answer