def solution(my_string, overwrite_string, s):
    start_index = len(my_string)-len(overwrite_string)-1
    answer=[]
    for i in range(s):
        answer.append(my_string[i])
    
    for i in range(len(overwrite_string)):
        answer.append(overwrite_string[i])
    
    # for i in range
    answer.append(my_string[s+len(overwrite_string):])
    
    return "".join(answer)