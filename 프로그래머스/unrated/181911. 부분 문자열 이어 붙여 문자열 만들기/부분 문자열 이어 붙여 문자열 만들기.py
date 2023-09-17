def solution(my_strings, parts):
    answer = ''
    # my_strings
    for i in range(len(parts)):
        num1 = parts[i][0]
        num2 = parts[i][1]
        answer+= my_strings[i][num1:num2+1]
    return answer